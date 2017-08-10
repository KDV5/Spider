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
        yield[
            a_s,
            href
        ]

def main():
    html = get_html('http://jwc.seu.edu.cn/9963/list.htm')
    res = parse_html(html)
    for i in res:
        print(i[0], '  ', i[1])

if __name__ == '__main__':
    main()
