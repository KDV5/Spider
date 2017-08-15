import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    td = soup.find("td", attrs={"valign":"top", "bgcolor":"#FFFFFF"}).find_next_sibling()
    table = td.find("table", attrs={"class":"font3"})
    trs = table.find('tr').find_next_siblings()
    for tr in trs:
        a_s = tr.find('a').text.strip()
        href = 'http://jwc.seu.edu.cn' + tr.find('a').get('href')
        date = tr.find('div', attrs={"style":"white-space:nowrap"}).text.strip()
        yield[
            date,
            a_s,
            href
        ]

def main():
    print("1：教务管理\n2：学籍管理\n3：国际交流\n4：课外研学\n")
    print("请输入选择：")
    k = input()
    url = select(k)
    print(url)
    html = get_html(url)
    res = parse_html(html)
    for i in res:
        print(i[0], ' ', i[1], ' ',i[2])

def select(cate):
    url = 'http://jwc.seu.edu.cn/'
    category = ''
    if cate == '1':
        category = '9961'   # 教务管理
    elif cate == '2':
        category = '10018'  # 学籍管理
    elif cate == '3':
        category = '10107'  # 国际交流
    elif cate == '4':
        category = '10097'  # 课外研学
    url = url + category + '/list.htm'
    return url


if __name__ == '__main__':
    main()