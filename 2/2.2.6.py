from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/execute_script.html'
    browser.get(link)
# Считать значение для переменной x.
    x = (browser.find_element_by_xpath('//*[@id="input_value"]')).text
    print(x)
# Посчитать математическую функцию от x.
    y = calc(x)
    print(y)
# Проскроллить страницу вниз.
    button = browser.find_element_by_xpath('/html/body/div/form/button')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")

# Ввести ответ в текстовое поле.
    answer = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

# Выбрать checkbox "I'm the robot".
    robot = browser.find_element_by_id('robotCheckbox').click()

# Переключить radiobutton "Robots rule!".
    radioRobot = browser.find_element_by_id('robotsRule').click()

# Нажать на кнопку "Submit".
    button.click()

finally:
    time.sleep(5)
    browser.quit()