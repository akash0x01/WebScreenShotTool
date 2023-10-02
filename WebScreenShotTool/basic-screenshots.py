# Basic functional required packages are below
# pip install selenium Pillow requests
# Additionally MartianMono-SemiBold Font File need to be present in same folder of this program to successfully annotate the screenshots.
# This can be downloaded from : https://fonts.google.com/specimen/Martian+Mono
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw, ImageFont
import requests
import sys
import time
import re
import os

def sanitize_filename(filename):
    return re.sub(r'[^\w\d_]', '_', filename)

def take_screenshot(driver, url, sub_url, file_name, folder_name):
    full_url = f"{url}{sub_url}"
    driver.get(full_url)
    
    # Set the zoom level to 110%
    driver.execute_script("document.body.style.zoom='110%'")
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except Exception as e:
        print(f"An error occurred while waiting for the page {full_url} to load: {e}")

    # Get the response code using requests
    response_code = None
    try:
        response = requests.get(full_url)
        response_code = response.status_code
    except Exception as e:
        print(f"Could not get the response code for {full_url}: {e}")

    screenshot_name = os.path.join(folder_name, sanitize_filename(file_name) + '.png')
    driver.save_screenshot(screenshot_name)
    
    screenshot = Image.open(screenshot_name)
    draw = ImageDraw.Draw(screenshot)
    font = ImageFont.truetype("MartianMono-SemiBold.ttf", 12)
    draw.text((10, 10), f"URL: {full_url}", font=font, fill="red")
    if response_code:
        draw.text((10, 30), f"Response Code: {response_code}", font=font, fill="red")
    screenshot.save(screenshot_name, dpi=(1000, 1000))

    print(f"Screenshot saved for {sub_url}")

def main(url):
    # Remove the trailing '/' if it exists
    url = url.rstrip('/')
    
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    
    timestamp = str(int(time.time()))
    folder_name = f"{timestamp}_screenshots"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    locations = [
        '/robots.txt',
        '/security.txt',
        '/secrets.txt',
        '/.git',
        '/.git/',
        '/backup',
        '/backup/',
        '/backups',
        '/backups/'
    ]
    
    for location in locations:
        take_screenshot(driver, url, location, f"screenshot_{location}", folder_name)

    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <website_url>")
    else:
        main(sys.argv[1])