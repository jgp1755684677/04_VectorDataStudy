# -*- coding:utf-8  -*-
import requests


# 百度地图API搜索
def baidu_search(query, region):
    url = 'http://api.map.baidu.com/place/v2/search?'
    output = 'json'
    ak = 'D2Yxu0kH9QRuu9daKUvy6lrVjvzB8pkD'
    # 创建数组
    array = []
    for i in range(12):
        print("正在爬取第" + str(i + 1) + "页！")
        uri = url + 'query=' + query + '&region=' + region + '&output=' + output + '&page_size=20&page_num=' + str(i) + '&ak=' + ak
        r = requests.get(uri)
        response_dict = r.json()
        results = response_dict["results"]
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
    file = open("data.txt", "w", encoding='utf-8')
    for line in array:
        file.write(line + '\n')
    file.close()
    print("写入完成！")


baidu_search('瑞幸咖啡', '上海市')
