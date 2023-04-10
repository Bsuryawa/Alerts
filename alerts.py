from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window
driver.find_element(By.ID, "name").send_keys("Bhagyashri")
driver.find_element(By.ID, "alertbtn").click()
alert =driver.switch_to.alert
alertText= alert.text
print(alertText)
alert.accept()
driver.close()