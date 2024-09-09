
import streamlit as st
import requests as rq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
import matplotlib
import matplotlib.pyplot as plt
def webScrapingReviews(url):
    reviews = []
    link = []
    
    
    r1 = rq.get(url)
    sleep(2)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    
    f_url = ''
    for i in soup1.findAll('a', attrs={'href': re.compile("/product-review")}):
        q = i.get('href')
        link.append(q)
        for j in link:
            if 'LSTMOBF3HZ2H9YZSYRYTFKW51' in j:
                aa = i
        f_url = 'https://www.flipkart.com' + str(j)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f_url)
    
    i = 1
    while i < 3:
        ss = driver.get(f_url + "&page=" + str(i))
        qq = driver.current_url
        r2 = rq.get(qq)
        soup = BeautifulSoup(r2.text, 'html.parser')
        reviews_container = soup.find('div', {'class': '_1YokD2 _3Mn1Gg col-9-12'})
        if reviews_container:
            reviews_divs = reviews_container.find_all('div', {'class': 't-ZTKy'})
            for child in reviews_divs:
                third_div = child.div.div
                text = third_div.text.strip()
                cleaned_text = clean_text(text)
                reviews.append(cleaned_text)
        else:
            print(f"No reviews container found on page {i}")
        sleep(1)
        i += 1
    
    driver.quit()  # Close the browser
    file_path='reviews1.xlsx'
    data = pd.DataFrame({'review': reviews})
    data.to_excel(file_path, index=False)
    return data

def main():
    print("Calling print_hello() function:")
    webScrapingReviews("https://www.flipkart.com/eureka-forbes-bold-wet-dry-vacuum-cleaner/p/itm5a1c0501fa6e0?pid=VCLFHW6AYCE6GRST&lid=LSTVCLFHW6AYCE6GRSTHROKPE&marketplace=FLIPKART&store=j9e%2Fabm%2Ful2&srno=b_1_1&otracker=browse&fm=organic&iid=en_g1W-X2d22as92EvbfdPft8Kkfm9vhxsGx0mi4P5WzNva6SMSIHMObZYP-W0oXJF6xsknhEKhASMD6v_cUm2TcQ%3D%3D&ppt=None&ppn=None&ssid=n0kpyge61s0000001689450624994")

if __name__ == "__main__":
    main()
