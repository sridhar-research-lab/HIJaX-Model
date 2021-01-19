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
    url = 'http://localhost/bWAPP/xss_ajax_1-1.php'
    driver.get(url)

    success = 0
    time.sleep(5)
    for input in input_arr:
        try:
            input_1 = driver.find_element_by_xpath('//*[@id="title"]')
            input_1.clear()
            encoded_input = str(escape(input)).replace('x27','39')
            input_1.send_keys(encoded_input)
            time.sleep(1)
        except UnexpectedAlertPresentException:
            success += 1
            driver.get(url)

    score = (success/len(input_arr)) * 100
    print('success:', str(success), ' out of', str(len(input_arr)))
    print('score:', str(score), '%')

