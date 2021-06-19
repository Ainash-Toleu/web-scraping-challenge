from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# def title():
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

#     nasa_url = 'https://redplanetscience.com/'
#     browser.visit(nasa_url)

#     html = browser.html
#     soup = BeautifulSoup(html, "lxml")

#     title = soup.find('div', class_='content_title').get_text()

#     browser.quit()

#     return title

# def text():
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

#     nasa_url = 'https://redplanetscience.com/'
#     browser.visit(nasa_url)
#     html = browser.html
#     soup = BeautifulSoup(html, "lxml")

#     text = soup.find('div', class_='article_teaser_body').get_text()

#     browser.quit()

#     return text

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

    mars_html = df.to_html(index = False, classes='table table-striped table-md')
    
    return mars_html
    

def images():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    astrogeology_url = 'https://marshemispheres.com/'
    browser.visit(astrogeology_url)

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    hrefs = []
    all_a = soup.select('.description a')

    for a in all_a:
        hrefs.append(a['href'])

    hemisphere_image_urls = []

    for href in hrefs:
        images_url = astrogeology_url + href
        browser.visit(images_url)
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')
        image = soup.find("img", class_="wide-image")['src']
        title = soup.find("h2", class_="title").text
        hemisphere_image_urls.append({"title": title, "img_url": astrogeology_url + image})
    browser.quit()
    
    return hemisphere_image_urls 


  






def scrape():
    mars = {}
    # mars["title"] = title()
    # mars["text"] = text()
    mars['image'] = image()
    mars['table'] = table()
    mars['hemisphere_image_urls'] = images()

    return mars


    