from mocourtscraper.scripts.case_parse import parse_parties, parse_charges
from mocourtscraper.constants import navigation
import requests
import re


PATH_PATT = "(?<=cases\/)(.*)(?=\?)"

def get_case_details(url, paths, details_result):
    case_path = re.findall(PATH_PATT, url)[0]
    for path in paths:
        path_url = url.replace(case_path, path)
        path_parse_function = navigation.PATH_PARSERS.get(path)
        body = requests.get(path_url).content
        details_result.append(globals()[path_parse_function](body))
    return details_result