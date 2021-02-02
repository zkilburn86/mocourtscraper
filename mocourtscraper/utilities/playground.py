from mocourtscraper.utilities import chromedriver
from mocourtscraper.constants import search_options, navigation
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pprint
from urllib.parse import urlencode, quote
