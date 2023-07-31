from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import os
import traceback

import socket
socket.setdefaulttimeout(15)

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("paris")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 스크롤을 아래로 내린다
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 스크롤 될 때 로딩 대기
    time.sleep(SCROLL_PAUSE_TIME)
    # 스크롤이 마지막까지 오게되면 while문을 탈출
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".LZ4I").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(1)
        try:
            element = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
            imgUrl = element.get_attribute("src")
        except:
            print('안먹힘안먹힘안먹힘안먹힘')
            pass   
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        file_path = f"이유진의 부탁4/{count}.jpg"
        retry = 1
        while(retry < 3):
            try:
                urllib.request.urlretrieve(imgUrl, file_path)
                count = count + 1
                break
            except Exception as e:
                print('retry #', retry)
                retry += 1
                print(e)
                continue
    except:
        pass

driver.close()
