from bs4 import BeautifulSoup
import pandas as pd
import json
from mocourtscraper.creds import SCRAPER_API_KEY
from scraper_api import ScraperAPIClient
import re

CLIENT = ScraperAPIClient(SCRAPER_API_KEY)
