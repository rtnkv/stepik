from selenium import webdriver
from  pathlib import *
import os
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    first_name = browser.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys('Ivan')
    last_name = browser.find_element_by_css_selector('input.form-control:nth-child(4)').send_keys('Ivanov')
    email = browser.find_element_by_css_selector('input.form-control:nth-child(6)').send_keys('ivan@ivanov.ii')
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'test.txt')
    send_file = browser.find_element_by_css_selector('#file').send_keys(file_path)
    button = browser.find_element_by_css_selector('.btn').click()
finally:
    time.sleep(5)
    browser.quit()