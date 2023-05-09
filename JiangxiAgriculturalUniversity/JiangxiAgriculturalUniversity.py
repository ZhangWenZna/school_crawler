import csv
import requests
from lxml import etree
import time


def main(url):
    url_1 = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    #resp.encoding = "utf-8"
    html = resp.text
    print(html)

    data=etree.HTML(html)
    subject=data.xpath("/html/body/div[3]/div/div[2]/ul[1]/div/table/tbody/tr/td[4]")
    print(subject)
    major = data.xpath("/html/body/div[3]/div/div[2]/ul[1]/div/table/tbody/tr/td[6]")
    applicants = data.xpath("/html/body/div[3]/div/div[2]/ul[1]/div/table/tbody/tr/td[14]")
    admissionLine = data.xpath("/html/body/div[3]/div/div[2]/ul[1]/div/table/tbody/tr/td[8]")
    for s, m, a, l in zip(subject, major, applicants,admissionLine):
        csvwriter.writerow((s, m, a, l))
        print(s, m, a, l)
    print('爬取完毕')


if __name__ == '__main__':
    with open('01.csv', 'a', encoding='utf-8')as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(('科类', '专业', '录取人数', '专业录取线'))
        subject_1=["http://zs.jxau.edu.cn/index_lnlqcj.php?year=2022&province=14&kl=1","http://zs.jxau.edu.cn/index_lnlqcj.php?year=2022&province=14&kl=2","http://zs.jxau.edu.cn/index_lnlqcj.php?year=2022&province=14&kl=5","http://zs.jxau.edu.cn/index_lnlqcj.php?year=2022&province=14&kl=7"]
        for i in subject_1:
            main(i)
            time.sleep(2)
