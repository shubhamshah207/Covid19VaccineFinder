from selenium import webdriver  
import time    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

def open_chrome():
    delay = 5
    print("sample test case started")  
    driver=webdriver.Chrome(r"D:\CodingRelated\MY_Projects\VaccineFindCode\chromedriver.exe")  
    #driver=webdriver.firefox()  
    #driver=webdriver.ie()  
    #maximize the window size  
    driver.maximize_window()  
    #navigate to the url  
    driver.get("https://selfregistration.cowin.gov.in/")  
    #identify the Google search text box and enter the value  
    driver.find_element_by_id("mat-input-0").send_keys("9737931913")
    driver.find_elements_by_css_selector("#main-content > app-login > ion-content > div > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(1) > ion-grid > form > ion-row > ion-col.col-padding.md.hydrated > div > ion-button")[0].click()
    
    
    while driver.current_url != "https://selfregistration.cowin.gov.in/dashboard":
        print("waiting")
    
    schedule = "#main-content > app-beneficiary-dashboard > ion-content > div > div > ion-grid > ion-row > ion-col > ion-grid.beneficiary-box.md.hydrated > ion-row:nth-child(3) > ion-col > ion-grid > ion-row.dose-data.md.hydrated > ion-col:nth-child(2) > ul > li > a"
    try:
        time.sleep(3)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , schedule))).click()
        # driver.find_element_by_css_selector().click()
        
        while driver.current_url != "https://selfregistration.cowin.gov.in/appointment":
            print("waiting")
        time.sleep(2)
        bydistrict = "#main-content > app-appointment-table > ion-content > div > div > ion-grid > ion-row > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(2) > form > ion-grid > ion-row > ion-col:nth-child(2) > div > label > div"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , bydistrict))).click()
        # driver.find_element_by_css_selector("").click()
        # time.sleep(3)
        state = "#mat-select-0 > div > div.mat-select-arrow-wrapper.ng-tns-c84-4 > div"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , state))).click()
        # driver.find_element_by_css_selector("").click()
        guj = '//*[@id="mat-option-11"]'
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH , guj))).click()
        # driver.find_element_by_css_selector("").click()
        time.sleep(2)
        dist = "#mat-select-2 > div > div.mat-select-arrow-wrapper.ng-tns-c84-6 > div"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , dist))).click()
        gngr = '//*[@id="mat-option-52"]'
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH , gngr))).click()
        search = '#main-content > app-appointment-table > ion-content > div > div > ion-grid > ion-row > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(2) > form > ion-grid > ion-row > ion-col.col-padding.ng-star-inserted.md.hydrated > ion-row > ion-col.ion-text-start.col-space-mobile.md.hydrated > ion-button'
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , search))).click()
        # pyperclip.copy()
        eighteen = '#main-content > app-appointment-table > ion-content > div > div > ion-grid > ion-row > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(2) > form > ion-grid > ion-row > ion-col:nth-child(4) > div > div:nth-child(1) > label'
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR , eighteen))).click()
        while driver.current_url != "xyz":
            print("waiting")
        
    except:
        traceback.print_exc()
