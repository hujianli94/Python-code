import requests
from bs4 import BeautifulSoup
import configparser
import re, math, time
from Insql import *
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    'Host':'search.51job.com',
    'Upgrade-Insecure-Requests': '1'
}

# 获取城市的城市编号
def get_city_code():
    url = 'https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js'
    r = requests.get(url)
	# 字符串转换字典
    city_dict = eval(r.text.split('=')[1].split(';')[0])
	# 字典的键值互换
    city_dict = {v : k for k, v in city_dict.items()}
    return city_dict

# 获取职位的总页数，参数city_code是城市编号，keyword是职位关键字
def get_pageNumber(city_code, keyword):
    url = 'https://search.51job.com/list/'+str(city_code)+',000000,0000,00,9,99,'+str(keyword)+',2,1.html'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content.decode('gbk'), 'html5lib')
    find_page = soup.find('div', class_='rt').getText()
    temp = re.findall(r"\d+\.?\d*", find_page)
    if temp:
        pageNumber = math.ceil(int(temp[0])/50)
        return pageNumber
    else:
        return 0

# 爬取职位详情页的数据，参数url是职位详情页的链接
def get_info(url):
    temp_dict = {}
    if 'https://jobs.51job.com' in url:
        r = requests.get(url, headers=headers)
        time.sleep(1.5)
        soup = BeautifulSoup(r.content.decode('gbk'), 'html5lib')
        # 职位ID
        temp_dict['job_id'] = url.split('.html')[0].split('/')[-1]
        # 企业名
        temp_dict['company_name'] = soup.find('a', class_='catn').getText().strip()
        # 企业类型、规模、经营范围
        com_tag = soup.find('div', class_='com_tag').find_all('p')
        for i in com_tag:
            if 'i_flag' in str(i):
                temp_dict['company_type'] = i.getText()
            if 'i_people' in str(i):
                temp_dict['company_scale'] = i.getText()
            if 'i_trade' in str(i):
                temp_dict['company_trade'] = i.getText()
        # 职位名称
        temp_dict['job_name'] = soup.find('h1').getText().strip()
        # 职位薪资
        temp_dict['job_pay'] = soup.find('div', class_='cn').find('strong').getText().strip()
        # 职位要求：工龄、招聘人数、发布日期、学历要求
        msgltype = soup.find('p', class_='msg ltype').getText().split('|')
        education = ['初中', '中专', '中技', '大专', '高中', '本科', '硕士', '博士']
        if msgltype:
            for i in msgltype:
                if '经验' in i.strip():
                    temp_dict['job_years'] = i.strip()
                elif '人' in i.strip():
                    temp_dict['job_member'] = i.strip()
                elif '发布' in i.strip():
                    temp_dict['job_date'] = i.strip()
                elif i.strip() in education:
                    temp_dict['job_education'] = i.strip()
        # 企业福利待遇
        t1 = soup.find('div', class_='t1').find_all('span')
        welfare = []
        for i in t1:
            welfare.append(i.getText().strip())
        temp_dict['company_welfare'] = '/'.join(welfare)
        # 上班地点
        bmsg = soup.find('div', class_='bmsg inbox')
        if bmsg:
            if bmsg.find('p', class_="fp"):
                temp_dict['job_location'] = bmsg.find('p', class_="fp").getText().strip()
        # 职位的工作描述
        find_describe = soup.find('div', class_='bmsg job_msg inbox')
        temp = str(find_describe).split('<div class="mt10">')[0]
        Mysoup = BeautifulSoup(temp, 'html5lib')
        temp_dict['job_describe'] = Mysoup.getText().strip()
        # 招聘来源
        temp_dict['recruit_sources'] = '前程无忧'
        return temp_dict


# 遍历每一页的职位信息
def get_page(keyword, pageNumber):
    for p in range(int(pageNumber)):
        url = 'https://search.51job.com/list/' + str(city_code) + ',000000,0000,00,9,99,' + str(keyword) + ',2,' + str(
            p + 1) + '.html'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content.decode('gbk'), 'html5lib')
        find_p = soup.find_all('p', class_=re.compile('t1'))
        # 进入职位详情页获取数据
        for i in find_p:
            try:
                info_dict = None
                print(i.find('a')['href'])
                url = i.find('a')['href']
                info_dict = get_info(url)
                # 入库处理
                if info_dict:
                    insert_db(info_dict)
            except Exception as e:
                print(e)
                time.sleep(5)


if __name__=='__main__':
    # 读取同一路径的配置文件
    cf = configparser.ConfigParser()
    cf.read("51job.conf")
    keyword = str(cf.get('51job', 'keyword')).split(',')
    city = str(cf.get('51job', 'city')).split(',')

    # 程序的运行方式
    for c in city:
        # 获取城市编号
        city_code = get_city_code()[c]
        for k in keyword:
            # 获取总页数
            pageNumber = get_pageNumber(city_code, k)
            # 遍历总页数
            get_page(k, pageNumber)