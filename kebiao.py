import urllib.parse
import requests
from bs4 import BeautifulSoup
import http.cookiejar
import urllib


def get_html(data):

	url = 'http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.actionCurriculum.action'
	data = urllib.parse.urlencode(data).encode('utf-8')
	header = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept_Language': 'zh-CN,zh;1=0.8',
		'Connection': 'keep-alive',
		'Host': 'xk.urp.seu.edu.cn',
		'Referer': 'http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
		}
	req = urllib.request.Request(url,data,header)
	r = urllib.request.urlopen(req)
	print(r)
	return r

def get_data():
	data = {
		"queryStudentId": 213151320,
		"queryAcademicYear": 17-18-2
	}
	return data

def parse_html(html):
	soup = BeautifulSoup(html, 'lxml')
	tables = soup.find('table', attrs={"class": "tableline"})
	trs = tables.find('tr').find_next_siblings
	for tr in trs:
		tds = tr.find_all("td")
		yield [
			tds[0].text.strip(),
			tds[1].text.strip(),
			tds[2].text.strip(),
			tds[3].text.strip(),
			tds[4].text.strip()
		]

def main():
	data = get_data()
	html = get_html(data) 
	res = parse_html(html)
	for i in res:
		for j in range(0, 4):
			print(i[j])

if __name__ == '__main__':
	main()
