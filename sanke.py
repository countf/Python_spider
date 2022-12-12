import requests
from lxml import etree
from flask import Flask,jsonify
if __name__ =="__main__":
    sanxia_tiche=Flask(__name__)
    sanxia_tiche.config['JSON_AS_ASCII'] = False

    session=requests.Session()
    url ='本校体育测试网址'
    user_agent={
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }


    page_data01 = {
        '姓名:': 123,
        '学籍号:': 123,
        '身份证号:': 123,
        '测试年度:': 123,
        '性别:': 123,
        '出生日期:': 123,
        '生 源 地:': 123,
        '学校:': 123,
        '附属学校:': 123,
        '综合得分:': 123,
        '学校排名占比:': 123,
        '学院排名占比:': 123,
    }
    page02_list = []


    def top01(password,username,year):
        password = password
        username = username
        year = year
        data = {
            'password': password,
            'username': username,
        }
        session.post(url=url, headers=user_agent, data=data)

        url02 = '本校体育测试网址'

        url03 = '本校体育测试网址' % (
            year)

        page = session.get(url=url03, headers=user_agent).text

        page_etree = etree.HTML(page)

        page_data_name = page_etree.xpath('//span[@id="StuName"]/text()')[0]
        page_data01['姓名:'] = page_data_name

        page_data_StuNo = page_etree.xpath('//span[@id="StuNo"]/text()')[0]
        page_data01['学籍号:'] = page_data_StuNo

        page_data_IDCard = page_etree.xpath('//span[@id="IDCard"]/text()')[0]
        page_data01['身份证号:'] = page_data_IDCard

        page_data_TestYear = page_etree.xpath('//span[@id="TestYear"]/text()')[0]
        page_data01['测试年度:'] = page_data_TestYear

        page_data_Sex = page_etree.xpath('//span[@id="Sex"]/text()')[0]
        page_data01['性别:'] = page_data_Sex

        page_data_Birthday = page_etree.xpath('//span[@id="Birthday"]/text()')[0]
        page_data01['出生日期:'] = page_data_Birthday

        page_data_AreaCode = page_etree.xpath('//span[@id="AreaCode"]/text()')[0]
        page_data01['生 源 地:'] = page_data_AreaCode

        page_data_SchoolName = page_etree.xpath('//span[@id="SchoolName"]/text()')[0]
        page_data01['学校:'] = page_data_SchoolName

        page_data_GroupName = page_etree.xpath('//span[@id="GroupName"]/text()')[0]
        page_data01['附属学校:'] = page_data_GroupName

        page_data_TotalScore = page_etree.xpath('//span[@id="TotalScore"]/text()')[0]
        page_data01['综合得分:'] = page_data_TotalScore

        page_data_Label4 = page_etree.xpath('//span[@id="Label4"]/text()')[0]
        page_data01['学校排名占比:'] = page_data_Label4

        page_data_Label5 = page_etree.xpath('//span[@id="Label5"]/text()')[0]
        page_data01['学院排名占比:'] = page_data_Label5

        page02_list.append(page_data01)
        page_data02 = {
            '测试年度': 123,
            '项目编号': 123,
            '项目名称': 123,
            '项目成绩': 123,
            '单位': 123,
            '项目得分': 123,
            '等级评价': 123,
            '测试时间': 123,

        }

        page_data02_list = [
            '测试年度',
            '项目编号',
            '项目名称',
            '项目成绩',
            '单位',
            '项目得分',
            '等级评价',
            '测试时间', ]



        for data02_num in range(0, 8):
            list_td = page_etree.xpath('//tbody/tr[@id="tcRadGrid_ctl00__%d"]/td' % (data02_num))
            i = 0
            for td in list_td:
                page_data02[page_data02_list[i]] = td.xpath('./text()')[0]
                i += 1
            page02_list.append(page_data02)

    home={
        '测试':'http://127.0.0.1:5000/top/密码/学号/学年',
        '参数':{'默认':'http://127.0.0.1:5000/top/',
              '密码，身份证后六位':'密码',
              '学号':'学号',
              '学年':'学年'
              },
        '缓存清理':'http://127.0.0.1:5000/clear',

    }
    def clear01():
        page02_list.clear()
        return

    @sanxia_tiche.route('/')
    def hello():
        return jsonify(home)

    @sanxia_tiche.route('/top/<password>/<username>/<int:year>',methods=['GET'])
    def top(password,username,year):
        top01(password,username,year)
        return jsonify(page02_list)

    @sanxia_tiche.route('/clear')
    def clear():
        clear01()
        return jsonify(data='数据清除完毕')

    # @sanxia_tiche.route('/bottom',methods=['GET'])
    # def bottom():
    #     return jsonify(page02_list)

    sanxia_tiche.run(host='0.0.0.0')

