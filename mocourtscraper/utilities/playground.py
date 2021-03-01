from bs4 import BeautifulSoup
import pandas as pd
import json
from mocourtscraper.creds import SCRAPER_API_KEY
from scraper_api import ScraperAPIClient
import re

CLIENT = ScraperAPIClient(SCRAPER_API_KEY)


def _replace_breaks(text):
    text = text.replace('\n','')
    text = text.replace('\t','')
    text = text.replace('\r','')
    return text

""" url = 'https://www.courts.mo.gov/casenet/cases/charges.do?inputVO.caseNumber=21CR-CR00033&inputVO.courtId=CT08'
req = CLIENT.get(url=url) """
html_file = open('/home/zkilburn/projects/consulting/mocourtscraper/multiple-charges.html', 'r')
soup = BeautifulSoup(html_file.read(), features='lxml')

separators = soup.find_all('td', 'detailSeperator')

all_charges = []
for separator in separators:
    charge_labels = []
    detail_labels = separator.find_all_next('td', 'detailLabels')
    for label in detail_labels:
        label_text = label.text.strip().replace('\xa0','_')
        if label_text != '':
            label_text = label_text.replace(':','').replace(' ', '_').lower()
            charge_labels.append(label_text)

    charge_data = []
    detail_data = separator.find_all_next('td', 'detailData')
    for item in detail_data:
        item_text = item.text.strip().replace('\xa0',' ')
        if item_text != '':
            item_text = _replace_breaks(item_text)
            charge_data.append(item_text)

    charges = {}
    position = 0
    if len(charge_labels) == len(charge_data):
        for label in charge_labels:
            charges[label] = charge_data[position]
            position += 1

    all_charges.append(charges)

print(all_charges)