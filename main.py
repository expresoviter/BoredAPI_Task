import requests
import psycopg2
from database import *


class APIWrapper:
    def __init__(self):
        self.url = "http://www.boredapi.com/api/activity/"

    def request(self, **kwargs):
        PARAMS = kwargs
        possibleKeys = {'key', 'type', 'participants', 'price', 'minprice', 'maxprice', 'accessibility',
                         'minaccessibility', 'maxaccessibility'}
        incorrectKeys = kwargs.keys() - possibleKeys
        if len(incorrectKeys) != 0:
            print(f'{incorrectKeys} are incorrect keys.')
        R = requests.get(url=self.url, params=PARAMS)
        DATA = R.json()
        return DATA


if __name__ == "__main__":
    api = APIWrapper()
    result = api.request(type="social", participants=1)
    print(result)
    saver = ActivitySaver()
    #saver.saveActivity(result)
    saver.getLatestActivities()

