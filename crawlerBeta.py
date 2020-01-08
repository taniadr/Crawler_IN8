#FirstVersion - Modifications needed!!!!#
#- fix runtime error#
#save to JSON, add image and rename tags#
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd

webdriver = "./chromedriver"

driver = Chrome(webdriver)

url = "https://g1.globo.com/"

driver.get(url)

items = driver.find_elements_by_class_name("feed-post")

total = []
count = 0
for item in range(1,items):
    if count == 3:
        break
        
    quotes = driver.find_elements_by_class_name("feed-post")
    for quote in quotes:
        quote_text = quote.find_element_by_class_name('feed-post-link').text[1:-2]
        author = quote.find_element_by_class_name('feed-post-body').text
        new = ((quote_text,author))
        total.append(new)
df = pd.DataFrame(total,columns=['feed-post-link','feed-post-body'])
count = count+1
df.to_csv('feed.csv')
driver.close()
