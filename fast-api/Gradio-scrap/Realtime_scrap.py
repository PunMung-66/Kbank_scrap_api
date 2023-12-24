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
mongo_url = "mongodb+srv://admin:November@userdata.ipq1o58.mongodb.net/"
client = MongoClient(mongo_url)

def scrap_balance( u_bank, p_bank, name):
    try:
        db = client[name]
        col = db["status"]
        driver = webdriver.Chrome(options= opt)
        start = time.time()
        url = "https://kbiz.kasikornbank.com/authen/login.jsp?lang=th" 
        driver.get(url)
        print("*- balance scraping -*")
        sleep = 2
        if col.find_one()["statement"] == "yes":
                return "Error"
        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "userName")
        inputm.send_keys(u_bank)

        if col.find_one()["statement"] == "yes":
                return "Error"
        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "password")
        inputm.send_keys(p_bank)

        if col.find_one()["statement"] == "yes":
                return "Error"    
        time.sleep(sleep)
        login = driver.find_element(By.ID, "loginBtn")
        login.click()

        print("-- login - yes")
        #get value
        time.sleep(sleep)
        balance = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary/app-ads/div[2]/div[1]/div[1]/div/p/span')
        bal = balance.text
        print("-- get value - yes")
        driver.quit()
        end = time.time()
        use_time = end - start
        print(f"* balance scraped ✅ time: {use_time}, balance: {bal} ฿*")
        return bal

    except WebDriverException as e:
        print(e)
        return "Error"

import datetime

date = datetime.datetime.now()
today = date.day

user = "test"
balance_i  = 0
round_= 0

def balancedata_name():
    old_dbs = []
    while True:
        client = MongoClient(mongo_url)
        global balance_i
        global user
        global round_
        global today

        dbs = client.list_database_names()
        print(dbs)
        print(old_dbs)

        if old_dbs != dbs:
            new_one = list(set(dbs) - set(old_dbs))
            for name in new_one:
                if name == "admin" or name == "local" or name == "config":
                    continue
                db = client[name]
                col = db["login"]
                if col.find_one() == None:
                    continue
                bank = col.find_one({"name" : name})
                u_bank = bank["bank_u"]
                p_bank = bank["bank_p"]
                balance_i = scrap_balance(u_bank, p_bank, name)
                if balance_i == "Error":
                    print(f"Error in '{name}' account")
                    continue
                user = name
                balance_i = float(balance_i)
                col = db["status"]
                if col.find_one()["statement"] == "yes":
                    continue
                if col.find_one() != None :
                    col.update_one({"tag" :"status"},{"$set" : {"previous" : balance_i}})
                    col.update_one({"tag" :"status"},{"$set" : {"current" : balance_i}})
                    col.update_one({"tag" :"status"},{"$set" : {"goal" : 0}})
                    col.update_one({"tag" :"status"},{"$set" : {"summary" : balance_i - col.find_one()["goal"]}})
                print(f"Update '{name}' status completed")
        
        if old_dbs == dbs:
            for name in dbs:
                today_now = datetime.datetime.now().day

                if name == "admin" or name == "local" or name == "config":
                    continue
                db = client[name]
                col = db["login"]

                if col.find_one() == None:
                    print(f"Not found data in '{name}' account")
                    continue
                bank = col.find_one({"name" : name})
                u_bank = bank["bank_u"]
                p_bank = bank["bank_p"]

                col = db["status"]
                if col.find_one()["statement"] == "yes":
                    continue
                balance_i = scrap_balance(u_bank, p_bank, name)
                if balance_i == "Error":
                    print(f"Error in '{name}' account")
                    continue
                user = name
                balance_i = float(balance_i)
                if col.find_one() != None :
                    if today_now != today:
                        today = today_now
                        # col.update_one({"tag" :"status"},{"$set" : {"previous" : col.find_one()["current"]}})
                        col.update_one({"tag" :"status"},{"$set" : {"usage_d" : 0}})
                    elif today_now == today:
                        col.update_one({"tag" :"status"},{"$set" : {"previous" : col.find_one()["current"]}})
                    col.update_one({"tag" :"status"},{"$set" : {"current" : balance_i}})
                    if col.find_one()["previous"] > col.find_one()["current"]:
                        col.update_one({"tag" :"status"},{"$inc" : {"usage_d" : col.find_one()["previous"] - col.find_one()["current"]}})    
                    col.update_one({"tag" :"status"},{"$set" : {"summary" : balance_i - col.find_one()["goal"]}})
                print(f"Update '{name}' status completed")
        old_dbs = dbs
    # return {"balance" : balance_i,
    #         "status" : f"Update '{name}' status completed"}
#####################################################################
balancedata_name()
# def balance():
#     return balance_i

# # Start the background task in a separate thread
# background_thread = threading.Thread(target=balancedata_name)
# background_thread.daemon = True
# background_thread.start()

# with gr.Blocks() as iface:
#     gr.Markdown("Scrap TEST.")
#     with gr.Tab("balance_scrap"):
#         ba_n_output = gr.Textbox()
#         ba_n_button = gr.Button("balance")
#     ba_n_button.click(balance, outputs=ba_n_output)

# iface.launch()