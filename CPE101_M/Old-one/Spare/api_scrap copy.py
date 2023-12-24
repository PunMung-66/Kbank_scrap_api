import time
from fastapi import APIRouter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


async def scrap_balance():
    start = time.time()
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(opt)
    url = "https://kbiz.kasikornbank.com/authen/login.jsp?lang=th" 
    driver.get(url)
    sleep = 2

    time.sleep(sleep)
    inputm = driver.find_element(By.NAME, "userName")
    inputm.send_keys("Punnawat01")

    time.sleep(sleep)
    inputm = driver.find_element(By.NAME, "password")
    inputm.send_keys("NonutNovember0!")
        
    time.sleep(sleep)
    login = driver.find_element(By.ID, "loginBtn")
    login.click()

    print("-- login - yes")
    #get value
    time.sleep(sleep + 3)
    balance = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary/app-ads/div[2]/div[1]/div[1]/div/p/span')
    bal = balance.text
    
    print("-- get value - yes")
    time.sleep(sleep)
    logout = driver.find_element(By.XPATH, '//*[@id="userprofile"]/ul/li[2]/button')
    logout.click()

    time.sleep(sleep)
    logout_confirm = driver.find_element(By.XPATH, '//*[@id="popup-alert-logout"]/div/div/a[2]')
    logout_confirm.click()

    driver.quit()
    end = time.time()
    use_time = end - start
    return (bal, use_time)

async def scrap_statement():
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
        inputm.send_keys("Punnawat01")

        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "password")
        inputm.send_keys("NonutNovember0!")

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

        time.sleep(sleep+0.5)
        logout = driver.find_element(By.XPATH, '//*[@id="userprofile"]/ul/li[2]/button')
        logout.click()

        time.sleep(sleep+0.5)
        logout_confirm = driver.find_element(By.XPATH, '//*[@id="popup-alert-logout"]/div/div/a[2]')
        logout_confirm.click()

    finally:
        driver.quit()
        end = time.time()
        use_time = end - start
        return use_time

router = APIRouter(
    prefix="/scrap",
    tags=["scrap"],
    responses={404: {"message": "Not found"}}
)

@router.get('/')
async def scrap():
    return {"result" : "Scrap"}

@router.get('/balance')
async def balance_scrap_api():
    balance_i, time_use =  await scrap_balance()
    return {"balance" : f"{balance_i} ฿",
            "Use time" : "%.2f" % time_use}

@router.get('/statement')
async def statement_scrap_api():
    time_use = await scrap_statement()
    return {"result" : "Scrap Statement completed",
            "Use time" : "%.2f s" % time_use}