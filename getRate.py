import pandas as pd
import numpy as np
import map

pd.set_option('display.max_columns', None)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
np.set_printoptions(threshold=np.inf)

place = ['top', 'jungle', 'mid', 'bottom', 'support']
top = np.genfromtxt('top.txt')
jungle = np.genfromtxt('jungle.txt')
mid = np.genfromtxt('mid.txt')
bottom = np.genfromtxt('bottom.txt')
support = np.genfromtxt('support.txt')


def get(cp1, cp2):
    v = map.cp_map[cp1]
    s = map.cp_map[cp2]
    for i in range(len(place)):
        rate = globals()[place[i]][v][s]
        print(cp1, cp2, place[i], rate)


if __name__ == "__main__":
    get('annie', 'ahri')
