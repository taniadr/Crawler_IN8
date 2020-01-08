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
timeout = 12
items = driver.find_elements_by_class_name("feed-post")
total = []
count = 0

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

driver.close()
