from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    #button = browser.find_element_by_tag_name("button")
    #button.click()
    time.sleep(3)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #browser.execute_script("window.scrollBy(0, 100);")
    button.click()

finally:
    time.sleep(3)
    browser.quit()