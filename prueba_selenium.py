from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os

def send_whatsapp_video(contact_name, video_path):
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=/Users/sebastianarana/Library/Application Support/Google/Chrome/Default") 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")
    
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="3"]'))
    )
    search_box.send_keys(contact_name)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'//span[contains(text(),"{contact_name}")]'))
    ).send_keys(Keys.ENTER)

    attachment_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[title="Adjuntar"]'))
    )
    attachment_button.click()

    gallery_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
    )
    gallery_option.send_keys(video_path)

    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-icon="send"]'))
    )
    send_button.click()

    sleep(1) 
    driver.quit()

contact_name = "Sebs"  
video_path = os.path.abspath("borrar2.mp4")  

send_whatsapp_video(contact_name, video_path)
