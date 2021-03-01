from mocourtscraper.scripts.case_parse import parse_parties, parse_charges
from mocourtscraper.constants import navigation
from mocourtscraper.creds import SCRAPER_API_KEY
from scraper_api import ScraperAPIClient
import re


PATH_PATT = "(?<=cases\/)(.*)(?=\?)"
CLIENT = ScraperAPIClient(SCRAPER_API_KEY)

def get_case_details(url, paths, details_result):
    case_path = re.findall(PATH_PATT, url)[0]
    for path in paths:
        path_url = url.replace(case_path, path)
        path_parse_function = navigation.PATH_PARSERS.get(path)
        body = CLIENT.get(url=path_url).content
        details_result.append(globals()[path_parse_function](body))
    return details_result
