from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work!');")




finally:
    browser.quit()