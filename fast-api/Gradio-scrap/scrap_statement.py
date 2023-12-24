import time
import gradio as gr
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

opt = Options()
opt.add_argument("--no-sandbox")
opt.add_argument("--headless")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--window-size=700,700")
mongo_url = "mongodb+srv://admin:November@userdata.ipq1o58.mongodb.net/"
    
    

def scrap_statement(u_bank, p_bank):
    print("*- statement scraping -*")
    try:
        driver = webdriver.Chrome(options= opt)
        start = time.time()
        url = "https://kbiz.kasikornbank.com/authen/login.jsp?lang=th" 
        driver.get(url)
        sleep = 2

        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "userName")
        inputm.send_keys(u_bank)

        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "password")
        inputm.send_keys(p_bank)

        time.sleep(sleep)
        login = driver.find_element(By.ID, "loginBtn")
        login.click()
        
        print("-- login - yes")
        time.sleep(sleep)
        account = driver.find_element(By.XPATH, "/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary/app-ads/div[2]/div[2]/div/app-account-summary-card/div/div[3]/a")
        account.click()

        time.sleep(sleep)
        bar = driver.find_element(By.XPATH, '//*[@id="buttonMobileDDLID_title"]')
        bar.click()

        print("-- account - yes")
        time.sleep(sleep)
        statement = driver.find_element(By.XPATH, '//*[@id="buttonMobileDDLID_child"]/ul/li[2]/img')
        statement.click()

        print("-- statement - yes")
        time.sleep(sleep)
        email = driver.find_element(By.XPATH, '//*[@id="statement"]/div[2]/label/span')
        email.click()

        time.sleep(sleep)
        month = driver.find_element(By.XPATH, '//*[@id="advance-type-2"]/div[4]/div/div/div[12]/label/span')
        month.click()

        time.sleep(sleep)
        confirm = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary-main/app-account-statement/div[1]/div/div/form/div/a')
        confirm.click()

        time.sleep(sleep)
        confirm = driver.find_element(By.XPATH, '//*[@id="popup-sent-email-success"]/div/div/a')
        confirm.click()
        driver.quit()
        end = time.time()
        use_time = end - start
        print(f"* statement sent ✅ time: {use_time}*")
        return "Success"
    except WebDriverException as e:
        print(e)
        return "Error"

def statementdata_name(name):
    client = MongoClient(mongo_url)
    db = client[name]
    col = db["login"]
    bank = col.find_one({"name" : name})
    if bank == None:
        return {"result" : f"Not found data in '{name}' account"}
    u_bank = bank["bank_u"]
    p_bank = bank["bank_p"]
    col = db["status"]
    col.update_one({"tag" :"status"},{"$set" : {"statement" : "yes"}})
    result = scrap_statement(u_bank, p_bank)
    col.update_one({"tag" :"status"},{"$set" : {"statement" : "no"}})
    return {"result" : f"Scrap Statement completed {result}"}

with gr.Blocks() as iface:
    with gr.Tab("statement_scrap"):
        st_n_input = gr.Textbox()
        st_n_output = gr.Textbox()
        st_n_button = gr.Button("statement")

    st_n_button.click(statementdata_name, inputs=st_n_input, outputs=st_n_output)

iface.launch()