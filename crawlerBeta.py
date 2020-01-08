#FirstVersion - Modifications needed!!!!#
#save to JSON instead of CSV (utf-8), add image#
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd
import json

webdriver = './chromedriver'
driver = Chrome(webdriver)
url = 'https://g1.globo.com/'
driver.get(url)
timeout = 12
items = driver.find_elements_by_class_name('feed-post')
total = []
count = 0
news = []

for item in items:
    if count == 3:
        break        
    quote_text = item.find_element_by_class_name('feed-post-body').text
    link = item.find_element_by_class_name('feed-post-link').text
    new = ((quote_text,link))
    total.append(new)
    df = pd.DataFrame(total,columns=['quote_text','link'])
    count = count+1
    df.to_csv('feed.csv')
    
    news.append({
        'postLink' : link,
        'postBody' : quote_text
        })
   
driver.close()

with open('data.txt', 'w') as outfile:
    json.dump(news, outfile)
