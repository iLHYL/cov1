import json
import time

import requests
from selenium.webdriver import Chrome,ChromeOptions

def get_tencent_data():
    """
    :return: 返回历史数据和当日详情数据
    """
    url_curruntday = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    url_history = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    # headers = {
    #     "User - Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    # }
    r_today = requests.get(url_curruntday)
    r_history = requests.get(url_history)
    data_t = json.loads(r_today.text)
    data_h = json.loads(r_history.text)
    data_today = json.loads(data_t["data"])
    data_history = json.loads(data_h["data"])
    # print(data_history)
    # print(data_today)
    history = {}

    for i in data_history['chinaDayList']:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)   # 改变时间格式以便存入数据库
        confirm = i["confirm"]
        suspect = i["suspect"]
        dead = i["dead"]
        heal = i["heal"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}

    for i in data_history["chinaDayAddList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式以便存入数据库
        confirm = i["confirm"]
        suspect = i["suspect"]
        dead = i["dead"]
        heal = i["heal"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    china_details = []   #当日详情数据
    update_time = data_today["lastUpdateTime"]
    data_country = data_today["areaTree"]
    data_province = data_country[0]["children"]
    for pro_infos in data_province:
        province = pro_infos["name"]
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm_add = city_infos["today"]["confirm"]
            confirmCuts_add = city_infos["today"]["confirmCuts"]
            confirm_total = city_infos["total"]["confirm"]
            suspect_total = city_infos["total"]["suspect"]
            dead_total = city_infos["total"]["dead"]
            heal_total = city_infos["total"]["heal"]
            china_details.append([update_time,province,city,confirm_add,confirmCuts_add,confirm_total,suspect_total,dead_total,heal_total])

    # forien_detials = []   #国外详情,和真实数据有出入，暂做保留
    # for forien_infos in data_today["areaTree"][1:]:
    #     country_name = forien_infos["name"]
    #     confirm_add = forien_infos["today"]["confirm"]
    #     confirm_total = forien_infos["total"]["confirm"]
    #     suspect_total = forien_infos["total"]["suspect"]
    #     dead_total = forien_infos["total"]["dead"]
    #     heal_total = forien_infos["total"]["heal"]
    #     forien_detials.append([update_time,country_name,confirm_add,confirm_total,suspect_total,dead_total,heal_total])
    # # print(forien_detials)
    return history,china_details #,forien_detials

# a = get_tencent_data()[1]
# print(a)

#获取百度热搜数据
def get_baidu_hot():
    url = "https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"
    #设置浏览器无头模式
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    browser = Chrome(executable_path='chromedriver.exe',options = option)
    browser.get(url)

    #模拟点击更多按钮
    more_button = browser.find_element_by_xpath('//*[@id="ptab-0"]/div/div[2]/section/div')
    more_button.click()
    time.sleep(1)
    res = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[2]/section/a/div/span[2]')
    context = []
    for i in res:
        context.append(i.text)
    # print(context)
    return context
