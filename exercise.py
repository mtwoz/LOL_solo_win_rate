import requests
import json
from bs4 import BeautifulSoup


def getTranslate(word):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    fromData = {
        'i': word,
        'from': 'en',
        'to': 'zh-CHS',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '16119123460078',
        'sign': '054f26e1f6046a30fcb90fb4dfe9b2e6',
        'lts': '1611912346007',
        'bv': '8cdcf2f22cfb09d980351a86ccd10374',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    response = requests.post(url, data=fromData)

    content = json.loads(response.text)
    print(content)
    # print(content['translateResult'][0][0]['tgt'])


def novel():
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', class_='listmain')
    # print(div[0])
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        print(each.string, server + each.get('href'))