from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    news_title = soup.find('div', id=)

    # Get the min avg temp
    
    news_p = avg_temps.find_all('strong')[0].text


    # Store data in a dictionary
    mars_data = {
        "news_title": ,
        "news_p": 
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
