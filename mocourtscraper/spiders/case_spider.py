import scrapy
import pandas as pd
import os
import re
from mocourtscraper.utilities import case_spider_helper


PATT = "(?<=caseNumber=)(.*)(?=&)"

class CaseSpider(scrapy.Spider):
    name = "cases"

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
        case_number = re.findall(PATT, response.url)[0]
        case_result = {
            'case_number': case_number
        }
        parsed_case = case_spider_helper.parse_case(response.body)
        case_result.update(parsed_case)
        yield case_result