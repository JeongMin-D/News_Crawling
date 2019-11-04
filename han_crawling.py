from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import re
import csv
import time

# [create csv file, open]
f = open('han.csv', 'w', encoding='utf-8_sig',  newline='')
csv_writer = csv.writer(f)

# [Chrome driver set]
path="C:\\Users\\J25ng\\Documents\\Project\\driver\\chromedriver"
driver = webdriver.Chrome(path)


# [brower_on]
for i in range(1):
    driver.get("http://search.hani.co.kr/Search?command=query&keyword=%EC%88%98%EC%82%AC%EA%B5%AC%EC%A1%B0%EA%B0%9C%ED%98%81&media=news&submedia=&sort=d&period=all&datefrom=2000.01.01&dateto=2019.10.31&pageseq="+str(i))

    time.sleep(0.5)

    for num in range(1,11):
        b = '//*[@id="contents"]/div[3]/ul/li['+str(num)+']/dl/dt/a'
        driver.find_element_by_xpath(b).click()

        date = driver.find_element_by_xpath('//*[@id="article_view_headline"]/p[2]/span[1]')
        title = driver.find_element_by_xpath('//*[@id="article_view_headline"]/h4/span')
        content = driver.find_element_by_xpath('//*[@id="a-left-scroll-in"]/div[2]/div/div[2]')

        write_date = date.text
        write_title = title.text
        write_content = content.text

        csv_writer.writerow([write_date, write_title, write_content])

        driver.back()

f.close()