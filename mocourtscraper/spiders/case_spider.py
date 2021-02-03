import scrapy
from mocourtscraper.scripts import parse
from mocourtscraper.constants import search_options
from mocourtscraper.utilities import case_spider_helper
from datetime import datetime

class CaseSpider(scrapy.Spider):
    name = "cases"

    #Setting defaults
    params = {
        'court_description': search_options.COURT_DESCRIPTIONS[0],
        'county_description': 'All',
        'location_description': 'All',
        'case_status': 'All',
        'start_date': datetime.now().strftime('%m/%d/%Y'),
        'case_type': 'All'
    }

    def __init__(self, **kwargs):
        for arg in kwargs.keys():
            self.params[arg] = kwargs.get(arg)
        self.start_urls = [
            case_spider_helper.build_url(self.params)
        ]
        super(CaseSpider, self).__init__(**kwargs)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')