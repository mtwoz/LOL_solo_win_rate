import requests
import csv
import map
import champions
from bs4 import BeautifulSoup

'''
champions = []

with open('champions.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        # print(i[0])
        champions.append(i[0])

mapOfhampion = dict(zip(champions, range(0, len(champions))))

print(mapOfhampion['zoe'])
'''

champion_url = 'https://www.op.gg/champion/' + champions.cp_dict[0] + '/statistics/top/matchup'
print(champion_url)
req = requests.get(url=champion_url)
html = req.text
div_bf = BeautifulSoup(html, features="html.parser")
# print(div_bf)
div = div_bf.find_all('div', class_='champion-matchup-champion-list')
# print(div[0])
# print("1")

opponent_bf = BeautifulSoup(str(div[0]), features='html.parser')
opponent = opponent_bf.find_all('div', class_='champion-matchup-list__champion')
# print(opponent)
# print("2")

opponent_name_bf = BeautifulSoup(str(opponent), features='html.parser')
name = opponent_name_bf.find_all('span')
rate = opponent_name_bf.find_all('span', class_='champion-matchup-list__winrate')
# print("3")
# print(opponent_name[1].string)
# print(opponent_rate[0])

# print(len(opponent_rate))
# for i in range(len(opponent_rate)):
    # print(champions[0], opponent_name[i * 2].string, opponent_rate[i].string.strip())
    # print(str(opponent_name[i].string))