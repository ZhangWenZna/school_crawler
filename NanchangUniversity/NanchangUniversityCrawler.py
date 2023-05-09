import csv
import json
import requests


def save_data(data):
    with open('./南昌大学高考志愿.csv', encoding='UTF-8', mode='a+', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(data)
    f.close()

header = {
    'user-agent': ''  # 自己填自己的
}
head = ['科类', '专业', '录取人数', '专业录取线', '参考排名']

with open('./南昌大学高考志愿.csv', encoding='utf-8-sig', mode='w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f.close()
s1 = 'https://api.eol.cn/web/api/?admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page='
s2 = '&province_id=&ranktype=&request_type=1&school_type=&size=20&top_school_id=[589]&type=&uri=apidata/api/gk/school/lists&signsafe=429e2ced223b25d694a7a8ce81f73915'
s3 = 'https://static-data.gaokao.cn/www/2.0/schoolspecialindex/2022/'
s4 = '/33/3/16/'

for i in range(1, 143):
    url = s1 + str(i) + s2
    html = requests.post(url, headers=header).text
    unicodestr = json.loads(html)
    dat = unicodestr["data"]
    dat = dat["item"]
    for j in dat:
        school = j["name"]
        schoolid = j["school_id"]
        province_name = j["province_name"]
        print(school)
        for k in range(1, 10):
            urll = s3 + str(schoolid) + s4 + str(k) + '.json'
            htmll = requests.get(urll, headers=header).text
            unicode = json.loads(htmll)
            try:
                da = unicode["data"]
            except:
                break
            da = da["item"]
            for w in da:
                sc = w["min"]
                min_section = w["min_section"]
                spname = w["spname"]
                sp_info = w["sp_info"]
                tap = (province_name, school, spname, sc, min_section, sp_info)
                save_data(tap)
