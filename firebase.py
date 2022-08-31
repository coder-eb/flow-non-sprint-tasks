import os
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv.main import load_dotenv

def initialize_driver():
    driver = uc.Chrome(use_subprocess=True)
    return driver

def create_firebase_project(driver):
    
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class,"new-project-button")]'))).click()
    project_name = driver.find_element(By.ID, 'projectName')
    project_name.send_keys('selenium-demo')

    # These check boxes are not present sometimes. Don't know why :(
    try:
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'mat-checkbox-1'))).click()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'mat-checkbox-2'))).click()
    except TimeoutException:
        pass

    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]'))).click()    

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'mat-mdc-slide-toggle-1-button'))).click()
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()

    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class,"success-container")]/button'))).click()    
    

def login_to_google(driver):
    
    url = "https://console.firebase.google.com/"
    driver.get(url)
    # Enter email address
    email_field = driver.find_element(By.ID , "identifierId")
    email_field.send_keys(os.environ.get('GOOG_EMAIL'))
    driver.find_element(By.ID , "identifierNext").click()
    # Enter password and submit
    password_field = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
    password_field.send_keys(os.environ.get('GOOG_PASSWORD'))
    submit_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
    submit_button.click()

    return driver

def main():
    driver = initialize_driver()
    driver = login_to_google(driver)
    create_firebase_project(driver)    
    sleep(20)

if __name__ == '__main__':
    load_dotenv()
    main()