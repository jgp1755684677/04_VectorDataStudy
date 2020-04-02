# _*_ coding: cp936 _*_
import os
import pandas as pd
import matplotlib.pyplot as plt
import geopandas
from geopandas import GeoSeries
from shapely.geometry import Point

# ���������ó�SimHei������������ʾ����
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['figure.dpi'] = 200  # �ֱ���
# ���� geopandas ����ת shp ���ݲ���ͼ
# Ҫ�� EXCEL ���еľ�γ���ֶ����Ʒֱ�Ϊ��LONGITUDE,LATITUDE��
# ExcelFile���ļ���������·����


def point_to_vector(filename):
    # geopandas�Դ����ݣ�����Ҫ���ϱ��룬�������Ļ�������
    data = pd.read_excel(filename, encoding="utf-8")
    # print(Exceldata)
    # ������Ϣ
    x = data.lng
    # print(x)
    # γ����Ϣ
    y = data.lat
    # print(y)
    # ���꣬������Ϣ
    xy = [Point(xy) for xy in zip(x, y)]
    # �������ռ�����,��EXCEL��Ϣ�ͼ�����Ϣ��ֵ
    point_data_frame = geopandas.GeoDataFrame(data, geometry=xy)
    # �趨ͶӰ����ϵΪWGS84��������ϵ�����Ϊ"EPSG:4326"
    point_data_frame.crs = "EPSG:4326"
    print(point_data_frame.head())
    # ��ȡ�ļ�������������׺����
    filename_prefix = filename.split('.')[0]
    # �����������ʸ���ļ���
    vector_filename = filename_prefix + ".shp"
    # ���Shp,���ñ����ʽ���������Ļ�������
    point_data_frame.to_file(vector_filename, 'ESRI Shapefile', encoding="utf-8")
    # �ռ�������ͼ
    point_data_frame.plot(color='red')
    # ��ʾ���
    plt.show()


if __name__ == '__main__':
    # ��ȡ���̸�Ŀ¼��·��
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print('root path:' + root_path)
    # �����ļ�·��
    data_path = os.path.abspath(root_path + r'\ShpData')
    print('data path:' + data_path)
    # �л�Ŀ¼
    os.chdir(data_path)
    excel_filename = "xicha.xlsx"
    point_to_vector(excel_filename)
