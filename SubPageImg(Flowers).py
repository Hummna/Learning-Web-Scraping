from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import urllib.request

import time
driver = webdriver.Edge()
driver.get("https://unsplash.com/")
searchInput = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/header/nav/div[2]/form/div/input")
searchInput.send_keys("flowers")
searchBtn=driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/header/nav/div[2]/form/button")
searchBtn.click()
time.sleep(3)
Div = driver.find_element(By.CLASS_NAME,"FqUkp")
divs=Div.find_elements(By.TAG_NAME,"a")
k=1
for x in divs[:3]:
 time.sleep(2)
 txt=x.text
 driver.get(f"https://unsplash.com/s/photos/{x.text}")
 time.sleep(2)
 category = txt
 if not os.path.exists(category):
  os.makedirs(category)
 div_img=driver.find_elements(By.CLASS_NAME,"MorZF")
 for Y in div_img[:3]:
  time.sleep(1)
  img=Y.find_element(By.TAG_NAME,"img")
  url=img.get_attribute("src")
  urllib.request.urlretrieve(url,f"{txt}/img{k}.jpg")
  k+=1
 driver.back()
 time.sleep(1)
