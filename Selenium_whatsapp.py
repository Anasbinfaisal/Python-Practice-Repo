
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
print("Scan QR code and Press enter")
input()
print("Logged In")
time.sleep(5)
contact = 'Mum'
mssg = 'Whatsapp TEST Message!!!!'


search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
for i in range(30):
    mssg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    mssg_box.send_keys(random.choice(mssg))
    mssg_box.send_keys(Keys.ENTER)
time.sleep(100)
driver.quit()