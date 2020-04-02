# -*- coding:utf-8  -*-
import requests
import pandas as pd


# 百度地图API搜索
def baidu_search(query, region):
    url = 'http://api.map.baidu.com/place/v2/search?'
    output = 'json'
    ak = 'D2Yxu0kH9QRuu9daKUvy6lrVjvzB8pkD'
    # 创建数组
    array = []
    i = 0
    while True:
        print("正在爬取第" + str(i + 1) + "页！")
        uri = url + 'query=' + query + '&region=' + region + '&output=' + output + '&page_size=20&page_num=' + str(i) + '&ak=' + ak
        r = requests.get(uri)
        response_dict = r.json()
        i += 1
        results = response_dict["results"]
        if len(results) == 0:
            break
        for adr in results:
            name = adr['name']
            location = adr['location']
            lng = float(location['lng'])
            lat = float(location['lat'])
            address = adr['address']
            line = name + "," + str(lng) + "," + str(lat) + "," + address
            print(line)
            if line not in array:
                array.append(line)
    # 写入txt文件
    file = open("ShpData/data1.txt", "w", encoding='utf-8')
    for line in array:
        file.write(line + '\n')
    file.close()
    # name = []
    # lng = []
    # lat = []
    # address = []
    # for i in range(len(array)):
    #
    # print(array)
    # pf = pd.DataFrame(array, [])
    # filename = pd.ExcelWriter("test.xlsx")
    # pf.to_excel(filename, startcol=0, index=False)
    print("写入完成！")


baidu_search('喜茶', '北京市')
