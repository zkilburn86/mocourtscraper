from bs4 import BeautifulSoup
import pandas as pd
from mocourtscraper.utilities import case_search_spider_helper


class NoResultsError(Exception):
    pass

class ResultsTableParseError(Exception):
    pass

class TableRowParseError(Exception):
    pass

def has_results(soup):
    message_line = soup.find('td', 'messageLine')
    if message_line is None:
        return True
    else:
        return False

def get_results(soup):
    df = build_frame(soup)
    df = add_results_to_frame(soup, df)
    
    return df

def get_pagination(soup):
    result_counts = []
    result_description = soup.find('td', 'resultDescription').find_all('b')
    for result in result_description:
        try:
            result_counts.append(int(result.text.strip()))
        except ValueError:
            continue
    return result_counts

def build_frame(soup):
    headers = []
    table_headers = soup.find_all('td','header')
    for label in table_headers:
        header = label.text.replace('\xa0', '_')
        headers.append(header)

    df = pd.DataFrame(columns=headers)

    return df

def add_results_to_frame(soup, df):
    headers = list(df)
    num_of_columns = len(headers)

    all_rows = []
    all_rows.extend(soup.find_all('td', 'td1'))
    all_rows.extend(soup.find_all('td', 'td2'))
    num_of_cells = len(all_rows)

    if num_of_cells%num_of_columns != 0:
        raise ResultsTableParseError('Unable to parse results table')
    
    end_index = num_of_columns
    start_index = 0
    while end_index <= num_of_cells:
        row = all_rows[start_index:end_index]
        built_row = build_row(row, headers)
        df = df.append(
            built_row,
            ignore_index=True
        )
        start_index += num_of_columns
        end_index += num_of_columns
    
    return df

def build_row(row, headers):
    result = {}
    if len(row) != len(headers):
        raise TableRowParseError('Unable to parse table row')
    indexer = 0
    for col in headers:
        result[col] = row[indexer].text.strip()
        indexer += 1
    return result

def post_process(df):
    case_to_loc = pd.Series(df.Location.values,index=df.Case_Number).to_dict()
    case_urls = []
    for case_number in case_to_loc.keys():
        case_urls.append(
            case_search_spider_helper.build_case_url(case_number, case_to_loc[case_number])
        )
    df['Case URL'] = case_urls
    return df