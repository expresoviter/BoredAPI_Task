import requests


class APIWrapper:
    def __init__(self):
        self.url = "http://www.boredapi.com/api/activity/"

    def request(self, parameters):
        PARAMS = dict()
        for i in parameters:
            if not parameters[i] is None:
                PARAMS[i] = parameters[i]
        possibleKeys = {'key', 'type', 'participants', 'price', 'minprice', 'maxprice', 'accessibility',
                        'minaccessibility', 'maxaccessibility'}
        incorrectKeys = parameters.keys() - possibleKeys
        if len(incorrectKeys) != 0:
            print(f'{incorrectKeys} are incorrect keys.')
        R = requests.get(url=self.url, params=PARAMS)
        DATA = R.json()
        return DATA
