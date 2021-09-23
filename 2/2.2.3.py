from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/selects1.html'
    browser.get(link)
    num1 = (browser.find_element_by_id('num1')).text
    num2 = (browser.find_element_by_id('num2')).text
    sum = str(int(num1) + int(num2))
    print ('num1 is: ' + num1, 'num2 is : ' + num2, 'and sum is: ' + sum)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(sum)
    btn = browser.find_element_by_class_name('btn').click()


finally:
    time.sleep(5)
    browser.quit()