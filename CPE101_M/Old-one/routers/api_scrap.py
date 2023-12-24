import time
from fastapi import APIRouter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:November@userdata.ipq1o58.mongodb.net/")

async def scrap_balance( u_bank, p_bank):
    start = time.time()
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(opt)
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
    #get value
    time.sleep(sleep + 3)
    balance = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary/app-ads/div[2]/div[1]/div[1]/div/p/span')
    bal = balance.text
    print("-- get value - yes")
    driver.quit()
    end = time.time()
    use_time = end - start
    return (bal, use_time)

async def scrap_statement(u_bank, p_bank):
    try:
        start = time.time()
        opt = Options()
        opt.add_argument("--headless")
        driver = webdriver.Chrome(opt)
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
        time.sleep(sleep + 2 )
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
        time.sleep(sleep + 2)
        email = driver.find_element(By.XPATH, '//*[@id="statement"]/div[2]/label/span')
        email.click()

        time.sleep(sleep)
        month = driver.find_element(By.XPATH, '//*[@id="advance-type-2"]/div[4]/div/div/div[12]/label/span')
        month.click()

        time.sleep(sleep)
        confirm = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary-main/app-account-statement/div[1]/div/div/form/div/a')
        confirm.click()

        time.sleep(sleep+0.5)
        confirm = driver.find_element(By.XPATH, '//*[@id="popup-sent-email-success"]/div/div/a')
        confirm.click()

    finally:
        driver.quit()
        end = time.time()
        use_time = end - start
        return use_time

router = APIRouter(
    tags=["scrap"],
    responses={404: {"message": "Not found"}}
)


@router.get('/balance/{name}')
async def balance_scrap_api(name):
    db = client[name]
    col = db["login"]
    bank = col.find_one({"name" : name})
    if bank == None:
        return {"result" : f"Not found data in '{name}' account"}
    u_bank = bank["bank_u"]
    p_bank = bank["bank_p"]
    balance_i, time_use =  await scrap_balance(u_bank, p_bank)
    return {"balance" : f"{balance_i} ฿",
            "Use time" : "%.2f" % time_use}

@router.get('/statement/{name}')
async def statement_scrap_api(name):
    db = client[name]
    col = db["login"]
    bank = col.find_one({"name" : name})
    if bank == None:
        return {"result" : f"Not found data in '{name}' account"}
    u_bank = bank["bank_u"]
    p_bank = bank["bank_p"]
    time_use = await scrap_statement(u_bank, p_bank)
    return {"result" : "Scrap Statement completed",
            "Use time" : "%.2f s" % time_use}