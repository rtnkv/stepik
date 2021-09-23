from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    first_window = browser.window_handles[0]
    time.sleep(3)
    browser.find_element_by_css_selector('.trollface').click()
    #disable troll button movements
    #browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    new_window = browser.window_handles[1]
    time.sleep(0.5)
    browser.switch_to_window(first_window)
    print('switched to window 1')
    time.sleep(0.5)
    browser.switch_to_window(new_window)
    print('switched back to new window')

    x = browser.find_element_by_css_selector('#input_value').text
    answer = browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    button = browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(5)
    browser.quit()