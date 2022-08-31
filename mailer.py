from time import sleep
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv.main import load_dotenv
from helpers import login_to_google

def initialize_driver():
    driver = uc.Chrome(use_subprocess=True)
    return driver

def main():
    # email = input("Enter the email address to which you would like to receive the automated email\n")
    email = 'lazyprogrammer@gmail.com'
    driver = initialize_driver()
    driver = login_to_google(driver)

    driver.get("https://www.gmail.com")
    sleep(4)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Compose']"))).click()
    sleep(3)
    to_address = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id,"to")]')))
    to_address.send_keys(email)
    # sleep(10)
    subject = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@name,"subjectbox")]')))
    subject.send_keys('wassup')
    
    sleep(5)
    body = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, ':qz')))
    body.send_keys('lol')
   
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Send']"))).click()
    sleep(2)
    mail_status = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "bAq")))
    status = mail_status.get_text()
    print(status)
    
    sleep(60)

def generate_random_email():
    import requests
    url = "https://api.quotable.io/random"
    body = requests.get(url).json()
    quote = body['content']
    author = body['author']
    print(f"{quote}\n -{author}")

if __name__ == '__main__':
    main()
