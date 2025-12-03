from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chromeOpciones = Options()
chromeOpciones.add_argument("--incognito")
chromeOpciones.add_argument("--log-level=3")
chromeOpciones.add_argument("--disable-gpu")
chromeOpciones.add_argument("--start-maximized")
chromeOpciones.add_argument("--disable-notifications")
chromeOpciones.add_argument("--disable-software-rasterizer")
chromeOpciones.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chromeOpciones)

driver.get("https://qa-practice.netlify.app/bugs-form")

time.sleep(1)

#First Name
first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
first_name.send_keys("Alejandro")

time.sleep(1)

#Last Name
last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lastName")))
last_name.send_keys("Ocampo")

time.sleep(1)

#Phone
phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phone")))
phone.send_keys("3135948358")

time.sleep(1)

#Country
country = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "countries_dropdown_menu")))
Select(country).select_by_visible_text("Colombia")

time.sleep(1)

#Email
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "emailAddress")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email)
time.sleep(1)
email.send_keys("alejoben200@gmail.com")

time.sleep(1)

#Password
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("Alejo123456*")

time.sleep(1)

#Register
register = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "registerBtn")))
register.click()

time.sleep(1)

#Result
result = driver.find_element(By.ID, "results-section")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", result)

time.sleep(3)
driver.quit()