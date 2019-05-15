from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time 

t = time.time()
user = "lescartin@sespec.com.mx"
password = "Sespec2018"
options = FirefoxOptions()
options.add_argument("--headless")

# Logging in into Sespec
driver = webdriver.Firefox(options=options)
driver.get("https://sespec.segupoliza.com/#/pages/signin")
driver.find_element_by_css_selector("input[ng-model='user']").send_keys(user)
driver.find_element_by_css_selector("input[ng-model='password']").send_keys(password)
driver.find_element_by_css_selector("button[type='submit']").click()

# Clicking "Nueva Cotizacion"
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#/quotes/new']"))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "js-last-picked-label"))).click()

WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, "2020"))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, "KIA"))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, "SOUL"))).click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, "SOUL EX 4 CIL MPI AUT 4 ABS CLIMA VIDRIOELEC TELA SM SIN QUEMACOCOS BOLSAAIRE"))).click()

# There are 3 different inputs for the postal code. The one which works for SEGUVIN is the number 2
driver.find_elements_by_css_selector("input[data-ng-model='cp']")[2].send_keys("01430")
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-ng-model='cp']"))).send_keys("01430")
time.sleep(2)
#driver.find_element_by_link_text("Mostrar oferta").click()

WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, "Mostrar oferta"))).click()

WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body .row.mb10:nth-child(2) a[ng-click='printDeals()']"))).click()

#driver.find_elements_by_css_selector("a[ng-click='printDeals()']")[1].click()
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='generate(prospecto)']"))).click()
#driver.find_element_by_css_selector("button[ng-click='generate(prospecto)']").click()


URL_to_PDF = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='guardarDoc']"))).get_attribute("href")
#URL_to_PDF = driver.find_element_by_css_selector("a[class='guardarDoc']").get_attribute("href")
driver.close()
elapsed = time.time() - t
print("URL to PDF: \n" + URL_to_PDF)
print("Elapsed Time:" + str(elapsed))
