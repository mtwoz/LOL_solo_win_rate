import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

import map
import champions

pd.set_option('display.max_columns', None)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
np.set_printoptions(threshold=np.inf)

flag = True
rate = []
name = []
place = ['top', 'jungle', 'mid', 'bottom', 'support']
data_top = np.zeros((300, 300))
data_jungle = np.zeros((300, 300))
data_mid = np.zeros((300, 300))
data_bottom = np.zeros((300, 300))
data_support = np.zeros((300, 300))


def getOpponent(cp, pl):
    global flag
    global rate
    global name

    champion_url = 'https://www.op.gg/champion/' + cp + '/statistics/' + pl + '/matchup'
    print(champion_url)
    req = requests.get(url=champion_url)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    div = div_bf.find_all('div', class_='champion-matchup-champion-list')
    if len(div) == 0:
        flag = False
        return
    else:
        flag = True

    opponent_bf = BeautifulSoup(str(div[0]), features='html.parser')
    opponent = opponent_bf.find_all('div', class_='champion-matchup-list__champion')

    opponent_name_bf = BeautifulSoup(str(opponent), features='html.parser')
    name = opponent_name_bf.find_all('span')
    rate = opponent_name_bf.find_all('span', class_='champion-matchup-list__winrate')

    # for i in range(len(rate)):
    #     print(champions[0], name[i * 2].string, rate[i].string.strip())
    # print(str(opponent_name[i].string))


def write_data(n, m, pl, val):
    globals()['data_'+pl][n][m] = val


def save_data():
    np.savetxt('./data/top.txt', data_top, fmt='%.2f')
    np.savetxt('./data/jungle.txt', data_jungle, fmt='%.2f')
    np.savetxt('./data/mid.txt', data_mid, fmt='%.2f')
    np.savetxt('./data/bottom.txt', data_bottom, fmt='%.2f')
    np.savetxt('./data/support.txt', data_support, fmt='%.2f')


if __name__ == "__main__":
    # print(float(opponent.opponent_rate[0].string.strip().strip('%')))

    print(len(champions.cp_dict))

    # for i in range(5):
    for i in range(len(champions.cp_dict)):
        v = map.cp_map[champions.cp_dict[i]]
        for j in range(len(place)):
            getOpponent(champions.cp_dict[i], place[j])
            if not flag:
                continue
            print(champions.cp_dict[i])
            for k in range(len(rate)):
                s = map.cp_map[name[k * 2].string.lower().replace(' ', '').replace('.', '').replace('\'', '').replace('&', '').replace('willump', '')]
                win_rate = float(rate[k].string.strip().strip('%'))
                # data_top[v][] = win_rate
                # data_top[s][v] = 100.00 - win_rate
                # print(name[k * 2].string.lower())
                # print(v, s, data_top[v][s])
                write_data(v, s, place[j], win_rate)
                write_data(s, v, place[j], 100.00-win_rate)

    save_data()
