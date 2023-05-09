import csv
import requests
from lxml import etree
import time


def main():
    url = f'https://zjc.ncu.edu.cn/zszx/lnfs/9ba4f80248874172af2937017620226b.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    html = resp.text
    print(html)

    data=etree.HTML(html)
    subject=data.xpath("//html/body/div[1]/div[2]/article/div/div/table/tbody/tr/td[1]")
    print(subject)
    del subject[0]
    major = data.xpath("//html/body/div[1]/div[2]/article/div/div/table/tbody/tr/td[2]")
    applicants = data.xpath("//html/body/div[1]/div[2]/article/div/div/table/tbody/tr/td[3]")
    admissionLine = data.xpath("//html/body/div[1]/div[2]/article/div/div/table/tbody/tr/td[6]")
    ranking = data.xpath("//html/body/div[1]/div[2]/article/div/div/table/tbody/tr/td[7]")
    for s, m, a, l, r in zip(subject, major, applicants,admissionLine,ranking):
        csvwriter.writerow((s, m, a, l, r))
        print(s, m, a, l, r)
    print(f'爬取完毕')


if __name__ == '__main__':
    with open('01.csv', 'a', encoding='utf-8')as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(('科类', '专业', '录取人数', '专业录取线', '参考排名'))
        main()
