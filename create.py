
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH= "../exercise/chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.set_window_size(700,800)

driver.get("https://www.google.com/")
search = driver.find_element(By.NAME,"q")
search.send_keys('cuong')
search.send_keys(Keys.RETURN)


time.sleep(60)
driver.quit()
