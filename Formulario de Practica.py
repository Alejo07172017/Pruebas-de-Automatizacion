from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chromeOpciones = Options()
chromeOpciones.add_argument("--start-maximized")
chromeOpciones.add_argument("--incognito")
chromeOpciones.add_experimental_option('excludeSwitches', ['enable-logging'])
chromeOpciones.add_argument("--log-level=3")
chromeOpciones.add_argument("--disable-gpu")
chromeOpciones.add_argument("--disable-software-rasterizer")
chromeOpciones.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chromeOpciones)

# Función para scroll y click
def scroll_and_click(element):
    """Scroll al elemento y hacer click usando JS para evitar superposición"""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", element)

# Remover anuncios
driver.execute_script("""
   var ads = document.querySelectorAll('iframe[id^="google_ads"]');
   ads.forEach(a => a.remove());
""")

driver.get("https://demoqa.com/")

# Forms
forms = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h5[text()='Forms']")))

scroll_and_click(forms)

# Remover anuncios
driver.execute_script("""
   var ads = document.querySelectorAll('iframe[id^="google_ads"]');
   ads.forEach(a => a.remove());
""")

# Practice Form
practice_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@id='item-0']//span[text()='Practice Form']")))

scroll_and_click(practice_form)

# First Name
first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
first_name.send_keys("Alejandro")

# Last Name
last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lastName")))
last_name.send_keys("Ocampo")

# Email
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userEmail")))
email.send_keys("alejo2@gmail.com")

# Género Male
male_label = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']")))

scroll_and_click(male_label)

# Number
number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userNumber")))
number.send_keys("3135948358")

# Fecha de nacimiento
calendar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))

scroll_and_click(calendar)

year = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
Select(year).select_by_visible_text("2000")

month = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
Select(month).select_by_visible_text("July")

day = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='17']")))
scroll_and_click(day)

# Subjects
subjects = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
subjects.send_keys("English")
time.sleep(1)
first_option1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".subjects-auto-complete__menu-list div")))

scroll_and_click(first_option1)

# Hobbies - Sports
sports = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")))

scroll_and_click(sports)

# Dirección
address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "currentAddress")))
address.send_keys("Calle 1 Cra 1")

# State - NCR
state = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state.send_keys("NCR")
time.sleep(1)
first_option2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-3-option-0")))

scroll_and_click(first_option2)

# City - Noida
city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
city.send_keys("Noida")
time.sleep(1)
city.send_keys(Keys.ENTER)

# Botón Submit
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))

scroll_and_click(submit)

time.sleep(3)

# Botón Close
close = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "closeLargeModal")))

scroll_and_click(close)

time.sleep(3)

driver.quit()
