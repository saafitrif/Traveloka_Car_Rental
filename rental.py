import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from script import element


class E2ECarRental(unittest.TestCase):
    
    def setUp(self): 
        ChromeDriverManager().install()
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        self.browser = webdriver.Chrome(options=options)
        

    # Test Case E2E Car Rental)
    def test_end_to_end_car_rental_menu(self):
        # steps
        browser = self.browser #open web browser
        browser.get("https://www.traveloka.com") #open traveloka web
        time.sleep(1)
        browser.find_element(By.XPATH, element.car_rental_menu).click() # click Car Rental 
        time.sleep(1)
        browser.find_element(By.XPATH, element.Without_Driver_Button).click() # click Without Driver Button
        time.sleep(1)
        browser.find_element(By.XPATH, element.Pick_up_Location).send_keys("Jakarta") # Select Pick-up Location 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "div[aria-label='Jakarta']").click() # click Pick-up Location 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[data-testid="rental-search-form-date-input-start"]').click() # click field of Pick-up Date
        time.sleep(1) 
        browser.find_element(By.CSS_SELECTOR, element.Pick_up_Date).click() # Select Pick-up Date 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[data-testid="rental-search-form-time-input-start"]').click() # click field of Pick-up Time
        time.sleep(1) 
        browser.find_element(By.XPATH,element.Pick_up_Time).click() # Select Pick-up time
        time.sleep(1)
        browser.find_element(By.XPATH,element.Done_button ).click() # Click Done button
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[data-testid="rental-search-form-date-input-end"]').click() #click field of Drop-off Date
        time.sleep(1) 
        browser.find_element(By.CSS_SELECTOR, element.Drop_off_Date).click() # Select Drop-off Date 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[data-testid="rental-search-form-time-input-end"]').click() # click Drop-off Date
        time.sleep(1) 
        browser.find_element(By.XPATH, element.field_of_Drop_off_time).click() # Select field of Drop-off time
        time.sleep(1)
        browser.find_element(By.XPATH,element.Drop_off_time ).click() # Select Drop-off time
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'div[data-testid="rental-search-form-cta"]').click() # Select Done button
        time.sleep(5) 
        # search
        browser.find_element(By.XPATH,element.Search_Button).click() 
        # Car
        time.sleep(2) 
        browser.find_element(By.XPATH,element.Car).click()
        # provider
        time.sleep(2) 
        browser.find_element(By.XPATH, element.Car_Provider).click() 
        time.sleep(2) 
        browser.find_element(By.XPATH, element.Continue_Button).click()
        time.sleep(2) 
        browser.find_element(By.XPATH, element.Rental_Pick_Up_Location).click()
        time.sleep(2) 
        browser.find_element(By.XPATH, element.Rental_Drop_Off_Location).click()
        browser.find_element(By.XPATH, element.field_Drop_off_Location).send_keys("Jakarta")
        time.sleep(5)
        browser.find_element(By.XPATH, element.Drop_off_Location_in_other_location).click() # click Drop-off Location in other location
        time.sleep(2) 
        browser.find_element(By.XPATH,element.Drop_off_notes).send_keys("Teks") # click Drop-off notes
        time.sleep(2) 
        browser.find_element(By.XPATH, element.Book_Now_Button).click() # click button Continue Book Now
        time.sleep(5) 
     
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()