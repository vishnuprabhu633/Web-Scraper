# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

# Connect to Website and pull in data

URL = 'https://www.amazon.com/PlayStation-Digital-Marvels-Spider-Man-Bundle-5/dp/B0CV4J3TS7/ref=sr_1_3?crid=1NBHDWSVWT6MQ&dib=eyJ2IjoiMSJ9.yso0-d9KMYdlvQKR3IMB8RKq_19EELLrkTclSLzly8dsfu9fngIHutXXiAshcEF4n6zgg78hAsUy1WpSN3f7MAXn16DKJnuxKkcZC_5U2HOztlDiQlgnQ4wXGE82GSWgiKm1b_vbiLfhGrJZWYM-tXGrH1DM-pstiMUstL99BIhbaTMmY_koan5uoX--mx1DLqJS6x1Ad4CGSN0RHsF680UQsVF4mDj8sy4FLmck1Pc.yHRkY49_5c0eRn4VuQbR8fxyJ3PBk8rvvKnr9-EMVXQ&dib_tag=se&keywords=ps5&qid=1710665417&sprefix=ps+5%2Caps%2C653&sr=8-3'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='priceblock_ourprice').get_text()


print(title)
print(price)