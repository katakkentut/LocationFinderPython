from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def getLocation():
    options = Options()
    options.add_argument("user-agent=fake-useragent'")

    options.add_argument("window-position=-2000,0")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    timeout = 20
    ser = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=options)

    driver.get("https://my-location.org/")

    WebDriverWait(driver, timeout)
    time.sleep(3)

    longitude = driver.find_elements(by=By.XPATH, value='//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])

    latitude = driver.find_elements(by=By.XPATH, value='//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])

    address = driver.find_elements(by=By.XPATH, value='//*[@id="address"]')
    address = [x.text for x in address]
    address = str(address[0])
    driver.quit()
    return latitude, longitude, address


if __name__ == '__main__':

    result = getLocation()

    print(f"""
      Latitude  : {result[0]}
    
      Longitude : {result[1]}
    
      Address   : {result[2]}
    """)
