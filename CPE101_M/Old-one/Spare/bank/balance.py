import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def scrap_balance():
    start = time.time()
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(opt)
    url = "https://kbiz.kasikornbank.com/authen/login.jsp?lang=th" 
    driver.get(url)
    sleep = 3

    time.sleep(sleep)
    inputm = driver.find_element(By.NAME, "userName")
    inputm.send_keys("Punnawat01")

    time.sleep(sleep)
    inputm = driver.find_element(By.NAME, "password")
    inputm.send_keys("NonutNovember0!")
        
    time.sleep(sleep)
    login = driver.find_element(By.ID, "loginBtn")
    login.click()
        #get value
    time.sleep(sleep)
    balance = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary/app-ads/div[2]/div[1]/div[1]/div/p/span')
    print(balance.text)
        
    time.sleep(sleep)
    logout = driver.find_element(By.XPATH, '//*[@id="userprofile"]/ul/li[2]/button')
    logout.click()

    time.sleep(sleep)
    logout_confirm = driver.find_element(By.XPATH, '//*[@id="popup-alert-logout"]/div/div/a[2]')
    logout_confirm.click()

    driver.quit() 
    end = time.time()
    print("Use time", end - start," s")
scrap_balance()