import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    td = soup.find("td", attrs={"valign":"top", "bgcolor":"#FFFFFF"}).find_next_sibling()
    table = td.find("table", attrs={"class":"font3"})
    trs = table.find('tr').find_next_siblings()
    for tr in trs:
        date = tr.find('div', attrs={"style": "white-space:nowrap"}).text.strip()
        a_s = tr.find('a').text.strip()
        href = 'http://jwc.seu.edu.cn' + tr.find('a').get('href')
        yield[
            date,
            a_s,
            href
        ]

def getPage(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    em = soup.find('em', attrs={'class':'all_count'}).text
    em = int(em)
    if em % 14 == 0:
        page = em // 14
    else:
        page = em // 14 + 1
    return page

"""def getUrl(cate):
    page = getPage()
    if page > 10:
        url = 'jwc.seu.edu.cn/' + select(cate) + '/list' + page + '.psp'
    else:
        url = 'jwc.seu.edu.cn/' + select(cate) + '/list' + page + '.htm'
    return url"""

def selectCate(cate):
    category = ''
    if cate == '1':
        category = '9961'   # 教务管理
    elif cate == '2':
        category = '10018'  # 学籍管理
    elif cate == '3':
        category = '10107'  # 国际交流
    elif cate == '4':
        category = '10097'  # 课外研学
    return category

def main():
    print("1：教务管理\n2：学籍管理\n3：国际交流\n4：课外研学")
    print("请输入选择：")
    cate = input()
    url = 'http://jwc.seu.edu.cn/' + selectCate(cate) + '/list.htm'
    page = getPage(url)
    for j in range(1, page):
        pages = str(j)
        if j > 10:
            url = 'http://jwc.seu.edu.cn/' + selectCate(cate) + '/list' + pages + '.psp'
        else:
            url = 'http://jwc.seu.edu.cn/' + selectCate(cate) + '/list' + pages + '.htm'
        html = get_html(url)
        res = parse_html(html)
        for i in res:
            print(i[0], ' ', i[1], ' ',i[2])

if __name__ == '__main__':
    main()