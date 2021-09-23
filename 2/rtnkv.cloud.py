from selenium import webdriver
import string
import random

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


try:
    #first we need to take text
    text = input('Send text here:  ')
    print('Process started')

    #options
    options = webdriver.ChromeOptions()

    #headless mode
#    options.add_argument('--headless')
    options.headless = True


    #then open the links
#    browser = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')
    browser = webdriver.Chrome(
        options=options
    )
    browser.implicitly_wait(5)

    bin = 'https://rtnkv.cloud/bin/'
    lstu = 'https://rtnkv.cloud/lstu/'

    browser.get(bin)


    #Now we put it to pastebin
    dataInput = browser.find_element_by_css_selector('#message').send_keys(text)
    print('3')
    #expiration date feature
    #expirationDate =

    #now we click Publish button
    Publish = browser.find_element_by_css_selector('#sendbutton').click()
    print('2')

    pasteURL = browser.find_element_by_id('pasteurl')
    print('1')
    print('This is pastebin link: ', pasteURL.text)

    deleteLink = browser.find_element_by_id('deletelink').find_element_by_tag_name('a').get_attribute('href')
    print('This is delete link: ', deleteLink)

    #now get the short links
    print('Shorten the links.')
    browser.get(lstu)
    longLink = browser.find_element_by_xpath('//*[@id="lsturl"]').send_keys(pasteURL)
    customName = browser.find_element_by_css_selector('#lsturl-custom').send_keys(id_generator(5))
    shortIt = browser.find_element_by_css_selector('.button').click()
    shrt = browser.find_element_by_css_selector('#input-short').get_attribute('value')

    longLinkDel = browser.find_element_by_css_selector('#lsturl').send_keys(deleteLink)
    customNameDel = browser.find_element_by_css_selector('#lsturl-custom').send_keys(id_generator(5))
    shortItDel = browser.find_element_by_css_selector('.button').click()
    shrtDel = browser.find_element_by_css_selector('#input-short').get_attribute('value')
    print('This is short privatebin link: ', shrt)
    print('This is short delete link', shrtDel)


finally:
    browser.close()
    browser.quit()