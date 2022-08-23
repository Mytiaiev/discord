import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver

class GetToken:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)
    def __init__(self, email, name):
        self.email = email
        self.name = name
        
       
    @classmethod    
    def registration(cls, email:str, name:str)->str:
        "take email and name, to use that str in registration field.password will be generate"    
        pas = ''
        for x in range(16):
            pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        cls.driver.get('https://discord.com/register')
        cls.driver.find_element(By.NAME , "email").send_keys(email)
        cls.driver.find_element(By.NAME , "username").send_keys(name)
        cls.driver.find_element(By.NAME, "password").send_keys(pas)
        cls.action.key_down(Keys.TAB).send_keys('MAY').perform()
        cls.action.key_down(Keys.TAB).send_keys('1').perform()
        cls.action.key_down(Keys.TAB).send_keys('1990').perform()
        cls.driver.find_element(By.CLASS_NAME, "contents-3ca1mk").click()
        time.sleep(50)

        for request in cls.driver.requests:
            print(request.headers['Authorization'])

test = GetToken
test.registration("pyyemy@gmail.com","YA")