

BASE_URL = 'https://www.courts.mo.gov/casenet/cases/filingDateSearch.do'

SEARCH_PARAMS = {
    'inputVO.type': 'CT',
    'inputVO.courtId': '',
    'inputVO.errFlag': 'N',
    'inputVO.selectionAction': 'search',
    'inputVO.countyCode': '',
    'inputVO.juvenileUserFlag': 'N',
    'inputVO.countyDesc': '',
    'inputVO.selectedIndexCaseStatus': '',
    'inputVO.courtDesc': '',
    'inputVO.locationDesc': '',
    'courtId': '',
    'inputVO.startDate': '',
    'inputVO.caseStatus': '',
    'inputVO.caseType': '',
    'CountyId': '',
    'inputVO.locationCode': '',
    'findButton': 'Find'
}

CASE_SEARCH_HANDLER = {
    'court_description': '_handle_court',
    'county_description': '_handle_county',
    'location_description': '_handle_location',
    'case_status': '_handle_status',
    'start_date': '_handle_start_date',
    'case_type': '_handle_case_type'
}