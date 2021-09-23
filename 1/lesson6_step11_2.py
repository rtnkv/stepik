from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[1]/input")
    input1_message = input1.get_attribute("placeholder")
    print(input1_message)
    if input1_message == "Input your first name":
        input1.send_keys("Ivan")

    input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[2]/input")
    input2_message = input1.get_attribute("placeholder")
    print(input1_message)
    if input2_message == "Input your last name":
        input1.send_keys("Petrov")

    input1 = browser.find_element_by_xpath("//div[1]/form/div[1]/div[3]/input")
    input3_message = input1.get_attribute("placeholder")
    if input3_message == "Input your email":
        input1.send_keys("Ivan@petrov.rq")


    time.sleep(5)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # print("passed")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()