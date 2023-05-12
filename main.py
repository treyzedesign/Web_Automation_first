import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Scraper import Scraper
import time

os.environ['PATH'] += r"C:\Program Files (x86)\selenium_driver"
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.upwork.com/ab/account-security/login')
driver.implicitly_wait(10)
cookiebtn = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
element = driver.find_element(By.ID, "login_username").send_keys("sudoh141@gmail.com" )
loginbtn = driver.find_element(By.ID, "login_password_continue")
loginbtn.click()
wait = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login_control_continue"))
)
# time.sleep(10)
pas = driver.find_element(By.ID, "login_password")
# pas.clear()
pas.send_keys("savyor123")
pasbtn = driver.find_element(By.ID, "login_control_continue")
pasbtn.click()

WebDriverWait(driver,5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "up-modal-close"))
)
closebtn = driver.find_element(By.XPATH, "//button[@class='up-btn-reset up-modal-close']//div[@class='up-icon']//*[name()='svg']//*[name()='polygon' and contains(@fill-rule,'evenodd')]")
closebtn.click()
WebDriverWait(driver,5).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "up-modal-close"))
)
searchbar = driver.find_element(By.XPATH, "//input[@placeholder='Search for job']")
searchbar.send_keys("web scraping")
WebDriverWait(driver, 10)
searchbtn = driver.find_element(By.XPATH, "//button[@class='up-btn up-btn-primary']//div[@class='up-icon']//*[name()='svg']")
searchbtn.click()
WebDriverWait(driver, 5)
expectedUrl = "https://www.upwork.com/nx/jobs/search/?q=webscraping&sort=recency"
ActualUrl = driver.current_url
if expectedUrl != ActualUrl:
    print(driver.page_source)
else:
    print("unsuccessfully")