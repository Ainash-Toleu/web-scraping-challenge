from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news = {}

    nasa_url = 'https://redplanetscience.com/'
    browser.visit(nasa_url)

    html = browser.html
    soup = BeautifulSoup(html, "lxml")

    news["title"] = soup.find('div', class_= 'content_title').text
    news["text"] = soup.find('div', class_= 'article_teaser_body').text

    # Quit the browser
    browser.quit()

    return news
