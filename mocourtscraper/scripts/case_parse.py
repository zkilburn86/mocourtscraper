from bs4 import BeautifulSoup

def parse_header(response):
    soup = BeautifulSoup(response.body, features='lxml')

    detail_labels = soup.find_all('td', 'detailLabels')
    detail_data = soup.find_all('td', 'detailData')
    indexer = 0
    header_result = {}
    for label in detail_labels:
        if label.text.strip() != '':
            header_text = label.text.strip()
            header_text = header_text.replace(' ', '_').lower()
            header_result[header_text] = detail_data[indexer].text.strip()
        indexer += 1

    case_header = {'header': header_result}

    return case_header

def parse_parties(body):
    parties_result = {}
    soup = BeautifulSoup(body, features='lxml')

    parties_result = _get_case_parties(soup)
    party_addresses = _get_party_addresses(soup)
    parties_result = _assign_addresses(parties_result, party_addresses)

    case_parties = {'parties': parties_result}
    return case_parties

def parse_charges(body):
    charges_result = {}
    case_charges = {'charges': charges_result}
    return case_charges

def _get_case_parties(soup):
    case_parties = []
    detail_separators = soup.find_all('td', 'detailSeperator')
    for detail in detail_separators:
        cell_text = detail.text.strip()
        if cell_text != '' and 'represented by' not in cell_text:
            party = ' '.join(cell_text.split())
            party_details = party.split(' , ')
            party_dict = {}
            if len(party_details) == 3:
                party_dict = {
                    'first_name': party_details[1],
                    'last_name': party_details[0],
                    'role': party_details[2]
                }
            if len(party_details) == 2:
                party_dict = {
                    'party_name': party_details[0],
                    'role': party_details[1]
                }
            case_parties.append(party_dict)
    return case_parties

def _get_party_addresses(soup):
    party_addresses = []
    detail_data = soup.find_all('td', 'detailData')
    for detail in detail_data:
        cell_text = detail.text.strip()
        if cell_text != '':
            party_addresses.append(' '.join(cell_text.split()))
    return party_addresses

def _assign_addresses(parties, party_addresses):
    position = 0
    if len(party_addresses) == len(parties):
        for address in party_addresses:
            address_detail = address.split(' Year of Birth: ')
            parties = _append_address(parties, address_detail, position)
            position += 1
    return parties

def _append_address(parties, address_detail, position):
    if len(address_detail) == 2:
        address_dict = {
            'address': address_detail[0],
            'year_of_birth': address_detail[1]
        }
        parties[position].update(address_dict)
    if len(address_detail) == 1:
        address_dict = {
            'address': address_detail[0]
        }
        parties[position].update(address_dict)
    return parties