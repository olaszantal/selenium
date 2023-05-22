from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1005,9999")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options)

driver.get("http://varaljasiklos.hu/")
driver.implicitly_wait(10)

contact = driver.find_element(By.CSS_SELECTOR, "li#menu-item-365>a")
print(contact.get_attribute("text"))
print(contact.get_property('href'))

# myLink = driver.find_element(By., 'Kapcsolat')
contact.click()
name = driver.find_element(
    By.CSS_SELECTOR, "strong")
print(name.get_attribute("text"))
driver.quit()
