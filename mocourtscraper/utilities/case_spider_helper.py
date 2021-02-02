from mocourtscraper.constants import navigation, search_options
from urllib.parse import urlencode, quote


PARAMS = navigation.SEARCH_PARAMS

def build_url(kwargs):

    handler = navigation.CASE_SEARCH_HANDLER

    for arg in kwargs.keys():
        param_handler = handler.get(arg)
        globals()[param_handler](kwargs.get(arg))
    
    param_string = urlencode(PARAMS, quote_via=quote)
    url = navigation.BASE_URL + '?' + param_string
    
    return url

def _handle_court(court):
    court_id = search_options.COURT_IDS.get(court)
    PARAMS['inputVO.courtId'] = court_id
    PARAMS['courtId'] = court_id
    PARAMS['inputVO.courtDesc'] = court

def _handle_county(county):
    county_code = search_options.COUNTY_CODES.get(county)
    PARAMS['inputVO.countyCode'] = county_code
    PARAMS['inputVO.countyDesc'] = county 
    PARAMS['CountyId'] = county_code

def _handle_location(location):
    location_code = search_options.LOCATION_CODES.get(location)
    PARAMS['inputVO.locationDesc'] = location 
    PARAMS['inputVO.locationCode'] = location_code

def _handle_status(status):
    status_index = search_options.CASE_STATUS_INDICES.get(status)
    PARAMS['inputVO.caseStatus'] = status
    PARAMS['inputVO.selectedIndexCaseStatus'] = status_index

def _handle_start_date(start_date):
    PARAMS['inputVO.startDate'] = start_date

def _handle_case_type(case_type):
    PARAMS['inputVO.caseType'] = case_type