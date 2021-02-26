

def parse_header(soup):
    detail_labels = soup.find_all('td', 'detailLabels')
    detail_data = soup.find_all('td', 'detailData')
    indexer = 0
    header_result = {}
    for label in detail_labels:
        if label.text.strip() != '':
            header_result[label.text.strip()] = detail_data[indexer].text.strip()
        indexer += 1

    case_header = {}
    case_header['header'] = header_result

    return case_header