import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)
email = input("Enter mail:")
name = input("Enter name:")
        
       
pas = ''
for x in range(16):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

driver.get('https://discord.com/register')
driver.find_element(By.NAME , "email").send_keys(email)
driver.find_element(By.NAME , "username").send_keys(name)
driver.find_element(By.NAME, "password").send_keys(pas)
action.key_down(Keys.TAB).send_keys('MAY').perform()
action.key_down(Keys.TAB).send_keys('1').perform()
action.key_down(Keys.TAB).send_keys('1990').perform()
driver.find_element(By.CLASS_NAME, "contents-3ca1mk").click()
time.sleep(50)

for request in driver.requests:
    print(request.headers['Authorization'])
