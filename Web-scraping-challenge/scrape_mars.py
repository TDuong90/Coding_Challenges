import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    data = {}
    output = marsNews()
    data['mars_news'] = output[0]
    data['mars_paragraph'] = output[1]
    data['mars_image'] = marsImage()
    data['mars_weather'] = marsWeather()
    data['mars_facts'] = marsFacts()
    data['mars_hemisphere'] = marsHemisphere()

    return data


def marsNews():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text
    news_para = article.find("div", class_="article_teaser_body").text
    output = [news_title, news_para]
    return output


def marsImage():
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    main_url = "https://www.jpl.nasa.gov"
    browser.visit(img_url)
    html = browser.html
    soup = bs(html, "html.parser")
    img_source = soup.find("div", class_="carousel_items")
    img = img_source.article['style']
    img_url_string = list(img.split("url('"))[1][0:-3]
    featured_image_url = main_url + img_url_string
    return featured_image_url


def marsFacts():
    import pandas as pd
    Mars_fact_url = "https://space-facts.com/mars/"
    browser.visit(Mars_fact_url)
    html = browser.html
    soup = bs(html, "html.parser")
    mars_data = pd.read_html(Mars_fact_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_data.columns = ["Description", "Value"]
    mars_data = mars_data.set_index("Description")
    mars_facts = mars_data.to_html(header=False, index=False)
    return mars_facts


def marsHem():
    import time
    Mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Mars_hemi_url)
    html = browser.html
    soup = bs(html, "html.parser")

    mars_hemisphere = []

    products = soup.find("div", class_="result-list")
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link
        browser.visit(image_link)
        html = browser.html
        soup = bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})
    return mars_hemisphere
