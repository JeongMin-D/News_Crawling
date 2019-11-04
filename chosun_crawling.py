from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import re
import csv
import time

# [create csv file, open]
f = open('chosun.csv', 'w', encoding='utf-8_sig',  newline='')
csv_writer = csv.writer(f)

# [Chrome driver set]
path="C:\\Users\\J25ng\\Documents\\Project\\driver\\chromedriver"
driver = webdriver.Chrome(path)


# [brower_on]
# 101
for i in range(1,2):
    driver.get("http://nsearch.chosun.com/search/total.search?query=%EC%88%98%EC%82%AC%EA%B5%AC%EC%A1%B0%EA%B0%9C%ED%98%81&sort=1&pn="+str(i))

    time.sleep(0.5)

    for num in range(1,3):
        b = '//*[@id="Wrap"]/div[2]/div/div[1]/div[1]/dl[' + str(num) + ']/dt/a'
        driver.find_element_by_xpath(b).click()
        time.sleep(0.5)

        driver.switch_to.window(driver.window_handles[-1])
        #time.sleep(10)

        cur = driver.current_url
        req = requests.get(cur)
        html = req.text
        soup = BeautifulSoup(req.content.decode('utf-8', 'replace'))

        title = soup.find('h1',{'id':'news_title_text_id'}).get_text()
        date = soup.find('div',{'class':'news_date'}).get_text()
        content = soup.find_all('div',{'class':'par'})
        con = []
        for i in content:
            qq = i.get_text()
            con.append(qq)

        csv_writer.writerow([date, title, con])

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

f.close()