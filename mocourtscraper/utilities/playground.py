from bs4 import BeautifulSoup
import pandas as pd
import json
import requests 
import re

url = 'https://www.courts.mo.gov/casenet/cases/parties.do?inputVO.caseNumber=703480865&inputVO.courtId=SMPDB0005_CT42'
req = requests.get(url)
soup = BeautifulSoup(req.content, features='lxml')

num_of_parties = 0
detail_separators = soup.find_all('td', 'detailSeperator')
for detail in detail_separators:
    cell_text = detail.text.strip()
    if cell_text != '' and 'represented by' not in cell_text:
        party = ' '.join(cell_text.split())
        party_details = party.split(' , ')
        num_of_parties += 1
        if len(party_details) == 3:
            print('First Name: ', party_details[1], ' | Last Name: ', party_details[0], ' | Role: ', party_details[2])
        if len(party_details) == 2:
            print('Party: ', party_details[0], ' | Role: ', party_details[1])

party_addresses = []
detail_data = soup.find_all('td', 'detailData')
for detail in detail_data:
    cell_text = detail.text.strip()
    if cell_text != '':
        party_addresses.append(' '.join(cell_text.split()))

indexer = 0
if len(party_addresses) == num_of_parties:
    for address in party_addresses:
        address_detail = address.split(' Year of Birth: ')
        