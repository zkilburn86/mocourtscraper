from datetime import datetime, timedelta
import time
from scrapinghub import ScrapinghubClient
from mocourtscraper.creds import SHUB_API_KEY
from mocourtscraper.constants.search_options import COURT_IDS


CLIENT = ScrapinghubClient(SHUB_API_KEY)
PROJECT = CLIENT.get_project(503874)

CASE_TYPE = 'Criminal'
SPIDER = 'cases_search'
###stopped at CT11 02/19/2020###
skip = [
    'Supreme Court',
    'Eastern Appellate',
    'Southern Appellate',
    'Western Appellate',
    'Fine Collection Center',
    '1st Judicial Circuit (Clark, Schuyler & Scotland Counties)',
    '2nd Judicial Circuit (Adair, Knox & Lewis Counties)',
    '3rd Judicial Circuit (Grundy, Harrison, Mercer & Putnam Counties)',
    '4th Judicial Circuit (Atchison, Gentry, Holt, Nodaway & Worth Counties)',
    '5th Judicial Circuit (Andrew & Buchanan Counties)',
    '6th Judicial Circuit (Platte County)',
    '7th Judicial Circuit (Clay County)',
    '8th Judicial Circuit (Carroll & Ray Counties)'
]

for court in COURT_IDS.keys():
    if court not in skip:
        court_id = COURT_IDS.get(court)
        print(court_id)

        current_date = datetime(2020, 1, 1)
        end_date = datetime(2021, 1, 1)

        while current_date < end_date:

            job_args = {
                'court_id': court_id,
                'start_date': current_date.strftime('%m/%d/%Y'),
                'case_type': CASE_TYPE
            }
            print(job_args['start_date'])
            PROJECT.jobs.run(SPIDER, units=1, job_args=job_args, add_tag=['2020','missouri','criminal'])
            current_date = current_date + timedelta(days=7)