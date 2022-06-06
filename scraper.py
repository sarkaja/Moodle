import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://moodle.vse.cz/")
login = driver.find_element_by_xpath('//*[@id="banner"]/nav/div[2]/div[2]/div/span/a')
login.click()
login2 = driver.find_element_by_xpath('//*[@id="region-main"]/div[2]/div[2]/div/div/div/div/div/a')
login2.click()
mail = driver.find_element_by_xpath('//*[@id="i0116"]')
mail.send_keys('jads00@vse.cz')  
mail.send_keys(Keys.RETURN) 
time.sleep(5)
password = driver.find_element_by_xpath('//*[@id="passwordInput"]')
password.send_keys('')
password.send_keys(Keys.RETURN) 
time.sleep(5)
kurz = driver.find_element_by_xpath('//*[@id="label_3_5"]/span')
kurz.click()
time.sleep(3)
znamky = driver.find_element_by_xpath('//*[@id="label_4_12"]/span')
znamky.click()
time.sleep(3)
export = driver.find_element_by_link_text('Export')
export.click()
time.sleep(3)
excel = driver.find_element_by_partial_link_text('Excel')
excel.click()
time.sleep(3)
download = driver.find_element_by_xpath('//*[@id="id_submitbutton"]')
download.click()
time.sleep(5)
driver.close()

