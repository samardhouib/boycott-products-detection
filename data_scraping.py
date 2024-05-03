from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import wget
from datetime import date
import os
import time
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome()
driver.maximize_window()
link = "https://www.google.com/search?q=boga+plastic+bottle&sca_esv=5fee7d56a3546583&udm=2&biw=681&bih=639&sxsrf=ACQVn08CL_27kb3qz4p00hKzmJTDvWFVIA%3A1708806544705&ei=kFHaZd_TKpCei-gPpri0qAo&ved=0ahUKEwjf29i46MSEAxUQzwIHHSYcDaUQ4dUDCBA&uact=5&oq=boga+plastic+bottle&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2JvZ2EgcGxhc3RpYyBib3R0bGUyBBAjGCdIwR5QhhZYwRdwA3gAkAEAmAGlAaABoQKqAQMwLjK4AQPIAQD4AQL4AQGYAgGgAoQBmAMA4gMFEgExIECIBgGSBwMwLjE&sclient=gws-wiz-serp"

driver.get(f"{link}")
sleep(6)
src = driver.page_source
soup = BeautifulSoup(src,features="lxml")
items = soup.find_all("div", class_= "H8Rx8c")
items2 = soup.find_all("div",class_ = "fR600b islir")
i=0
for item in items :
    image = item.find("img")
    source = image.get("src")

    try:
        i+=1
        wget.download(
            source,
            out=f"boga/bogap{i}.png")
    except Exception as e:
        print(e)
        pass

for item in items2:
    image = item.find("img")
    source = image.get("src")
    print(source)
    try:
        i+=1
        wget.download(
            source,
            out=f"boga/bogap{i}.png")
    except Exception as e:

        pass
