# _*_ coding: cp936 _*_
import os
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
from geopandas import GeoSeries
from shapely.geometry import Point

# 将字体设置成SimHei，用于正常显示中文
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['figure.dpi'] = 200  # 分辨率
# 利用 geopandas 将点转 shp 数据并绘图
# 要求 EXCEL 表中的经纬度字段名称分别为：LONGITUDE,LATITUDE；
# ExcelFile：文件名【包含路径】


def point_to_vector(filename):
    # geopandas自带数据，后面要加上编码，否则中文会变成乱码
    data = pd.read_excel(filename, encoding="utf-8")
    # print(Exceldata)
    # 经度信息
    x = data.lng
    # print(x)
    # 纬度信息
    y = data.lat
    # print(y)
    # 坐标，几何信息
    xy = [Point(xy) for xy in zip(x, y)]
    # 定义地理空间数据,将EXCEL信息和几何信息赋值
    point_data_frame = geopandas.GeoDataFrame(data, geometry=xy)
    # 设定投影坐标系为WGS84地理坐标系，编号为"EPSG:4326"
    point_data_frame.crs = "EPSG:4326"
    print(point_data_frame.head())
    # 获取文件名【不包含后缀名】
    filename_prefix = filename.split('.')[0]
    # 输出缓冲区后矢量文件名
    vector_filename = filename_prefix + ".shp"
    # 输出Shp,设置编码格式，否则中文会有乱码
    point_data_frame.to_file(vector_filename, 'ESRI Shapefile', encoding="utf-8")
    # 空间数据制图
    point_data_frame.plot(color='red')
    # 显示结果
    plt.show()


if __name__ == '__main__':
    # 获取工程根目录的路径
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print('root path:' + root_path)
    # 数据文件路径
    data_path = os.path.abspath(root_path + r'\ShpData')
    print('data path:' + data_path)
    # 切换目录
    os.chdir(data_path)
    excel_filename = "xicha.xlsx"
    point_to_vector(excel_filename)
