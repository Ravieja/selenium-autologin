import time
from multiprocessing.connection import wait
import os
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from getpass import getpass

username = "shiny.s@exeterpremedia.com"
password = 12345
PATH = 'E:\seleniumautologin\chromedriver'
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))

# driver = webdriver.Edge("msedgedriver.exe")


def user_login():
    driver.get("https://testing.kriyadocs.com/dashboard")

    username_textbox = driver.find_element_by_id("username")
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id("password")
    password_textbox.send_keys(password)
    login_button = driver.find_element_by_xpath(
        "//*[@id='login-page']/div/form/div/div[2]/div[5]/div[1]/a")
    driver.execute_script("arguments[0].click();", login_button)
    driver.implicitly_wait(10)
# for multi login authentication
    try:
        multilog = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, '/html/body/div[3]/div/form/div/div[3]/div[2]/div/div[1]/span')))
        multilog.click()
    except:
        print()


def user_login2():
    driver.get("https://testing.kriyadocs.com/dashboard")


def select_report():
    customer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div')))
    customer.click()
    i = 1
    p = True

    while i < 46:
        x = i
        custval = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "/html/body/div[1]/main/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div["+"{x}".format(x=i)+"]")))
        custval.click()

        try:

            report = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '/html/body/header/ul[1]/li[3]/a')))
            report.click()
            article = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/h4')))
            article.click()
            export = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/h4/button')))
            export.click()
            user_login2()
            customer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div')))
            customer.click()
            i = i+1
        except:
            user_login2()
            customer = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div')))
            customer.click()
            i = i+1


user_login()
select_report()
