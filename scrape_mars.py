import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

def mars_news():
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news'

    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        news = soup.find('div',class_="content_title")
        news_title = news.find('a').text.strip()
        par = soup.find('div', class_="rollover_description_inner")
        news_par = par.text.strip()

    except AttributeError:
        return None, None

    return news_title, news_par
    news_title, news_par = mars_news()


def featured_image():
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    response2 = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    feat = soup2.find('section',class_="centered_text clearfix main_feature primary_media_feature single")
    feature_image =  feat.a['data-fancybox-href']
    image_url = "https://www.jpl.nasa.gov/" + feature_image
    img = image_url.get("src") 
    return image_url
    
     


def weather():
     # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response3 = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup3 = BeautifulSoup(response3.text, 'html.parser')

    mars_weather = soup3.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    return mars_weather


def facts():
    df_Mars_Facts = pd.read_html("https://space-facts.com/mars/")

    df_Mars_Facts = df_Mars_Facts[0]

    df_Mars_Facts.rename({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    df_Mars_Facts = df_Mars_Facts

    df_Mars_Facts_table = df_Mars_Facts.to_html("df_Mars_Facts_Table.html",index=False)

    return df_Mars_Facts_table  

def scrape():
    all_data = {
        "news_title": news_title,
        "news_paragraph": news_par,
        "featured_image": featured_image(),
        "weather": weather(),
        "facts": facts(),
    }
    return all_data
