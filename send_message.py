import pywhatkit as kit
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

phone_number = "+91 1234567890" 
message = "Hello using AI"  

kit.sendwhatmsg_instantly(phone_number, message)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") 

driver = webdriver.Chrome(options=chrome_options)

time.sleep(5)

send_button_xpath = '//button[@data-testid="compose-btn-send"]'
send_button = driver.find_element(By.XPATH, send_button_xpath)
send_button.click()

input("Message sent! Press Enter to exit...")
driver.quit()