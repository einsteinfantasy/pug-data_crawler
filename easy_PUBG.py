from bs4 import BeautifulSoup
import requests
while True:
    name = input('欢迎光临绝地求生大逃杀数据查询系统,请输入要查询的玩家ID(例如:Danielscates):')
    server = input('请输入玩家所在的服务器地区(as/sea/eu/sa/na/oc):')
    print('查询中...')
    try:
        a = requests.get(f'https://pubg.op.gg/user/{name}?server={server}')
    except:
        print('无法查询到数据')
    html = a.text
    soup = BeautifulSoup(html, 'lxml')
    match_list = soup.find_all('div', class_="matches-item__summary")
    i = 0
    for match in match_list:
        i += 1
        mod = match.find('div', class_="matches-item__mode").i.text.strip()
        rank = match.find('div', class_="matches-item__ranking").text.strip()
        try:
            rank_change = match.find('div', class_="matches-item__layout matches-item__layout--game-list").div.text.strip()
        except:
            rank_change = '未统计'
        kills = match.find('div', class_="matches-item__column matches-item__column--kill").div.text.strip()
        damage = match.find('div', class_="matches-item__column matches-item__column--damage").div.text.strip()
        distance = match.find('div', class_="matches-item__column matches-item__column--distance").div.text.strip()
        print(f'''{name}:的最近比赛: 第{i}场:
            比赛模式{mod}
            排名:{rank}  击杀:{kills}    造成伤害:{damage}   跑毒距离:{distance}  rank变化:{rank_change}''')
