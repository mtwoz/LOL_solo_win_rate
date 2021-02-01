from wxpy import *
import numpy as np
import pandas as pd
import map
import get_online


pd.set_option('display.max_columns', None)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
np.set_printoptions(threshold=np.inf)

place = ['top', 'jungle', 'mid', 'bottom', 'support']
top = np.genfromtxt('./data/top.txt')
jungle = np.genfromtxt('./data/jungle.txt')
mid = np.genfromtxt('./data/mid.txt')
bottom = np.genfromtxt('./data/bottom.txt')
support = np.genfromtxt('./data/support.txt')


bot = Bot()

fa = bot.friends().search('K哥')[0]


@bot.register()
def just_print(msg):
    print(msg)
    words = msg.text.split(' ')
    print(words)
    if words[0] =='R':
        v = map.cp_map[words[1]]
        s = map.cp_map[words[2]]
        for i in range(len(place)):
            rate = globals()[place[i]][v][s]
            # print(cp1, cp2, place[i], rate)
            # return '{}, {}, {}, {}'.format(words[1], words[2], place[i], rate)
            rep = words[1] + ' ' + words[2] + ' ' + place[i] + ' ' + str(rate)
            msg.reply(rep)
    if words[0] == 'O':
        rep = get_online.get_rate_online(words[1], words[2], words[3])
        print(rep)
        msg.reply(rep)

# rate()
embed()
