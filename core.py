from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import pyttsx3
import keyboard
import json


def zoom():
    path = 'D:\works\zoom auto\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(3600)



    with open('database/data.json') as f:
        data = json.load(f) 


    def presenting(): 
        time.sleep(15)
        mute = driver.find_element_by_xpath('//*[@id="wc-footer"]/div/div[1]/div[1]/button')
        mute.click()
        chat_button = driver.find_element_by_xpath('//*[@id="wc-footer"]/div/div[2]/div[3]/button')
        chat_button.click()
        wait = WebDriverWait(driver, 10)
        chatbox = driver.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[4]/textarea')
        chatbox.send_keys('Present sir!' + Keys.RETURN)
        pyttsx3.speak('Name successfully presented!')
        time.sleep(20)
        pyttsx3.speak('WARNING! LEAVING THE CLASS!')
            

    def joining():
        url = 'https://zoom.us/wc/join/' + data["c1_id"]
        driver.get(url)
        name = driver.find_element_by_xpath('//*[@id="inputname"]')
        name.send_keys(data["my_name"])
        join = driver.find_element_by_xpath('//*[@id="joinBtn"]')
        join.click()
        password = driver.find_element_by_xpath('//*[@id="inputpasscode"]')
        password.send_keys(data["c1_pass"])
        join_button = driver.find_element_by_xpath('//*[@id="joinBtn"]')
        join_button.click()
        presenting()       

    try:
        joining()
    except:
        time.sleep(3)
        print('NOT CLASS TIME YET, WAITING FOR THE RIGHT TIME..')
        zoom()


def quick_join(mid, mpass , uname ):
    path = 'D:\works\zoom auto\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(3600)




    with open('database/data.json') as f:
        data = json.load(f) 


    url = 'https://zoom.us/wc/join/' + mid
    driver.get(url)
    name = driver.find_element_by_xpath('//*[@id="inputname"]')
    name.send_keys(uname)
    join = driver.find_element_by_xpath('//*[@id="joinBtn"]')
    join.click()
    password = driver.find_element_by_xpath('//*[@id="inputpasscode"]')
    password.send_keys(mpass)
    join_button = driver.find_element_by_xpath('//*[@id="joinBtn"]')
    join_button.click()
    mute = driver.find_element_by_xpath('//*[@id="wc-footer"]/div/div[1]/div[1]/button')
    mute.click()
    chat_button = driver.find_element_by_xpath('//*[@id="wc-footer"]/div/div[2]/div[3]/button')
    chat_button.click()
    wait = WebDriverWait(driver, 10)
    chatbox = driver.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[4]/textarea')
    chatbox.send_keys('Present sir!' + Keys.RETURN)
    pyttsx3.speak('Name successfully presented!')
    time.sleep(15)
    pyttsx3.speak('WARNING! LEAVING THE CLASS!')
    

    try:
        quick_join()
    except:
        time.sleep(3)
        print('Class didnt started..')
