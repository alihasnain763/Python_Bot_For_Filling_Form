

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Start a Chrome browser service and create a webdriver
# Navigate to the product page
count = 1 
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
while count <= 100:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        try:
            driver.get('https://www.example.com')
        except ConnectionRefusedError:
            print("Could not establish a connection to the website")

        # Wait for the "Buy it now" button to become interactable, then click it
        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'modal__close js-modal-close ') and contains(@class, 'text-link')]"))
            )
            element.click()
        except TimeoutException:
            print("Timed out waiting for 'close' button to be clickable")
        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Buy it now']"))
            )
            element.click()
        except TimeoutException:
            print("Timed out waiting for 'Buy it now' button to be clickable")

        # Wait for the form fields to load, then fill them out
        time.sleep(10)
        try:
            driver.find_element(By.ID, "email").send_keys("example@gmail.com")
            driver.find_element(By.ID, "TextField1").send_keys("example")
            driver.find_element(By.ID, "TextField2").send_keys("abc")
            driver.find_element(By.ID, "TextField3").send_keys("def")
            driver.find_element(By.ID, "TextField4").send_keys("ghi")
            driver.find_element(By.ID, "TextField5").send_keys("fmn")
            driver.find_element(By.ID, "TextField6").send_keys("2345678")
        except NoSuchElementException:
            print("Unable to find one or more form fields")

        # Click the "Continue to shipping" link
        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue to shipping']"))
            )
            element.click()
        except TimeoutException:
            print("Timed out waiting for 'Continue to shipping' button to be clickable")

        # Click the "Continue to shipping" link
        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue to payment']"))
            )
            element.click()
        except TimeoutException:
            print("Timed out waiting for 'Continue to payment' button to be clickable")

        try:
            element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Complete order']"))
            )
            element.click()
        except TimeoutException:
            print("Timed out waiting for 'Continue to payment' button to be clickable")

        # Wait for the shipping page to load
        time.sleep(10)

        # Close the web browser
        # service.stop()
        driver.quit()
        count = count + 1


