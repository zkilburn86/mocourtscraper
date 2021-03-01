import scrapy
import pandas as pd
import os
import re
from mocourtscraper.utilities import case_spider_helper
from mocourtscraper.scripts.case_parse import parse_header


CASE_NUM_PATT = "(?<=caseNumber=)(.*)(?=&)"

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
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        details_result = []

        case_number = re.findall(CASE_NUM_PATT, response.url)[0]
        case_result = {'case_number': case_number}
        
        header_result = parse_header(response)
        details_result.append(header_result)

        details_result = case_spider_helper.get_case_details(response.url, self.paths, details_result)
        
        case_result['details'] = details_result
        yield case_result