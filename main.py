# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json


def connect():

    headers = {
        'Authorization': 'Bearer 7d61f7b763a9c0122580e5ec18e9007862bacbc032200c8ccc4c064cff982844',
    }

    response = requests.get('https://api.youneedabudget.com/v1/budgets', headers=headers)
    d=response.json()["data"]
    print(d)
    with open("output.json", 'w') as outfile:
        json.dump(d, outfile, indent=4)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
