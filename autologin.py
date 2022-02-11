import time
from multiprocessing.connection import wait
import os
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By

from getpass import getpass

username = "shiny.s@exeterpremedia.com"
password = 12345
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))

#driver = webdriver.Edge("msedgedriver.exe")
driver.get("https://testing.kriyadocs.com/dashboard")

username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)
driver.find_element_by_xpath(
    "/html/body/div[3]/div/form/div/div[2]/div[5]/div[1]/a").click()
driver.implicitly_wait(10)
button = driver.find_element_by_css_selector(".center, .center-align")

ActionChains(driver).move_to_element(button).click(button).perform()

driver.find_element_by_id("reportView").click()
driver.find_element_by_xpath("//*[@id=\"reportView\"]").click()
print(driver.find_element_by_id('filterCustomer'))
