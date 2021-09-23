from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/math.html'

browser.get(link)

checkbox1 = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
radio1 = browser.find_element_by_css_selector('[for="robotsRule"]').click()

x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
x = x_element.text
y = calc(x)
print('x is equals = ' + x)
print('y is equals = ' + y)

answer = browser.find_element_by_id('answer').send_keys(y)
button = browser.find_element_by_xpath('/html/body/div/form/button').click()



time.sleep(10)
browser.quit()