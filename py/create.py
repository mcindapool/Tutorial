
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH= "../crawldata-shopee/chromedriver.exe"
driver= webdriver.Chrome(PATH)


driver.get("https://shopee.vn/")
time.sleep(5)

search = driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input")
search.send_keys('áo khoác')
search.send_keys(Keys.RETURN)
time.sleep(5)

show_topseller = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div[3]')
show_topseller.click()
time.sleep(5)
#--------------------------Tên sản phẩm
#elems= driver.find_elements(By.XPATH, "//div[@class='FDn--+']")
#for elem in elems:
#    title= elem.text
#    print(title)   
    
#--------------------------Link sản phẩm(!!!!!!)
elems_link= driver.find_elements(By.CLASS_NAME, 'col-xs-2-4.shopee-search-item-result__item')
#print(elems_link)

for elems in elems_link:
    link = elems.find_elements(By.XPATH, "//a[@href]")
    #a= link.__getattribute__("href")
    #print(a)
    #print(link)


#------------------------Tên shop(!!!!!!!)
#elems_shop= driver.find_elements(By.CSS_SELECTOR,'_3LoNDM')
#print(elems_shop)
#for elem in elems_shop:
#    shop= elem.text
#    print(shop)

#------------------------Số người mua
#elems_countbuyers = driver.find_elements(By.XPATH, "//div[@class='r6HknA uEPGHT']")
#for elem in elems_countbuyers:
#    countBuyers= elem.text
#    print(countBuyers)

time.sleep(120)
driver.quit()
