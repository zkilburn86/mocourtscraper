from bs4 import BeautifulSoup
from mocourtscraper.scripts import case_parse


def parse_case(page_source):
    soup = BeautifulSoup(page_source, features='lxml')
    header_result = case_parse.parse_header(soup)
    return header_result