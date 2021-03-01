import scrapy
from scraper_api import ScraperAPIClient
import pandas as pd
import os
import re
from mocourtscraper.utilities import case_spider_helper
from mocourtscraper.scripts.case_parse import parse_header
from mocourtscraper.creds import SCRAPER_API_KEY


CASE_NUM_PATT = "(?<=caseNumber=)(.*)(?=&)"
CLIENT = ScraperAPIClient(SCRAPER_API_KEY)

class CaseSpider(scrapy.Spider):
    name = "cases"

    # Default case details to parse
    paths = ['parties.do','charges.do']

    def start_requests(self):
        cases_dir = getattr(self, 'dir', None)
        search_results = os.listdir(cases_dir)
        start_urls = []

        for result in search_results:
            df = pd.read_csv(cases_dir + '/' + result)
            start_urls.extend(df['Case_URL'].to_list())

        for url in start_urls:
            case_number = re.findall(CASE_NUM_PATT, url)[0]
            clean_url = url
            url = CLIENT.scrapyGet(url=url)
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(case_number=case_number, clean_url=clean_url))

    def parse(self, response, case_number, clean_url):
        details_result = []

        case_result = {'case_number': case_number}
        
        header_result = parse_header(response)
        details_result.append(header_result)

        details_result = case_spider_helper.get_case_details(clean_url, self.paths, details_result)
        
        case_result['details'] = details_result
        yield case_result