from selenium import webdriver
import time

link = 'http://suninjuly.github.io/math.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

# проверяе значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio is:', people_checked)
    assert people_checked is not None, 'People radio is not selected by default'

#проверяем значение аттрибута checked у robots radio
    robots_radio = browser.find_element_by_id('robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of robots radio is:', robots_checked)
    assert robots_checked is None

#проверяем значение аттридута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute('disabled')
    print('vaulue of button Submit is:', button_disabled)
    assert button_disabled is None

#проверяем значение атрибута disabled у кнопки Submit после таймаута
#    time.sleep(10)
    button_disabled2 = button.get_attribute('disabled')
    print('value of button Submit after 10 sec is:', button_disabled2)
    assert button_disabled2 is not None


finally:
    browser.quit()
