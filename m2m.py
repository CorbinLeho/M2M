from bs4 import BeautifulSoup
import time 
import pandas as pd

def m_news():

    browser = init_browser()

   

    # Set Up for NASA Mars News
    url_Mars_News = "https://mars.nasa.gov/news/"

    browser.visit(url_Mars_News)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html,'html.parser')