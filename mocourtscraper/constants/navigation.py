

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

CASE_URL = 'https://www.courts.mo.gov/casenet/cases/'

CASE_PATHS = [
    'header.do',
    'parties.do',
    'searchDockets.do',
    'charges.do',
    'service.do',
    'filings.do',
    'events.do',
    'judgements.do',
    'garnishment.do'
]

PATH_PARSERS = {
    'parties.do': 'parse_parties',
    'charges.do': 'parse_charges',
    'header.do': 'parse_header'
}

LOCATION_TO_COURT_ID = {
    'Novinger Municipal': 'SMPDB0004_CT02', 'Kirksville Municipal Court': 'SMPDB0004_CT02', 'Kirksville Municipal': 'SMPDB0004_CT02',
    'Circuit Division': 'SMPDB0001_CT04', 'Brashear Municipal': 'SMPDB0004_CT02', 
    'Associate Division Adair': 'SMPDB0004_CT02', 'Country Club Municipal': 'CT05', 
    'Savannah Municipal': 'CT05', 'Associate Division': 'SMPDB0001_CT04', 'Tarkio Municipal Court': 'SMPDB0001_CT04', 
    'Rock Port Municipal': 'SMPDB0001_CT04', 'Fairfax Municipal': 'SMPDB0001_CT04', 'Mexico Municipal Court': 'CT12', 
    'Vandalia Municipal Court': 'CT12', 'Benton City Municipal Court': 'CT12', 'Martinsburg Municipal Division': 'CT12', 
    'Circuit Division Audrain': 'CT12', 'Associate Division Audrain': 'CT12', 'Vandiver Village Audrain': 'CT12', 
    'Farber Municipal Court': 'CT12', 'Laddonia Municipal Court': 'CT12', 'Rush Hill Municipal Court': 'CT12', 
    'Wheaton Municipal': 'CT39', 'Exeter Municipal': 'CT39', 'Cassville Municipal Court': 'CT39', 'Barry': 'CT39', 
    'Butterfield Municipal': 'CT39', 'Monett Municipal': 'CT39', 'Purdy Municipal': 'CT39', 
    'Associate Division Barry': 'CT39', 'Seligman Municipal Court': 'CT39', 'Washburn Municipal': 'CT39', 
    'Lamar Municipal': 'SMPDB0004_CT28', 'Golden City Municipal': 'SMPDB0004_CT28', 
    'Liberal Municipal Court': 'SMPDB0004_CT28', 'Adrain Municipal': 'SMPDB0005_CT27', 'Tipton Municipal': 'SMPDB0004_CT26', 
    'Rich Hill Municipal': 'SMPDB0005_CT27', 'Bates County Circuit Court': 'SMPDB0005_CT27', 
    'Associate Div Bates': 'SMPDB0005_CT27', 'Cole Camp Municipal': 'SMPDB0005_CT30', 'Warsaw Municipal Court': 'SMPDB0005_CT30', 
    'Associate/Circuit Divisions': 'SMPDB0004_CT36', 'Lincoln Municipal': 'SMPDB0005_CT30', 
    'Marble Hill Municipal': 'SMPDB0001_CT32', 'Sturgeon Municipal Division': 'CT13', 'Hallsville Municipal Division': 'CT13', 
    'Columbia Municipal': 'CT13', 'Probate Division': 'CT22', 'Ashland Municipal Division': 'CT13', 
    'Centralia Municipal Division': 'CT13', 'Easton Buchanan Municipal': 'CT05', 'Fisk Municipal Division': 'SMPDB0004_CT36', 
    'Qulin Municipal Division': 'SMPDB0004_CT36', 'Caldwell Municipal': 'SMPDB0005_CT43', 'Polo Municipal': 'SMPDB0005_CT43', 
    'Braymer Municipal': 'SMPDB0005_CT43', 'Breckenridge Municipal': 'SMPDB0005_CT43', 'Cowgill Municipal': 'SMPDB0005_CT43', 
    'Kidder Municipal': 'SMPDB0005_CT43', 'Caldwell Circuit Court': 'SMPDB0005_CT43', 'Juvenile Office Caldwell': 'SMPDB0005_CT43', 
    'New Bloomfield Municipal': 'CT13', 'Auxvasse Municipal': 'CT13', 'Fulton Municipal Court': 'CT13', 
    'Holts Summit Municipal Court': 'CT13', 'Linn Creek Municipal Court': 'SMPDB0004_CT26', 
    'Sunrise Beach Municipal Court': 'SMPDB0004_CT26', 'Camdenton Municipal': 'SMPDB0004_CT26', 
    'Four Seasons Municipal Court': 'SMPDB0004_CT26', 'Camden Circuit': 'SMPDB0004_CT26', 'Perryville Municipal': 'SMPDB0001_CT32', 
    'Circuit Division (Cape Girard)': 'SMPDB0001_CT32', 'Circuit Division (Jackson)': 'SMPDB0001_CT32', 
    'Associate Probate Division': 'SMPDB0001_CT32', 'Associate Division (Jackson)': 'SMPDB0001_CT32', 
    'Gordonville Municipal': 'SMPDB0001_CT32', 'Allenville Municipal': 'SMPDB0001_CT32', 'Delta Municipal': 'SMPDB0001_CT32', 
    'Bogard Municipal': 'CT08', 'Bosworth Municipal': 'CT08', 'Hale Municipal': 'CT08', 'Norborne Municipal': 'CT08', 
    'Carrollton Municipal': 'CT08', 'Tina Municipal': 'CT08', 'Ellsinore Municipal': 'SMPDB0005_CT37', 
    'Grandin Municipal': 'SMPDB0005_CT37', 'Van Buren Municipal': 'SMPDB0005_CT37', 'Archie Municipal': 'CT17', 
    'Cleveland Municipal': 'CT17', 'Creighton Municipal': 'CT17', 'Drexel Municipal': 'CT17', 'East Lynne Municipal': 'CT17', 
    'Freeman Municipal': 'CT17', 'Lake Annette Municipal': 'CT17', 'Strasburg Municipal': 'CT17', 'Garden City Municipal': 'CT17', 
    'Pleasant Hill Municipal': 'CT17', 'Cass County Ordinance Court': 'CT17', 'Cass Circuit': 'CT17', 
    'Stockton Municipal Court': 'SMPDB0004_CT28', 'El Dorado Springs Municipal': 'SMPDB0004_CT28', 
    'Jerico Springs Municipal': 'SMPDB0004_CT28', 'Ozark Municipal': 'CT38', 'Sparta Municipal Division': 'CT38', 
    'City of Billings Municipal Court': 'CT38', 'Nixa Municipal Court': 'CT38', 'City of Clever Municipal Court': 'CT38', 
    'Christian Historic Courthouse': 'CT38', 'Christian County Cir Ct Bldg': 'CT38', 'Highlandville Municipal': 'CT38', 
    'Associate Civil Div Christian': 'CT38', 'Assoc Crim/Probate Christian': 'CT38', 'Kahoka Municipal': 'SMPDB0004_CT01', 
    'Missouri City Municipal': 'SMPDB0001_CT07', 'Praethersville Municipal': 'SMPDB0001_CT07', 
    'Avondale Municipal': 'SMPDB0001_CT07', 'Birmingham Municipal': 'SMPDB0001_CT07', 'Glenaire Municipal': 'SMPDB0001_CT07', 
    'Holt Municipal': 'SMPDB0001_CT07', 'Mosby Municipal': 'SMPDB0001_CT07', 'Clay Circuit Court': 'SMPDB0001_CT07', 
    'North Kansas City Municipal': 'SMPDB0001_CT07', 'Smithville Municipal': 'SMPDB0001_CT07', 
    'Cameron Municipal Court': 'SMPDB0005_CT43', 'Clinton Circuit Court': 'SMPDB0005_CT43', 
    'Juvenile Office Clinton': 'SMPDB0005_CT43', 'Trimble Municipal': 'SMPDB0005_CT43', 'Taos Municipal': 'SMPDB0004_CT19', 
    'Wardsville Municipal': 'SMPDB0004_CT19', 'Jefferson City Muni': 'SMPDB0004_CT19', 'Boonville Municipal Division': 'CT18', 
    'Prairie Home Municipal': 'CT18', 'Windsor Place Municipal': 'CT18', 'Pilot Grove Municipal Division': 'CT18', 
    'Otterville Municipal': 'CT18', 'Bunceton Municipal': 'CT18', 'Blackwater Municipal': 'CT18', 
    'Bourbon Municipal Court': 'SMPDB0005_CT42', 'Steelville Municipal Court': 'SMPDB0005_CT42', 
    'Leasburg Municipal': 'SMPDB0005_CT42', 'Greenfield Municipal': 'SMPDB0004_CT28', 'Everton Municipal Court': 'SMPDB0004_CT28', 
    'Lockwood Municipal Court': 'SMPDB0004_CT28', 'Urbana Municipal': 'SMPDB0005_CT30', 'Buffalo Municipal': 'SMPDB0005_CT30', 
    'Gallatin Municipal': 'SMPDB0005_CT43', 'Altamont Municipal': 'SMPDB0005_CT43', 'Pattonsburg Municipal': 'SMPDB0005_CT43', 
    'Jamesport Municipal': 'SMPDB0005_CT43', 'Winston Municipal': 'SMPDB0005_CT43', 'Daviess Circuit Court': 'SMPDB0005_CT43', 
    'Associate Division Daviess': 'SMPDB0005_CT43', 'Juvenile Office Daviess': 'SMPDB0005_CT43', 
    'Clarksdale Municipal': 'SMPDB0005_CT43', 'Maysville Municipal': 'SMPDB0005_CT43', 'Osborn Municipal': 'SMPDB0005_CT43', 
    'Stewarsville Municipal': 'SMPDB0005_CT43', 'Unionstar Municipal': 'SMPDB0005_CT43', 'DeKalb Circuit Court': 'SMPDB0005_CT43', 
    'Associate Division DeKalb': 'SMPDB0005_CT43', 'Juvenile Office DeKalb': 'SMPDB0005_CT43', 
    'Dent Judicial Building': 'SMPDB0005_CT42', 'Salem Municipal': 'SMPDB0005_CT42', 'Ava Municipal': 'SMPDB0005_CT44', 
    'Douglas Circuit Court': 'SMPDB0005_CT44', 'Associate Division Douglas': 'SMPDB0005_CT44', 
    'Hornersville Municipal': 'SMPDB0001_CT35', 'Arbyrd Municipal': 'SMPDB0001_CT35', 'Malden Municipal': 'SMPDB0001_CT35', 
    'Campbell Municipal': 'SMPDB0001_CT35', 'Senath Municipal': 'SMPDB0001_CT35', 'Kennett Municipal Court': 'SMPDB0001_CT35', 
    'Gerald Municipal Court': 'SMPDB0004_CT20', 'St Clair Municipal Court': 'SMPDB0004_CT20', 
    'New Haven Municipal Court': 'SMPDB0004_CT20', 'Miramiguoa Park Municipal': 'SMPDB0004_CT20', 
    'Pacific Municipal': 'SMPDB0004_CT20', 'Associate Division VII': 'SMPDB0004_CT20', 'Associate Division VI': 'SMPDB0004_CT20', 
    'Franklin Co Municipal': 'SMPDB0004_CT20', 'Sullivan Municipal': 'SMPDB0004_CT20', 'Union Municipal Court': 'SMPDB0004_CT20', 
    'City of Washington': 'SMPDB0004_CT20', 'Gasconade Municipal Court': 'SMPDB0004_CT20', 
    'Berger Municipal Court': 'SMPDB0004_CT20', 'Hermann Municipal': 'SMPDB0004_CT20', 'Owensville Municipal': 'SMPDB0004_CT20', 
    'Rosebud Municipal': 'SMPDB0004_CT20', 'Bland Municipal': 'SMPDB0004_CT20', 'Stanberry Municipal': 'SMPDB0001_CT04', 
    'Albany Municipal': 'SMPDB0001_CT04', 'King City Municipal': 'SMPDB0001_CT04', 'Walnut Grove Municipal': 'CT31', 
    'Republic Municipal': 'CT31', 'Ash Grove Municipal': 'CT31', 'Fair Grove Municipal Court': 'CT31', 
    'Stafford Municipal Court': 'CT31', 'Battlefield Municipal': 'CT31', 'Springfield Municipal': 'CT31', 
    'Willard Municipal Court': 'CT31', 'Greene County Ordinance Court': 'CT31', 'Trenton Municipal': 'SMPDB0001_CT03', 
    'Gilman City Municipal': 'SMPDB0001_CT03', 'Bethany Municipal': 'SMPDB0001_CT03', 'Eagleville Municipal': 'SMPDB0001_CT03', 
    'Ridgeway Municipal': 'SMPDB0001_CT03', 'New Hampton Municipal': 'SMPDB0001_CT03', 'Calhoun Municipal': 'SMPDB0005_CT27', 
    'Deepwater Municipal': 'SMPDB0005_CT27', 'Montrose Municipal': 'SMPDB0005_CT27', 'Urich Municipal': 'SMPDB0005_CT27', 
    'Henry County Circuit Court': 'SMPDB0005_CT27', 'Windsor Municipal': 'SMPDB0005_CT27', 'Big Lake Municipal': 'SMPDB0001_CT04', 
    'Maitland Municipal': 'SMPDB0001_CT04', 'Oregon Municipal': 'SMPDB0001_CT04', 'Forest City Municipal': 'SMPDB0001_CT04', 
    'Mound City Municipal': 'SMPDB0001_CT04', 'Craig Municipal': 'SMPDB0001_CT04', 'New Franklin Municipal': 'SMPDB0001_CT14', 
    'Fayette Municipal': 'SMPDB0001_CT14', 'Glasgow Municipal': 'SMPDB0001_CT14', 'Viburnum Municipal Court': 'SMPDB0005_CT42', 
    'Ironton Municipal': 'SMPDB0005_CT42', 'Pilot Knob Municipal Court': 'SMPDB0005_CT42', 'Arcadia Municipal': 'SMPDB0005_CT42', 
    'Annapolis Municipal': 'SMPDB0005_CT42', 'Lake Lotawana Municipal Court': 'CT16', "Lee's Summit Municipal Court": 'CT16', 
    'Lake Tapawingo Municipal': 'CT16', 'Grandview Municipal': 'CT16', 'Raytown Municipal': 'CT16', 'Greenwood Municipal': 'CT16', 
    'Circuit Division (Family Ct Justice Cntr)': 'CT16', 'Circuit Division (Kansas City)': 'CT16', 
    'Circuit Division (Independence)': 'CT16', 'Criminal Justice Center': 'CT16', 'Independence Criminal/Traffic': 'CT16', 
    'Kansas City Criminal/Traffic': 'CT16', 'Lone Jack Municipal': 'CT16', 'Probate (Kansas City)': 'CT16', 
    'Probate (Independence)': 'CT16', 'Carterville Municipal': 'SMPDB0001_CT29', 'Sarcoxie Municipal': 'SMPDB0001_CT29', 
    'Circuit Division (Joplin)': 'SMPDB0001_CT29', 'Circuit Division (Carthage)': 'SMPDB0001_CT29', 
    'Carthage Municipal': 'SMPDB0001_CT29', 'Probate Division III': 'SMPDB0001_CT29', 'Associate Division IV': 'SMPDB0001_CT29', 
    'Associate Division V': 'SMPDB0001_CT29', 'Duquesne Municipal': 'SMPDB0001_CT29', 'Oronogo Municipal Court': 'SMPDB0001_CT29', 
    'Joplin Municipal': 'SMPDB0001_CT29', 'Carl Junction Municipal': 'SMPDB0001_CT29', 'Webb City Municipal': 'SMPDB0001_CT29', 
    'Purcell Municipal': 'SMPDB0001_CT29', 'Jasper Municipal': 'SMPDB0001_CT29', 'Airport Drive Municipal': 'SMPDB0001_CT29', 
    'Byrnes Municipal': 'CT23', 'Crystal City Municipal': 'CT23', 'Arnold Municipal': 'CT23', 'Herculaneum Municipal': 'CT23', 
    'Desoto Municipal': 'CT23', 'Festus Municipal': 'CT23', 'Jefferson County Municipal': 'CT23', 'Hillsboro Municipal': 'CT23', 
    'Jefferson Circuit Court': 'CT23', 'Pevely Municipal': 'CT23', 'Centerview Muncipal': 'CT17', 'Chilhowee Municipal': 'CT17', 
    'Holden Municipal': 'CT17', 'Kingsville Municipal': 'CT17', 'Leeton Municipal': 'CT17', 'Knob Noster Municipal': 'CT17', 
    'Edina Municipal': 'SMPDB0004_CT02', 'Associate Division Knox': 'SMPDB0004_CT02', 'Lebanon Municipal Court': 'SMPDB0004_CT26', 
    'Conway Municipal': 'SMPDB0004_CT26', 'Laclede Circuit': 'SMPDB0004_CT26', 'Corder Municipal': 'SMPDB0001_CT15', 
    'Mayview Municipal': 'SMPDB0001_CT15', 'Emma Municipal': 'SMPDB0001_CT15', 'Lake Lafayette Municipal': 'SMPDB0001_CT15', 
    'Napoleon Municipal': 'SMPDB0001_CT15', 'Wellington Municipal': 'SMPDB0001_CT15', 'Waverly Municipal': 'SMPDB0001_CT15', 
    'Concordia Municipal': 'SMPDB0001_CT15', 'Odessa Municipal Court': 'SMPDB0001_CT15', 
    'Higginsville Municipal Court': 'SMPDB0001_CT15', 'Alma Municipal': 'SMPDB0001_CT15', 'Lafayette Hall': 'SMPDB0001_CT15', 
    'Bates City Municipal': 'SMPDB0001_CT15', 'Verona Municipal': 'CT39', 'Miller Municipal Court': 'CT39', 
    'Aurora Municipal Court': 'CT39', 'Marionville Municipal': 'CT39', 'Associate Division Lawrence': 'CT39', 'Lawrence': 'CT39', 
    'Mount Vernon Municipal': 'CT39', 'Pierce City Municipal': 'CT39', 'Freistatt Municipal Court': 'CT39', 
    'Stotts City Municipal Court': 'CT39', 'Canton Municipal': 'SMPDB0004_CT02', 'Lagrange Municipal': 'SMPDB0004_CT02', 
    'Silex Municipal': 'SMPDB0005_CT45', 'Truxton Municipal': 'SMPDB0005_CT45', 'Elsberry Municipal': 'SMPDB0005_CT45', 
    'Moscow Mills Municipal': 'SMPDB0005_CT45', 'Old Monroe Municipal': 'SMPDB0005_CT45', 'Foley Municipal': 'SMPDB0005_CT45', 
    "Fountain N' Lakes": 'SMPDB0005_CT45', 'Hawk Point Municipal': 'SMPDB0005_CT45', 'Winfield Municipal': 'SMPDB0005_CT45', 
    'Browning Municipal': 'SMPDB0001_CT09', 'Bucklin Municipal': 'SMPDB0001_CT09', 'Marceline Municipal': 'SMPDB0001_CT09', 
    'Brookfield Municipal': 'SMPDB0001_CT09', 'Chillicothe Municipal': 'SMPDB0005_CT43', 
    'Associate Division Livingston': 'SMPDB0005_CT43', 'Juvenile Office Livingston': 'SMPDB0005_CT43', 
    'Livingston Circuit Court': 'SMPDB0005_CT43', 'Callao Municipal': 'SMPDB0004_CT41', 'Laplata Municipal': 'SMPDB0004_CT41', 
    'Macon Municipal Court': 'SMPDB0004_CT41', 'Bevier Municipal': 'SMPDB0004_CT41', 'South Gifford Macon': 'SMPDB0004_CT41', 
    'Atlanta Municipal': 'SMPDB0004_CT41', 'Fredericktown Municipal': 'SMPDB0005_CT24', 'Marquand Municipal': 'SMPDB0005_CT24', 
    'Vienna Municipal': 'SMPDB0005_CT25', 'Belle Municipal': 'SMPDB0005_CT25', 'Maries Associate': 'SMPDB0005_CT25', 
    'Maries Circuit': 'SMPDB0005_CT25', 'Hannibal Municipal Court': 'SMPDB0004_CT10', 'Palmyra Municipal': 'SMPDB0004_CT10', 
    'Marion Palmyra': 'SMPDB0004_CT10', 'Marion Hannibal': 'SMPDB0004_CT10', 'Lanagan Municipal Court': 'SMPDB0001_CT40', 
    'Pineville Municipal Court': 'SMPDB0001_CT40', 'Anderson Municipal Court': 'SMPDB0001_CT40', 
    'Noel Municipal Court': 'SMPDB0001_CT40', 'Goodman Municipal Court': 'SMPDB0001_CT40', 
    'Southwest City Municipal Court': 'SMPDB0001_CT40', 'McDonald': 'SMPDB0001_CT40', 'Princeton Municipal': 'SMPDB0001_CT03', 
    'Mercer Municipal': 'SMPDB0001_CT03', 'Eldon Municipal Court': 'SMPDB0004_CT26', 'Iberia Municipal Court': 'SMPDB0004_CT26', 
    'Lake Ozark Municipal': 'SMPDB0004_CT26', 'Miller Circuit': 'SMPDB0004_CT26', 'Anniston Municipal Court': 'SMPDB0005_CT33', 
    'California Municipal Court': 'SMPDB0004_CT26', 'Clarksburg Municipal Court': 'SMPDB0004_CT26', 
    'Associate Division Moniteau': 'SMPDB0004_CT26', 'Moniteau Circuit': 'SMPDB0004_CT26', 'Jamestown Municipal': 'SMPDB0004_CT26', 
    'Madison Municipal': 'SMPDB0004_CT10', 'Paris Municipal': 'SMPDB0004_CT10', 'Monroe City Municipal': 'SMPDB0004_CT10', 
    'Middleton Municipal Court': 'CT12', 'Montgomery Municipal Court': 'CT12', 'Rhineland Municipal': 'CT12', 
    'Wellsville Municipal': 'CT12', 'Bellflower Municipal Court': 'CT12', 'New Florence Municipal Court': 'CT12', 
    'High Hill Municipal Court': 'CT12', 'Jonesburg Municipal Court': 'CT12', 'Laurie Municipal': 'SMPDB0004_CT26', 
    'Stover Municipal': 'SMPDB0004_CT26', 'Associate Division Morgan': 'SMPDB0004_CT26', 'Morgan': 'SMPDB0004_CT26', 
    'Lilbourn Municipal': 'SMPDB0005_CT34', 'Parma Municipal Court': 'SMPDB0005_CT34', 
    'New Madrid Municipal Court': 'SMPDB0005_CT34', 'Risco Municipal': 'SMPDB0005_CT34', 
    'Morehouse Municipal Court': 'SMPDB0005_CT34', 'Portageville Municipal Court': 'SMPDB0005_CT34', 
    'Marston Municipal': 'SMPDB0005_CT34', 'Canalou Municipal': 'SMPDB0005_CT34', 'Matthews Municipal': 'SMPDB0005_CT34', 
    'Diamond Municipal Court': 'SMPDB0001_CT40', 'Granby Municipal Court': 'SMPDB0001_CT40', 'Seneca Municipal Court': 'SMPDB0001_CT40', 
    'Neosho Municipal Court': 'SMPDB0001_CT40', 'Fairview Municipal': 'SMPDB0001_CT40', 'Newton': 'SMPDB0001_CT40', 
    'Hopkins Municipal': 'SMPDB0001_CT04', 'Pickering Municipal': 'SMPDB0001_CT04', 'Skidmore Municipal': 'SMPDB0001_CT04', 
    'Maryville Municipal Court': 'SMPDB0001_CT04', 'Maryville Municipal': 'SMPDB0001_CT04', 'City of Tarkio': 'SMPDB0001_CT04', 'Burlington Junction Municipal': 'SMPDB0001_CT04', 
    'Clearmont Municipal': 'SMPDB0001_CT04', 'Clyde Municipal': 'SMPDB0001_CT04', 'Conception Junction Municipal': 'SMPDB0001_CT04', 
    'Conception Municipal': 'SMPDB0001_CT04', 'Elmo Municipal': 'SMPDB0001_CT04', 'Graham Municipal': 'SMPDB0001_CT04', 
    'Guilford Municipal': 'SMPDB0001_CT04', 'Parnell Municipal': 'SMPDB0001_CT04', 'Quitman Municipal': 'SMPDB0001_CT04', 
    'Ravenwood Municipal': 'SMPDB0001_CT04', 'Barnard Municipal': 'SMPDB0001_CT04', 'Alton Municipal': 'SMPDB0005_CT37', 
    'Koshkonong Municipal': 'SMPDB0005_CT37', 'Linn Municipal': 'SMPDB0004_CT20', 'Freeburg Municipal': 'SMPDB0004_CT20', 
    'Gainsville Municipal Court': 'SMPDB0005_CT44', 'Theodosia Municipal Court': 'SMPDB0005_CT44', 
    'Associate Division Ozark': 'SMPDB0005_CT44', 'Ozark Circuit Court': 'SMPDB0005_CT44', 
    'Caruthersville Municipal Court': 'SMPDB0005_CT34', 'Steele Municipal Court': 'SMPDB0005_CT34', 
    'Pemiscot County Justice Center': 'SMPDB0005_CT34', 'Juvenile Office Perry': 'SMPDB0001_CT32', 'Greenridge Municipal': 'CT18', 
    'Sedalia Municipal Court': 'CT18', 'Smithton Municipal': 'CT18', 'Houstonia Municipal': 'CT18', 'Hughesville Municipal': 'CT18', 
    'La Monte Municipal': 'CT18', 'Edgar Springs Municipal': 'SMPDB0005_CT25', 'Newburg Municipal': 'SMPDB0005_CT25', 
    'St James Municipal': 'SMPDB0005_CT25', 'Doolittle Municipal': 'SMPDB0005_CT25', 'Rolla Municipal Court': 'SMPDB0005_CT25', 
    'Phelps Circuit': 'SMPDB0005_CT25', 'Louisiana Municipal Court': 'SMPDB0005_CT45', 'Eolia Municipal': 'SMPDB0005_CT45', 
    'Clarksville Municipal': 'SMPDB0005_CT45', 'Frankford Municipal': 'SMPDB0005_CT45', 'Bowling Green Municipal': 'SMPDB0005_CT45', 
    'Dearborn Municipal': 'SMPDB0001_CT06', 'Platte City Municipal': 'SMPDB0001_CT06', 'Weston Municipal Court': 'SMPDB0001_CT06', 'Weston Municipal': 'SMPDB0001_CT06',
    'Tracy Municipal Court': 'SMPDB0001_CT06', 'Ferrelview Municipal': 'SMPDB0001_CT06', 'Lake Waukomis Municipal': 'SMPDB0001_CT06', 
    'Camden Point Municipal': 'SMPDB0001_CT06', 'Edgerton Municipal': 'SMPDB0001_CT06', 'Houston Lake Municipal': 'SMPDB0001_CT06', 
    'Northmoor Muni': 'SMPDB0001_CT06', 'Northmoor Municipal': 'SMPDB0001_CT06', 'Pleasant Hope Municipal': 'SMPDB0005_CT30', 
    'Bolivar Municipal': 'SMPDB0005_CT30', 'Humansville Municipal': 'SMPDB0005_CT30', 'Waynesville Municipal': 'SMPDB0005_CT25', 
    'Dixon Municipal': 'SMPDB0005_CT25', 'Crocker Municipal': 'SMPDB0005_CT25', 'Richland Municipal Court': 'SMPDB0005_CT25', 
    'St Robert Municipal': 'SMPDB0005_CT25', 'Pulaski Circuit': 'SMPDB0005_CT25', 'Unionville Municipal': 'SMPDB0001_CT03', 
    'Center Municipal': 'SMPDB0004_CT10', 'New London Municipal': 'SMPDB0004_CT10', 'Perry Municipal': 'SMPDB0004_CT10', 
    'Ralls Circuit Court': 'SMPDB0004_CT10', 'Huntsville Municipal': 'SMPDB0001_CT14', 'Clark Municipal': 'SMPDB0001_CT14', 
    'Moberly Municipal Court': 'SMPDB0001_CT14', 'Crystal Lakes Municipal': 'CT08', 'Homestead Municipal': 'CT08', 
    'Wood Heights Municipal': 'CT08', 'Fleming Municipal': 'CT08', 'Hardin Municipal': 'CT08', 'Henrietta Municipal': 'CT08', 
    'Camden Municipal': 'CT08', 'Bunker Municipal Court': 'SMPDB0005_CT42', 'Ellington Municipal Court': 'SMPDB0005_CT42', 
    'Doniphan Municipal Court': 'SMPDB0004_CT36', 'Naylor Municipal Court': 'SMPDB0004_CT36', 'Blackburn Municipal': 'SMPDB0001_CT15', 
    'Slater Municipal': 'SMPDB0001_CT15', 'Marshall Municipal': 'SMPDB0001_CT15', 'Queen City Municipal': 'SMPDB0004_CT01', 
    'Greentop Municipal': 'SMPDB0004_CT01', 'Lancaster Municipal': 'SMPDB0004_CT01', 'Memphis Municipal': 'SMPDB0004_CT01', 
    'Scotts City Municipal': 'SMPDB0005_CT33', 'Miner Municipal Court': 'SMPDB0005_CT33', 'Morley Municipal Court': 'SMPDB0005_CT33', 
    'Benton Municipal Court': 'SMPDB0005_CT33', 'Kelso Municipal Court': 'SMPDB0005_CT33', 'Oran Municipal Court': 'SMPDB0005_CT33', 
    'Eminence Municipal': 'SMPDB0005_CT37', 'Winona Municipal': 'SMPDB0005_CT37', 'Birch Tree Municipal': 'SMPDB0005_CT37', 
    'Shelbina Municipal': 'SMPDB0004_CT41', 'Clarence Municipal': 'SMPDB0004_CT41', 'Shelbyville Municipal': 'SMPDB0004_CT41', 
    'Weldon Spring Municipal': 'CT11', 'St. Charles County Municipal Court': 'CT11', 'Traffic Division': 'CT11', 
    'Associate Civil/Small Claim': 'CT11', 'St Charles City Municipal': 'CT11', 'Dardenne Prarie Municipal': 'CT11', 
    'Criminal Associate Division': 'CT11', 'Foristell Municipal': 'CT11', 'Lake St. Louis Municipal': 'CT11', 
    "O'Fallon Municipal": 'CT11', 'Cottleville Municipal': 'CT11', 'St. Peters Municipal': 'CT11', 'Augusta Municipal': 'CT11', 
    'Wentzville Municipal': 'CT11', 'Appleton City Municipal': 'SMPDB0005_CT27', 'Lowry City Municipal': 'SMPDB0005_CT27', 
    'Osceola Municipal': 'SMPDB0005_CT27', 'St.Clair County Circuit Court': 'SMPDB0005_CT27', 'Leadwood Municipal': 'SMPDB0005_CT24', 
    'Farmington Municipal': 'SMPDB0005_CT24', 'Park Hills Municipal': 'SMPDB0005_CT24', 'Bonne Terre Municipal Court': 'SMPDB0005_CT24', 
    'Leadington Municipal': 'SMPDB0005_CT24', 'Desloge Municipal': 'SMPDB0005_CT24', 'Associate Division 3': 'SMPDB0005_CT24', 
    'Bellerive Acres Municipal': 'CT21', 'Crystal Lake Park Municipal': 'CT21', 'Frontenac Municipal Court': 'CT21', 
    'Greendale Municipal': 'CT21', 'Hillsdale Municipal': 'CT21', 'Kinloch Municipal': 'CT21', 'Lakeshire Municipal': 'CT21', 
    'PINE LAWN MUNICIPAL COURT': 'CT21', 'Wellston Municipal Division': 'CT21', 'Woodson Terrace Municipal': 'CT21', 
    'Kirkwood Municipal Court': 'CT21', 'Crestwood Municipal': 'CT21', 'Velda City Municipal': 'CT21', 
    'Pasadena Hills Municipal': 'CT21', 'Ladue Municipal Court': 'CT21', 'Brentwood Municipal': 'CT21', 
    'Velda Village Hills Municipal': 'CT21', 'Webster Groves Municipal Court': 'CT21', 'Normandy Municipal': 'CT21', 
    'Clayton Municipal Court': 'CT21', 'Olivette Municipal Court': 'CT21', 'St Ann Municipal Court': 'CT21', 
    'Richmond Heights Municipal': 'CT21', 'Shrewsbury Municipal': 'CT21', 'Winchester Municipal': 'CT21', 
    'Country Club Hills': 'CT21', 'Bridgeton Municipal': 'CT21', 'Uplands Park Municipal': 'CT21', 'Warson Woods Municipal': 'CT21', 
    'Champ Municipal': 'CT21', 'Ballwin Municipal': 'CT21', 'Pagedale Municipal Court': 'CT21', 'Oakland Municipal': 'CT21', 
    'Flordell Hills Municipal': 'CT21', 'St. John Municipal': 'CT21', 'Moline Acres Municipal': 'CT21', 'Overland Municipal': 'CT21', 
    'Bellefontaine Neighbors': 'CT21', 'University City Municipal': 'CT21', 'Clarkson Valley Municipal': 'CT21', 
    'Vinita Park Municipal Court': 'CT21', 'Sycamore Hills Municipal': 'CT21', 'Grantwood Village Municipal': 'CT21', 
    'Sunset Hills Municipal Court': 'CT21', 'Ellisville Municipal Court': 'CT21', 'Eureka Municipal': 'CT21', 
    'Town and Country Municipal': 'CT21', 'Edmundson Muncipal Court': 'CT21', 'Glen Echo Park Municipal': 'CT21', 
    'Bella Villa Municipal Court': 'CT21', 'Pasadena Park Municipal': 'CT21', 'Beverly Hills Municipal': 'CT21', 
    'Hazelwood Municipal': 'CT21', 'Berkeley Municipal': 'CT21', 'Creve Coeur Municipal': 'CT21', 'Florissant Municipal Court': 'CT21', 
    'Probate St Louis County': 'CT21', 'Maplewood Municipal Court': 'CT21', 'St Louis Co Municipal': 'CT21', 'St Louis County': 'CT21', 
    'Valley Park Municipal': 'CT21', 'Village of Westwood Municipal': 'CT21', 'Bel-Nor Municipal': 'CT21', 
    'Bel-Ridge Municipal Court': 'CT21', 'Black Jack Municipal': 'CT21', 'Breckenridge Hills Municipal': 'CT21', 
    'Calverton Park Municipal': 'CT21', 'Charlack Municipal Court': 'CT21', 'Chesterfield Municipal Court': 'CT21', 
    'Cool Valley Municipal': 'CT21', 'Dellwood Municipal': 'CT21', 'Des Peres Municipal': 'CT21', 'Fenton Municipal': 'CT21', 
    'Ferguson Municipal Court': 'CT21', 'Glendale Municipal': 'CT21', 'Hanley Hills Municipal Court': 'CT21', 'Jennings Municipal': 'CT21', 
    'Manchester Municipal': 'CT21', 'Maryland Heights Municipal': 'CT21', 'Northwoods Municipal Court': 'CT21', 
    'Riverview Municipal Court': 'CT21', 'Rock Hill Municipal Court': 'CT21', 'Wildwood Municipal Court': 'CT21', 
    'St. Mary Municipal': 'SMPDB0005_CT24', 'Ste. Genevieve Municipal': 'SMPDB0005_CT24', 'Dexter Municipal': 'SMPDB0001_CT35', 
    'Div III & Probate': 'SMPDB0001_CT35', 'Bell City Municipal': 'SMPDB0001_CT35', 'Essex Municipal': 'SMPDB0001_CT35', 
    'Kimberling City Municipal': 'CT39', 'Branson West Municipal': 'CT39', 'Crane Municipal Court': 'CT39', 
    'Reeds Springs Municipal': 'CT39', 'Galena Municipal': 'CT39', 'Indian Point Village Municipal': 'CT39', 'Stone': 'CT39', 
    'Milan Municipal': 'SMPDB0001_CT09', 'Green City Municipal': 'SMPDB0001_CT09', 'Forsyth Municipal': 'CT46', 
    'Branson Municipal': 'CT46', 'Merriam Woods Municipal': 'CT46', 'Associate Civil Division Taney': 'CT46', 
    'Assoc Crim/Probate Div Taney': 'CT46', 'Rockaway Beach Muni': 'CT46', 'Cabool Municipal': 'SMPDB0005_CT25', 
    'Houston Municipal': 'SMPDB0005_CT25', 'Licking Municipal': 'SMPDB0005_CT25', 'Summersville Municipal': 'SMPDB0005_CT25', 
    'South Central Correctional CR': 'SMPDB0005_CT25', 'Texas Circuit': 'SMPDB0005_CT25', 'Texas Associate': 'SMPDB0005_CT25', 
    'Carnahan Courthouse': 'CT22', 'St. Louis City Municipal': 'CT22', 'City of St. Louis': 'CT22', 
    'Moundville Municipal': 'SMPDB0004_CT28', 'Nevada Municipal': 'SMPDB0004_CT28', 'Bronaugh Municipal Court': 'SMPDB0004_CT28', 
    'Sheldon Municipal Court': 'SMPDB0004_CT28', 'Walker Municipal Court': 'SMPDB0004_CT28', 'Marthasville Municipal': 'CT12', 
    'Truesdale Municipal': 'CT12', 'Wright City Municipal': 'CT12', 'Innsbrook Municipal': 'CT12', 'Warrenton Municipal': 'CT12', 
    'Irondale Municipal': 'SMPDB0005_CT24', 'Caledonia Municipal': 'SMPDB0005_CT24', 'Potosi Municipal': 'SMPDB0005_CT24', 
    'Williamsville Municipal': 'SMPDB0005_CT42', 'Piedmont Municipal Court': 'SMPDB0005_CT42', 
    'Marshfield Municipal Court': 'SMPDB0005_CT30', 'Rogersville Municipal Court': 'SMPDB0005_CT30', 
    'Fordland Municipal': 'SMPDB0005_CT30', 'Seymour Muni': 'SMPDB0005_CT30', 'Nianqua Municipal': 'SMPDB0005_CT30', 
    'Grant City Municipal': 'SMPDB0001_CT04', 'Hartville Municipal': 'SMPDB0005_CT44', 'Mountain Grove Municipal': 'SMPDB0005_CT44', 
    'Mansfield Municipal': 'SMPDB0005_CT44', 'Associate Division Wright': 'SMPDB0005_CT44', 'Wright Circuit Court': 'SMPDB0005_CT44',
    'Adair': 'SMPDB0004_CT02', 'Andrew': 'CT05', 'Atchison': 'SMPDB0001_CT04', 'Audrain': 'CT12', 'Barton': 'SMPDB0004_CT28',
    'Bates': 'SMPDB0005_CT27', 'Benton': 'SMPDB0005_CT30', 'Bollinger': 'SMPDB0001_CT32', 'Boone': 'CT13', 'Buchanan': 'CT05', 'Butler': 'SMPDB0004_CT36',
    'Caldwell': 'SMPDB0005_CT43', 'Callaway': 'CT13', 'Camden': 'SMPDB0004_CT26', 'Cape Girardeau': 'SMPDB0001_CT32', 'Carroll': 'CT08',
    'Carter': 'SMPDB0005_CT37', 'Cass': 'CT17', 'Cedar': 'SMPDB0004_CT28', 'Chariton': 'SMPDB0001_CT09', 'Christian': 'CT38', 'Clark': 'SMPDB0004_CT01',
    'Clay': 'SMPDB0001_CT07', 'Clinton': 'SMPDB0005_CT43', 'Cole': 'SMPDB0004_CT19', 'Cooper': 'CT18', 'Crawford': 'SMPDB0005_CT42', 'Dade': 'SMPDB0004_CT28',
    'Dallas': 'SMPDB0005_CT30', 'Daviess': 'SMPDB0005_CT43', 'DeKalb': 'SMPDB0005_CT43', 'Dent': 'SMPDB0005_CT42', 'Douglas': 'SMPDB0005_CT44', 'Dunklin': 'SMPDB0001_CT35',
    'Franklin': 'SMPDB0004_CT20', 'Gasconade': 'SMPDB0004_CT20', 'Gentry': 'SMPDB0001_CT04', 'Greene': 'CT31', 'Grundy': 'SMPDB0001_CT03', 'Harrison': 'SMPDB0001_CT03', 'Harrison County Circuit Court': 'SMPDB0001_CT03',
    'Henry': 'SMPDB0005_CT27', 'Hickory': 'SMPDB0005_CT30', 'Holt': 'SMPDB0001_CT04', 'Howard': 'SMPDB0001_CT14', 'Howell': 'SMPDB0005_CT37', 'Iron': 'SMPDB0005_CT42',
    'Jackson': 'CT16', 'Jasper': 'SMPDB0001_CT29', 'Jasper County - Joplin': 'SMPDB0001_CT29', 'Jasper County - Carthage': 'SMPDB0001_CT29', 'Jefferson': 'CT23', 'Johnson': 'CT17', 'Knox': 'SMPDB0004_CT02', 
    'Laclede': 'SMPDB0004_CT26', 'Lafayette': 'SMPDB0001_CT15', 'Lewis': 'SMPDB0004_CT02', 'Lincoln': 'SMPDB0005_CT45', 'Linn': 'SMPDB0001_CT09', 'Livingston': 'SMPDB0005_CT43', 
    'Macon': 'SMPDB0004_CT41', 'Madison': 'SMPDB0005_CT24', 'Maries County': 'SMPDB0005_CT25', 'Marion': 'SMPDB0004_CT10', 'Mercer': 'SMPDB0001_CT03',
    'Miller': 'SMPDB0004_CT26', 'Mississippi': 'SMPDB0005_CT33', 'Moniteau': 'SMPDB0004_CT26', 'Monroe': 'SMPDB0004_CT10', 'Montgomery': 'CT12', 
    'New Madrid': 'SMPDB0005_CT34', 'Nodaway': 'SMPDB0001_CT04', 'Oregon': 'SMPDB0005_CT37', 'Osage': 'SMPDB0004_CT20', 'Ozark': 'SMPDB0005_CT44',
    'Pemiscot': 'SMPDB0005_CT34', 'Perry': 'SMPDB0001_CT32', 'Pettis': 'CT18', 'Phelps County': 'SMPDB0005_CT25', 'Pike': 'SMPDB0005_CT45', 'Platte': 'SMPDB0001_CT06',
    'Polk': 'SMPDB0005_CT30', 'Pulaski': 'SMPDB0005_CT25', 'Putnam': 'SMPDB0001_CT03', 'Ralls': 'SMPDB0004_CT10', 'Randolph': 'SMPDB0001_CT14', 'Ray': 'CT08', 'Ray Circuit Division': 'CT08',
    'Carroll Circuit Division': 'CT08', 'Reynolds': 'SMPDB0005_CT42', 'Ripley': 'SMPDB0004_CT36', 'Saline': 'SMPDB0001_CT15', 'Schuyler': 'SMPDB0004_CT01', 'Scotland': 'SMPDB0004_CT01', 'Scott': 'SMPDB0005_CT33',
    'Shannon': 'SMPDB0005_CT37', 'Shelby': 'SMPDB0004_CT41', 'St. Charles': 'CT11', 'St. Clair': 'SMPDB0005_CT27', 'St. Francois': 'SMPDB0005_CT24', 'St. Louis County': 'CT21',
    'Ste. Genevieve': 'SMPDB0005_CT24', 'Stoddard': 'SMPDB0001_CT35', 'Sulivan': 'SMPDB0001_CT09', 'Taney': 'CT46', 'Texas': 'SMPDB0005_CT25', 'The City of St. Louis': 'CT22',
    'Vernon': 'SMPDB0004_CT28', 'Warren': 'CT12', 'Washington': 'SMPDB0005_CT24', 'Wayne': 'SMPDB0005_CT42', 'Webster': 'SMPDB0005_CT30', 'Worth': 'SMPDB0001_CT04', 'Wright': 'SMPDB0005_CT44',
    'SUPREME COURT OF MISSOURI': 'OSCDB0024_SUP', 'EASTERN DISTRICT CT OF APPEALS': 'SMPDB0005_EAP', 'SOUTHERN DISTRICT CT OF APPEAL': 'SMPDB0001_SAP', 'WESTERN DISTRICT CT OF APPEALS': 'SMPDB0001_WAP'
}