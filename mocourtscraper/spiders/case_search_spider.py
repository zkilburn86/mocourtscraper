import scrapy
from scraper_api import ScraperAPIClient
from datetime import datetime
from bs4 import BeautifulSoup
from mocourtscraper.scripts.results_parse import has_results, get_pagination, NoResultsError, get_case_numbers
from mocourtscraper.constants import search_options, navigation
from mocourtscraper.utilities import case_search_spider_helper
from mocourtscraper.scripts.case_parse import parse_header, parse_parties, parse_charges
from mocourtscraper.creds import SCRAPER_API_KEY
import re


CASE_NUM_PATT = "(?<=caseNumber=)(.*)(?=&)"
PATH_PATT = "(?<=cases\/)(.*)(?=\?)"
CLIENT = ScraperAPIClient(SCRAPER_API_KEY)
class CaseSearchSpider(scrapy.Spider):
    name = "cases_search"

    #Setting default search parameters
    params = {
        'court_description': search_options.COURT_DESCRIPTIONS[0],
        'county_description': 'All',
        'location_description': 'All',
        'case_status': 'All',
        'start_date': datetime.now().strftime('%m/%d/%Y'),
        'case_type': 'All'
    }

    # Default case details to parse
    paths = ['parties.do','charges.do']

    results_output = []

    url_map = {}

    def __init__(self, **kwargs):
        for arg in kwargs.keys():
            self.params[arg] = kwargs.get(arg)
        self.start_urls = [
            case_search_spider_helper.build_url(self.params)
        ]
        super(CaseSearchSpider, self).__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            url = CLIENT.scrapyGet(url=url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        content = response.body
        soup = BeautifulSoup(content, features='lxml')

        if has_results(soup):
            result_counts = get_pagination(soup)
            next_result = case_search_spider_helper.get_next_result(result_counts)
            last_page = case_search_spider_helper.is_last_page(result_counts)

            self.results_output.extend(get_case_numbers(soup))

            if not last_page:
                url = case_search_spider_helper.build_url(self.params) + '&inputVO.startingRecord=' + str(next_result)
                url = CLIENT.scrapyGet(url=url)
                yield scrapy.Request(url=url, callback=self.parse)
        else:
            raise NoResultsError('No cases found')

        if last_page:           
            for case in self.results_output:
                case_path = re.findall(PATH_PATT, case['url'])[0]
                self.url_map[case['url']] = case_path
                for path in self.paths:
                    path_url = case['url'].replace(case_path, path)
                    self.url_map[path_url] = path
            
            for url in self.url_map.keys():
                case_number = re.findall(CASE_NUM_PATT, url)[0]
                path = self.url_map.get(url)
                url = CLIENT.scrapyGet(url=url)
                yield scrapy.Request(url=url, callback=self.parse_paths, cb_kwargs=dict(case_number=case_number, path=path))

    def parse_paths(self, response, case_number, path):
        case_details_result = {'case_number': case_number}

        path_parse_function = navigation.PATH_PARSERS.get(path)
        path_result = globals()[path_parse_function](response.body)

        case_details_result.update(path_result)
        
        yield case_details_result
