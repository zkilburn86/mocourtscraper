from mocourtscraper.constants import navigation, search_options
from urllib.parse import urlencode, quote


def build_url(kwargs):

    handler = navigation.CASE_SEARCH_HANDLER
    PARAMS = navigation.SEARCH_PARAMS.copy()

    for arg in kwargs.keys():
        param_handler = handler.get(arg)
        globals()[param_handler](kwargs.get(arg), PARAMS)
    
    param_string = urlencode(PARAMS, quote_via=quote)
    url = navigation.BASE_URL + '?' + param_string

    return url

def is_last_page(result_counts):
    last_result_on_page = result_counts[1]
    last_result = result_counts[2]

    if last_result_on_page == last_result:
        return True
    else:
        return False

def get_next_result(result_counts):
    return result_counts[1] + 1

def build_case_url(case_number, location):
    court_param = 'inputVO.courtId=' + navigation.LOCATION_TO_COURT_ID[location]
    case_param = 'inputVO.caseNumber=' + case_number
    url = navigation.CASE_URL + navigation.CASE_PATHS[0] + '?' + case_param + '&' + court_param
    return url

def _handle_court(court, PARAMS):
    court_id = search_options.COURT_IDS.get(court)
    if court_id is not None:
        PARAMS['inputVO.courtId'] = court_id
        PARAMS['courtId'] = court_id
    PARAMS['inputVO.courtDesc'] = court

def _handle_county(county, PARAMS):
    county_code = search_options.COUNTY_CODES.get(county)
    if county_code is not None:
        PARAMS['inputVO.countyCode'] = county_code
        PARAMS['CountyId'] = county_code
    PARAMS['inputVO.countyDesc'] = county 
    
def _handle_location(location, PARAMS):
    location_code = search_options.LOCATION_CODES.get(location)
    if location_code is not None:
        PARAMS['inputVO.locationCode'] = location_code
    PARAMS['inputVO.locationDesc'] = location 

def _handle_status(status, PARAMS):
    status_index = search_options.CASE_STATUS_INDICES.get(status)
    PARAMS['inputVO.caseStatus'] = status
    PARAMS['inputVO.selectedIndexCaseStatus'] = status_index

def _handle_start_date(start_date, PARAMS):
    PARAMS['inputVO.startDate'] = start_date

def _handle_case_type(case_type, PARAMS):
    PARAMS['inputVO.caseType'] = case_type
    