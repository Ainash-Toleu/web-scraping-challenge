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
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find('div', class_='content_title').get_text()

    browser.quit()

    return title

def text():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    nasa_url = 'https://redplanetscience.com/'
    browser.visit(nasa_url)
    html = browser.html
    soup = BeautifulSoup(html, "lxml")

    text = soup.find('div', class_='article_teaser_body').get_text()

    browser.quit()

    return text

def image():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)   

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')  

    image = soup.find("img", class_="headerimage fade-in")["src"]
    featured_image_url = image_url + image

    browser.quit()

    return featured_image_url

def table():
    table_url = 'https://galaxyfacts-mars.com/'

    tables = pd.read_html(table_url)

    df = tables[0]
    df.columns = ['Description', 'Mars', 'Earth']   

    mars_html = df.to_html(index = False)
    
    return mars_html




def scrape():
    mars = {}
    mars["title"] = title()
    mars["text"] = text()
    mars['image'] = image()
    mars['table'] = table()

    return mars
    