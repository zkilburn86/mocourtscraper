from datetime import datetime, timedelta
import time
from scrapinghub import ScrapinghubClient
from mocourtscraper.creds import SHUB_API_KEY

CLIENT = ScrapinghubClient(SHUB_API_KEY)
PROJECT = CLIENT.get_project(503874)
COURT_ID = 'SMPDB0004_CT02'
CASE_TYPE = 'Criminal'
SPIDER = 'cases_search'

current_date = datetime(2020, 1, 1)
end_date = datetime(2021, 1, 1)

while current_date < end_date:

    job_args = {
        'court_id': COURT_ID,
        'start_date': current_date.strftime('%m/%d/%Y'),
        'case_type': CASE_TYPE
    }
    print(job_args['start_date'])
    PROJECT.jobs.run(SPIDER, units=4, job_args=job_args)
    current_date = current_date + timedelta(days=7)
    time.sleep(1)