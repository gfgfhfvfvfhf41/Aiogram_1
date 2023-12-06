# import requests
# from bs4 import BeautifulSoup as BS
#
# #headers = {"Chrome":"102.0.5005.62"}
# headers = {'user-agent': 'Chrome/102.0.5005.62'}
# #User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36
#
# find = input()
# url = f"https://www.google.com/search?q={find}"
# r = requests.get(url, headers=headers)
# r = BS(r.text, "html.parser")
# a = r.findAll("a")
# h3 = r.findAll("div")
# #print(a)
# print(h3)
# # r = BS(r.text, "")
# # print(r.findAll(, class_="checkbox__text", text="Красота и здоровье"))



class User:
    def __init__(self):
        self.keys = []
        self.iter = 0
        self.iter_title = 0

import requests as r
from bs4 import BeautifulSoup as bs
headers = {"user-agent":"Chrome/102.0.5005.62", "cookie":"__ddg1_=JcSFwpxgpbKHiDHpkubc; _ym_uid=1653760516276119006; _ym_d=1653760516; _ym_visorc=b; _ym_isad=2"}
#, headers=headers



req = r.get("https://www.cbr.ru/currency_base/daily/")
req = bs(req.text, "html.parser")
#print(req)
div = req.findAll("td")
b = 1
a = {}

titles = []
all = []
all_cat = {}

a[b] = User()

for key in div:
    all.append(key.text)
    if a[b].iter % 5 == 0:
        titles.append(key.text)
    elif a[b].iter % 5 != 0:
        pass
    a[b].iter = a[b].iter + 1
#print(titles)
#print(all)
iteration = 0
for i in range(len(titles)):
    all_cat[titles[iteration]] = all[:4]
    all = all[4:]
    iteration+=1
print(all)


#print(type(div[0]))
#print(div) , class_="table"