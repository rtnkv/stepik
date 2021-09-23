from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    browser.implicitly_wait(5)

    get_num = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    if get_num == True:
        done = browser.find_element_by_id('book').click()

    value = browser.find_element_by_xpath('//*[@id="input_value"]').text
    correct_value = calc(str(value))
    text_field = browser.find_element_by_css_selector('#answer').send_keys(correct_value)
#    write_answer = browser.execute_script('return argument[0].scrollIntoView(true);', text_field)
    solve = browser.find_element_by_css_selector('#solve').click()
#    alert = browser.switch_to.alert.accept()
finally:
    time.sleep(5)
    browser.quit()