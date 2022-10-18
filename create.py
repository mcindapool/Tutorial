import time
from selenium import webdriver

driver= webdriver.Edge(executable_path="../exercise/msedgedriver.exe")
driver.set_window_size(700,800)

driver.get("http://adh.bizz.vn")

time.sleep(10)
driver.quit