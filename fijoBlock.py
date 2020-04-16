#!/usr/bin/env python
import time
import sys
import datetime
import atexit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Exit handler: ensure driver and display are closed
def exit_handler():
    print('Entered in exit handler')
    print('Quitting driver...')
    try:
        driver.quit()
    except:
        print("Couldn't quit driver")
    if not debug:
        print('Stopping display...')
        try:
            display.stop()
        except:
             print("Couldn't stop display")
    print('Bye')
    print("")
    print("")

atexit.register(exit_handler)

#Program Start

print("===================================================")
print(datetime.datetime.now())
print("===================================================")


#Import config variables from config.py
from config import *

#Load block/unblock argument from command
blockOrder = sys.argv[1]

#Load web driver
print( 'Loading driver...')
if debug:
    from selenium.webdriver.chrome.options import Options
    options = Options()
    if headlessDebug:
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    print( 'Driver loaded')
else:
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1600, 1200))
    display.start()
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    print( 'Driver loaded')





#Start Operations
print('Performing GET...')
driver.get("http://192.168.1.1/login.html")

#Wait for "iniciar sesion" button to appear
WebDriverWait(driver, elementTimeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/input')))
print('Submiting login credentials...')
driver.find_element_by_xpath('//*[@id="activation-content-right"]/div[2]/div/input').send_keys(user)
driver.find_element_by_xpath('//*[@id="activation-content-right"]/div[3]/div[1]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/input').click()

#Wait for Mode Select appear
modeSelect_xpath =  '/html/body/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/a'
WebDriverWait(driver, elementTimeout).until(EC.presence_of_element_located((By.XPATH, modeSelect_xpath)))
print("wait lang done")

#Click on Mode Select
driver.find_element_by_xpath(modeSelect_xpath).click()

#Click on Expert mode
expertMode_xpath = '/html/body/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div/ul/li[2]'
driver.find_element_by_xpath(expertMode_xpath).click()

#Wait for Home page image load
WebDriverWait(driver, elementTimeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[6]/div[3]/div/div[2]/div[1]/div[1]')))

#Get to "No Molestar" section
driver.get("http://192.168.1.1/phone.html#sub=16")

#Wait for "schedule-table" tab
WebDriverWait(driver, elementTimeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="schedule-table"]')))

#Check current block status
print('Acquiring current status...')
selectText = driver.find_element_by_xpath('/html/body/div/div/div[6]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/a/span').get_attribute("innerText")
print("Var selectText is: "+selectText)

if selectText == "Activado":
    blockStatus = "block"
else:
    blockStatus = "unblock"


print("=========================")
print("Status is: "+blockStatus)
print("Order is: "+blockOrder) 
print("=========================")


#Perform action if proceds

if (blockOrder != blockStatus):
    print('Clicking on multioption...')
    driver.find_element_by_xpath('/html/body/div/div/div[6]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/a/span').click()
    # Wait for select being expanded
    WebDriverWait(driver, elementTimeout).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[6]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/ul/li[1]')))

    if blockOrder == "block":
        print('Clicking on activate block...')
        driver.find_element_by_xpath('/html/body/div/div/div[6]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/ul/li[1]').click()
    else:
        print('Clicking on deactivate block...')
        driver.find_element_by_xpath('/html/body/div/div/div[6]/div[3]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/div/ul/li[2]').click()
    

    print('Applying new settings...')
    driver.find_element_by_xpath('//*[@id="applyButton"]').click()
    #Wait for "Changes saved"
    WebDriverWait(driver, elementTimeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lang700176"]')))

else:
    print("Nothing to do...")


print("=========================")
print("Final status is: "+blockOrder)
print("=========================")
#Exit handler runs here