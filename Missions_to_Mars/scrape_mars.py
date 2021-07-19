from splinter import Browser, browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_info():
    # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)
    browser = Browser('chrome')

    # Scrape news title and paragraph into the page
    url = 'https://redplanetscience.com/'

    browser.visit(url)    

    time.sleep(1)

    html = browser.html

    soup = bs(html, "html.parser")

    news_title = soup.find('div', class_='content_title').text
    
    news_p = soup.find('div', class_='article_teaser_body').text

    

#     browser.quit()

#     return mars_data

#     # Scrape mars featured image from the website below
# def scrape_featured_img():

#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://spaceimages-mars.com/'

    browser.visit(url)

    html = browser.html

    soup = bs(html, "html.parser")

    img_source_link = soup.find('img', class_='headerimage fade-in')['src'].strip()

    featured_img_url = url+img_source_link

#     browser.quit()

#     return featured_img_url

# def scrape_facts():

#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

    # url = 'https://galaxyfacts-mars.com'

    # browser.visit(url)

    # html = browser.html

    # soup = bs(html, "html.parser")

    tables = pd.read_html('https://galaxyfacts-mars.com')

    facts_table = tables[1]

    facts_table.columns = ['Description', 'Value']

    facts_table.reset_index(drop=True, inplace=True)

    facts_table = facts_table.to_html(classes="table table-striped")

#     browser.quit()

#     return facts_table

# def scrape_hemispheres_data():

#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://marshemispheres.com/'

    browser.visit(url)

    html = browser.html

    soup = bs(html, "html.parser")

    hemispheres = soup.find_all('div', class_='item')

    hs_data = [] 

    count = 0

    for hemisphere in hemispheres:

        title = hemisphere.find('h3').text

        browser.find_by_css('a.itemLink img')[count].click()
    
        soup = bs(browser.html, 'html.parser')

        wide_img = soup.find('img', class_='wide-image')['src']
    
        wide_img_url = url+wide_img

        hs_data.append({'title': title, 'img_url':wide_img_url})

        count = count + 1

        browser.back()

    hs_data

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img": featured_img_url,
        "facts_table": facts_table, 
        "hs_data_1": hs_data[0]['img_url'],
        "hs_data_2": hs_data[1]['img_url'],
        "hs_data_3": hs_data[2]['img_url'],
        "hs_data_4": hs_data[3]['img_url'],
        "hs_data_1_t": hs_data[0]['title'],
        "hs_data_2_t": hs_data[1]['title'],
        "hs_data_3_t": hs_data[2]['title'],
        "hs_data_4_t": hs_data[3]['title']
    }

    browser.quit()
    
    # return hs_data

    return mars_data








    # Return results
    
