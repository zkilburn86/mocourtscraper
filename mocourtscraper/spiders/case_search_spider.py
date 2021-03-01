import scrapy
from scraper_api import ScraperAPIClient
from datetime import datetime
from bs4 import BeautifulSoup
from mocourtscraper.scripts.results_parse import has_results, get_results, get_pagination, NoResultsError, post_process
from mocourtscraper.constants import search_options
from mocourtscraper.utilities import case_search_spider_helper
from mocourtscraper.creds import SCRAPER_API_KEY

CLIENT = ScraperAPIClient(SCRAPER_API_KEY)
class CaseSearchSpider(scrapy.Spider):
    name = "cases_search"

    #Setting defaults
    params = {
        'court_description': search_options.COURT_DESCRIPTIONS[0],
        'county_description': 'All',
        'location_description': 'All',
        'case_status': 'All',
        'start_date': datetime.now().strftime('%m/%d/%Y'),
        'case_type': 'All'
    }

    results_output = None

    file_name = 'run-' + str(int(datetime.timestamp(datetime.now()))) + '.csv'

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

            if self.results_output is None:
                self.results_output = get_results(soup)
            else:
                self.results_output = self.results_output.append(get_results(soup), ignore_index=True)

            if not last_page:
                url = case_search_spider_helper.build_url(self.params) + '&inputVO.startingRecord=' + str(next_result)
                url = CLIENT.scrapyGet(url=url)
                yield scrapy.Request(url=url, callback=self.parse)
        else:
            raise NoResultsError('No cases found')

        if last_page:
            self.results_output = post_process(self.results_output)
            yield self.results_output.to_csv('runs/' + self.file_name, index=False)
