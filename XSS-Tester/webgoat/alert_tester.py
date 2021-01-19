from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

url = "http://localhost:8080/WebGoat/"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)   #This is chrome driver is from Chrome Version 83.0.4103.39. This won't work if your chrome isn't updated
driver.get(url)
old_page = driver.page_source
email = driver.find_element_by_id("exampleInputEmail1")
password = driver.find_element_by_id("exampleInputPassword1")
sign_in_button = driver.find_element_by_tag_name("button")
email.send_keys("yfrempon")
password.send_keys("frempong7")
sign_in_button.click()

pass_cnt = 0
fail_cnt = 0
mode = 1
reset_flag = False

f = open('./alert_payloads.txt', encoding="utf8") #<----- input file here
inputAttacks = f.readlines()

#alert demo
if mode == 1:
    driver.get("http://localhost:8080/WebGoat/start.mvc#lesson/CrossSiteScripting.lesson/6")
    time.sleep(5)
    input_field = driver.find_element_by_xpath('//*[@id="lessonContent"]/form/table[2]/tbody/tr[3]/td[2]/input')
    send_button = driver.find_element_by_xpath('//*[@id="lessonContent"]/form/table[2]/tbody/tr[5]/td/input')

    for attack in inputAttacks:
        print('hi')
        if reset_flag:
            reset_flag = False
            time.sleep(5)

        input_field.clear()
        input_field.send_keys(attack)
        send_button.click()
        try:
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
            driver.get("http://localhost:8080/WebGoat/start.mvc#lesson/CrossSiteScripting.lesson/7")
            driver.get("http://localhost:8080/WebGoat/start.mvc#lesson/CrossSiteScripting.lesson/6")
            reset_flag = True
            print('pass')
        except:
            print('fail')
