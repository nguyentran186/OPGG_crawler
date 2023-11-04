import os
import re
import time
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

from util import text2time

f = open('lol-result-prediction\data\data_crawler_1.txt', encoding='utf8')
htmlparse = f.read()
contents = BeautifulSoup(htmlparse, 'html.parser')

rank_table = contents.find('table')
rank_body = rank_table.find('tbody')
rank_items = rank_body.find_all('tr')
# for item in rank_items:
#     print('https://www.op.gg/' + item.a['href'][1:])


url='https://www.op.gg/summoners/kr/%EC%8A%A4%ED%8A%B8%EB%A0%88%EC%8A%A4%EC%9C%A0%EB%B0%9C%ED%98%91%EA%B3%A1'
res = requests.get(url).text
print(res)