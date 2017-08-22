import requests
from bs4 import BeautifulSoup
import datetime

def get_url(cate):
    url = 'http://jwc.seu.edu.cn/' + select_cate(cate) + '/list'
    return url

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

def get_page(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    em = soup.find('em', attrs={'class':'all_count'}).text
    em = int(em)
    if em % 14 is 0:
        page = em // 14
    else:
        page = em // 14 + 1
    return page

def select_cate(cate):
    category = ''
    if cate is '1':
        category = '9961'   # 教务管理
    elif cate is '2':
        category = '10018'  # 学籍管理
    elif cate is '3':
        category = '10107'  # 国际交流
    elif cate is '4':
        category = '10097'  # 课外研学
    return category

def show_me_all(cate):
    url = get_url(cate) + '.htm'
    page = get_page(url)
    for j in range(1, page):
        res = get_url_complete(j, cate)
        for i in res:
            print(i[0], ' ', i[1], ' ',i[2])
    print("请输入类别选择：")
    cate = input()
    return cate

def get_url_complete(j, cate):
    pages = str(j)
    if j > 10:
        url = get_url(cate) + pages + '.psp'
    else:
        url = get_url(cate) + pages + '.htm'
    html = get_html(url)
    res = parse_html(html)
    return res

def show_me_part(cate, month):
    now = datetime.datetime.now()
    c_year = int(now.strftime('%Y'))
    c_mon = int(now.strftime('%m'))
    flag = 0
    url = get_url(cate) + '.htm'
    page = get_page(url)
    for j in range(1, page):
        res = get_url_complete(j, cate)
        for i in res:
            year, mon = int(i[0][0:4]), int(i[0][5:7])
            if (c_year - year) * 12 + (c_mon - mon) <= month:
                print(i[0], ' ', i[1], ' ', i[2])
            else:
                flag = 1
                break
        if flag == 1:
            break
    print("请输入类别选择：")
    cate = input()
    
    return cate

def main():
    print("功能：\n1：全查（可能意义不大。。。）\n2：根据年份筛选(2017)")
    print("请输入选择")
    choice = input()
    print("类别：\n1：教务管理\n2：学籍管理\n3：国际交流\n4：课外研学\nexit：退出")
    print("请输入类别选择：")
    cate = input()
    while cate != 'exit':
        if choice is '2':
            print("请输入需要几个月内的公告：")
            print("1推荐2个月，2请随意操作，3推荐12个月，4推荐6个月")
            month = int(input())
            cate = show_me_part(cate, month)
        else:
            cate = show_me_all(cate)
    exit(0)

if __name__ == '__main__':
    main()