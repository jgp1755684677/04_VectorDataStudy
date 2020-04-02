# -*- coding:utf-8  -*-
import os  # 用于路径的操作
import matplotlib.pyplot as plt  # 用于图像的显示
import geopandas  # 用于矢量文件的显示
from geopandas import GeoSeries  # 用于图像中午标签的显示


plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为 SimHei，用于中文的正常显示
plt.rcParams['figure.dpi']  # 设置分辨率


# 显示矢量文件函数
def vector_show(filename, field=None):
    # 创建空间数据
    gdf = geopandas.GeoDataFrame
    # 读取常用格式的矢量文件，如：ShapeFile、Coverage、GeoDatabase、DWG
    shp = gdf.from_file(filename, encoding='gb18030')
    # 输出属性表
    print(shp.head())
    # 矢量文件绘图
    shp.plot()
    # 不显示坐标轴
    plt.axis('off')
    # 显示图像
    plt.show()


# 主函数
if __name__ == '__main__':
    # 获取工程根目录的路径
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 打印工程根目录的路径
    print("root path:" + root_path)
    # 获取数据文件的路径
    data_path = os.path.abspath(root_path + r'\ShpData')
    # 打印数据文件的路径
    print("data path:" + data_path)
    # 切换目录
    os.chdir(data_path)
    # 矢量文件名
    vector_filename = "gis_osm_transport_free_1.shp"
    # 显示矢量文件
    vector_show(vector_filename)
