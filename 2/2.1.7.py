from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('treasure')
    x_valuex = x.get_attribute('valuex')
    print('this is x: ', bool(x))
    print('this is x.text: ', bool(x.text))
    print('this is x_value: ', x_valuex)

    y = calc(x_valuex)

    checkbox = browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id('robotsRule').click()
    answer = browser.find_element_by_id('answer').send_keys(y)
    btn = browser.find_element_by_class_name('btn').click()

finally:
#    time.sleep(5)
    browser.quit()