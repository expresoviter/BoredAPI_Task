import requests


class APIWrapper:
    def __init__(self):
        self.url = "http://www.boredapi.com/api/activity/"

    def request(self, kwargs):
        PARAMS = dict()
        for i in kwargs:
            if not kwargs[i] is None:
                PARAMS[i]=kwargs[i]
        possibleKeys = {'key', 'type', 'participants', 'price', 'minprice', 'maxprice', 'accessibility',
                         'minaccessibility', 'maxaccessibility'}
        incorrectKeys = kwargs.keys() - possibleKeys
        if len(incorrectKeys) != 0:
            print(f'{incorrectKeys} are incorrect keys.')
        R = requests.get(url=self.url, params=PARAMS)
        DATA = R.json()
        return DATA

