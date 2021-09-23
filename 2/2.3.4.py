from selenium import webdriver
import time
import pyperclip
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    link2 = 'https://stepik.org/lesson/184253/step/4?unit=158843'
    browser.get(link)
# Нажать на кнопку
    button = browser.find_element_by_css_selector('.btn').click()
# Принять confirm
    confirm = browser.switch_to_alert()
    confirm.accept()
    time.sleep(2)
# На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_css_selector('#input_value').text
    print('the x value is: ', x)
    answer = browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    print('the answer is: ', calc(x))
    submit = browser.find_element_by_css_selector('.btn').click()
    alert = browser.switch_to_alert()
    alert_text = alert.text

    print('the alert text is: ', alert_text)
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    print('the final answer is:', addToClipBoard)
    alert.accept()


finally:
    time.sleep(5)
    browser.quit()
