#import selenium
#from selenium import webdriver

#from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import getpass



def oj_login(driver) :
    id_box = driver.find_element(By.XPATH, '//*[@id="id"]')
    pwd_box = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_btn = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div/div/form/div[2]/input"
    )
    
    id_box.send_keys(input("자신의 아이디 : "))
    pwd_box.send_keys(getpass.getpass("자신의 비밀번호 : "))


    login_btn.click()

    try:
        print(driver.get_issue_message)

        if driver.get_issue_message:
            print(Alert(driver).text)
            driver.quit()
    except:
        print("PASS")
