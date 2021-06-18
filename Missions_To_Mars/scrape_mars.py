from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def title():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    nasa_url = 'https://redplanetscience.com/'
    browser.visit(nasa_url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")

    title = soup.find('div', class_= 'content_title').get_text()

    browser.quit()

    return title

def text():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    nasa_url = 'https://redplanetscience.com/'
    browser.visit(nasa_url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")

    text = soup.find('div', class_= 'article_teaser_body').get_text()

    browser.quit()

    return text

def scrape():
    mars = {}
    mars["title"] = title()
    mars["text"] = text()

    return mars
    