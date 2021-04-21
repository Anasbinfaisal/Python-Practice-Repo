
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
contact = 'Contact_Name' //contact to be sent a message
mssg = 'Whatsapp TEST Message!!!!' //message

//Search Box 
search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]') //Search box xpath
search_box.send_keys(contact) //enter contact to be searched in search box
search_box.send_keys(Keys.ENTER) ////pressing enter after entering the contact 
time.sleep(5)
for i in range(30):     //To Send 30 Messages
    mssg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') //Message Box Xpath
    mssg_box.send_keys(mssg) //Message to be sent
    mssg_box.send_keys(Keys.ENTER) //pressing enter after entering the message
time.sleep(100)
driver.quit()
