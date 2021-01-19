from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
from html import unescape
from html import escape

if __name__ == '__main__':

    #load in data from file
    input_arr = []
    file = open('input.txt', 'r')
    for line in file:
        input_arr.append(line.strip())

    #open Chrome and go to bwapp
    url = "http://localhost/bWAPP/login.php"
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)

    #find login elements
    login = driver.find_element_by_xpath('//*[@id="login"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    submit = driver.find_element_by_xpath('//*[@id="main"]/form/button')

    login.send_keys('bee')
    password.send_keys('bug')
    submit.click()

    #reflected-get page
    url_og = 'http://localhost/bWAPP/xss_stored_1.php'
    driver.get(url_og)

    success = 0
    time.sleep(5)
    for input in input_arr:
        textbox = driver.find_element_by_xpath('//*[@id="entry"]')
        textbox.send_keys(input)
        submit_button = driver.find_element_by_xpath('//*[@id="main"]/form/table/tbody/tr[2]/td[1]/button')
        submit_button.click()

    score = (success/len(input_arr)) * 100
    print('success:', str(success), ' out of', str(len(input_arr)))
    print('score:', str(score), '%')

