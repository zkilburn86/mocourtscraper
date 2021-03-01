from bs4 import BeautifulSoup
import pandas as pd
import json
import requests 
import re

def _replace_breaks(text):
    text = text.replace('\n','')
    text = text.replace('\t','')
    text = text.replace('\r','')
    return text

url = 'https://www.courts.mo.gov/casenet/cases/charges.do?inputVO.caseNumber=703480865&inputVO.courtId=SMPDB0005_CT42'
req = requests.get(url)
soup = BeautifulSoup(req.content, features='lxml')

charge_labels = []
detail_labels = soup.find_all('td', 'detailLabels')
for label in detail_labels:
    label_text = label.text.strip().replace('\xa0','_')
    if label_text != '':
        label_text = label_text.replace(':','').replace(' ', '_').lower()
        charge_labels.append(label_text)

charge_data = []
detail_data = soup.find_all('td', 'detailData')
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

print(charges)