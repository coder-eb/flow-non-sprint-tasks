import os
from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from dotenv.main import load_dotenv

def initialize_driver():
    # chrome_options = Options()
    # chrome_dir = "/home/ebran/.config/google-chrome"
    # profile_name = "Profile 3"
    # chrome_options.add_argument(f"--user-data-dir={chrome_dir}")
    # chrome_options.add_argument(f"--profile-directory={profile_name}")

    # return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver = uc.Chrome(use_subprocess=True)
    return driver

def main():
    driver = initialize_driver()
    url = "https://console.firebase.google.com/"
    driver.get(url)
    email_field = driver.find_element(By.ID , "identifierId")
    email_field.send_keys(os.environ.get('GOOG_EMAIL'))
    driver.find_element(By.ID , "identifierNext").click()
    sleep(2)
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_field.send_keys(os.environ.get('GOOG_PASSWORD'))

    submit_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
    submit_button.click()

    sleep(12)
    create_project = driver.find_element(By.XPATH, '//*[contains(@class,"create-project")]/button[1]')
    create_project.click()
    
    sleep(10)

def main1():
    from selenium import webdriver
    import geckodriver_autoinstaller
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    geckodriver_autoinstaller.install()

    profile = webdriver.FirefoxProfile(
        '/home/ebran/.mozilla/firefox/1e8nzb5j.default-release')

    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX

    driver = webdriver.Firefox(firefox_profile=profile,
                            desired_capabilities=desired)
    # driver = webdriver.Firefox(desired_capabilities=desired)
    url = "https://console.firebase.google.com/"
    driver.get(url)
    email_field = driver.find_element(By.ID , "identifierId")
    email_field.send_keys(os.environ.get('GOOG_EMAIL'))
    driver.find_element(By.ID , "identifierNext").click()
    sleep(2)
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    password_field.send_keys(os.environ.get('GOOG_PASSWORD'))

    submit_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
    submit_button.click()

    sleep(12)

if __name__ == '__main__':
    load_dotenv()
    main()