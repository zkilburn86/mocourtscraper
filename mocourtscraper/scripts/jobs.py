from datetime import datetime, timedelta
from scrapinghub import ScrapinghubClient
from mocourtscraper.creds import SHUB_API_KEY

CLIENT = ScrapinghubClient(SHUB_API_KEY)
PROJECT = CLIENT.get_project(503874)

jobs = PROJECT.jobs.iter(state=['finished'], spider='cases_search', tag=['2020','criminal','missouri'])

""" job_count = []
for j in jobs:
    job = PROJECT.jobs.get(j['key'])
    items = job.items.iter()
    for item in items:
        print(item)
    break """