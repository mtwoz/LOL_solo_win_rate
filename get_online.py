import requests
from bs4 import BeautifulSoup


def get_rate_online(cp1, cp2, pl):
    champion_url = 'https://www.op.gg/champion/' + cp1 + '/statistics/' + pl + '/matchup/'
    print(champion_url)
    req = requests.get(url=champion_url)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    div = div_bf.find_all('div', class_='champion-matchup-champion-list')

    target_bf = BeautifulSoup(html, features='html.parser')
    target = target_bf.find_all('div', class_='champion-matchup-list__champion')

    opponent_name_bf = BeautifulSoup(str(target), features='html.parser')
    name = opponent_name_bf.find_all('span')
    rate = opponent_name_bf.find_all('span', class_='champion-matchup-list__winrate')

    # print(name[0].string)

    for i in range(len(name)):
        if name[i].string.lower().replace(' ', '').replace('.', '').replace('\'', '').replace('&', '').replace('willump', '') == cp2:
            # print(rate[i].string)
            return float(rate[i].string.strip().strip('%'))





if __name__ == "__main__":
    a = get_rate_online('aatrox', 'camille', 'top')
    print(a)
