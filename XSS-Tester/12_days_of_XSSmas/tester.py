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

success = 0
fail = 0
url = "https://playground.insecure.chefsecure.com/the-12-exploits-of-xssmas"
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")   #don't show Chrome(enable this if you don't want chrome to open up)
#chrome_options.add_argument("window-size=1920,1080") #standardize height(ignore this)
driver = webdriver.Chrome(options=chrome_options)   #This is chrome driver is from Chrome Version 83.0.4103.39. This won't work if your chrome isn't updated
driver.get(url)
old_page = driver.page_source
inputBox = driver.find_element_by_id("textarea")
injectButton = driver.find_element_by_id("update")

f = open('./mal-very-high/2000.txt', encoding="utf8") #<----- input file here
inputAttacks = f.readlines()
f.close()
working = []


for i in range(len(inputAttacks)):
    try:
        #print('pass:', success, '| fail:', fail)
        inputBox.clear()
        inputBox.send_keys(inputAttacks[i])
        injectButton.click()
        time.sleep(0.15)
        alert = driver.switch_to.alert
        #print('yes', inputAttacks[i])
        alert.accept()
        success = success + 1
        #working.append(inputAttacks[i])
    except TimeoutException:
        driver.get(url)
        old_page = driver.page_source
        inputBox = driver.find_element_by_id("textarea")
        injectButton = driver.find_element_by_id("update")
    except NoAlertPresentException:
        try:
            if driver.current_url != url:
                #('yes,', inputAttacks[i], '->', driver.current_url)
                success = success + 1
                time.sleep(1)
                driver.get(url)
                old_page = driver.page_source
                inputBox = driver.find_element_by_id("textarea")
                injectButton = driver.find_element_by_id("update")
            else:
                print('no: ', inputAttacks[i])
                fail = fail + 1
        except NoSuchElementException:
            time.sleep(1)
            driver.get(url)
            old_page = driver.page_source
            inputBox = driver.find_element_by_id("textarea")
            injectButton = driver.find_element_by_id("update")

    except(NoSuchElementException, UnexpectedAlertPresentException, ElementNotInteractableException, StaleElementReferenceException):
        try:
            #print('NO,', inputAttacks[i], '->', driver.current_url)
            time.sleep(1)
            driver.get(url)
            old_page = driver.page_source
            inputBox = driver.find_element_by_id("textarea")
            injectButton = driver.find_element_by_id("update")
        except UnexpectedAlertPresentException:
            try:
                #print('NO!,', inputAttacks[i], '->', driver.current_url)
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(1)
                driver.get(url)
                old_page = driver.page_source
                inputBox = driver.find_element_by_id("textarea")
                injectButton = driver.find_element_by_id("update")
            except NoAlertPresentException:
                #print('NO!!,', inputAttacks[i], '->', driver.current_url)
                driver.get(url)
                old_page = driver.page_source
                inputBox = driver.find_element_by_id("textarea")
                injectButton = driver.find_element_by_id("update")

driver.quit()
print('passed:',success)
print('failed:', fail)

'''with open("ouput.txt", "w") as output:
    output.writelines(working)'''