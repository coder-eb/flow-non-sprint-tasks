import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_google(driver):
    url = "https://accounts.google.com/"
    driver.get(url)
    email_field = driver.find_element(By.ID , "identifierId")
    email_field.send_keys(os.environ.get('GOOG_EMAIL'))
    driver.find_element(By.ID , "identifierNext").click()
    # Enter password and submit
    password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
    password_field.send_keys(os.environ.get('GOOG_PASSWORD'))
    submit_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
    submit_button.click()
    WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@role="search"]')))
    
    return driver

    