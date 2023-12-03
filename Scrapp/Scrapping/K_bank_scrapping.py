import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

start = time.time()
load_dotenv()

def main():
    try:
        driver = webdriver.Chrome()
        url = "https://kbiz.kasikornbank.com/authen/login.jsp?lang=th" 
        driver.get(url)
        sleep = 0.5

        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "userName")
        inputm.send_keys(os.getenv("USER"))

        time.sleep(sleep)
        inputm = driver.find_element(By.NAME, "password")
        inputm.send_keys(os.getenv("PASSWORD"))
        
        time.sleep(sleep)
        login = driver.find_element(By.ID, "loginBtn")
        login.click()

        time.sleep(sleep)
        logout = driver.find_element(By.XPATH, '//*[@id="userprofile"]/ul/li[2]/button')
        logout.click()
        #get value
        time.sleep(sleep)
        logout = driver.find_element(By.XPATH, '/html/body/app-root/menu-main/div[1]/main/div/div[2]/app-account-business/div/app-account-summary/app-ads/div[2]/div[1]/div[1]/div/p/span')
        print(logout.text)

        time.sleep(sleep)
        logout_confirm = driver.find_element(By.XPATH, '//*[@id="popup-alert-logout"]/div/div/a[2]')
        logout_confirm.click()

    finally:
        driver.quit() 


if __name__ == "__main__":
    main()

end = time.time()
print("Use time", end - start," s")