import csv
import requests
from bs4 import BeautifulSoup


cp_dict = []


def getChampionName():
    """
        use this function to get names,
        and pit these names into a csv file.
    """

    target = 'https://www.op.gg/champion/statistics'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    # div = div_bf.find_all('div', class_='champion-index__champion-item__name')
    div = div_bf.find_all('div', class_='champion-index__champion-list')
    print(div[0])
    name_bf = BeautifulSoup(str(div[0]), features="html.parser")
    name = name_bf.find_all('div', class_='champion-index__champion-item__name')
    # print(name[0].string)

    # champions = []

    for i in name:
        # champion_name.append(i.string)
        print(i.string.lower())


with open('./data/champions.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        # print(i[0])
        cp_dict.append(i[0])
