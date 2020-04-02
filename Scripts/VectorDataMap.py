# _*_ coding:cp936 _*_
import os
import numpy as np
import matplotlib.pyplot as plt
import geopandas
from geopandas import GeoSeries


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['figure.dpi'] = 200


def legend_vector_map():
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    # ��ӡ�������������
    print(world.head())
    # ��ӡ�������ͶӰ��Ϣ
    print(world.crs)
    world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
    world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
    fig, ax = plt.subplots(1, 1)
    world.plot(column='gdp_per_cap', cmap='OrRd', ax=ax, legend=True, legend_kwds={'label': "GDP per capital", 'orientation': "horizontal"})
    plt.show()


def layers_map():
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    base = world.plot(color='grey', edgecolor='black')
    cities.plot(ax=base, marker='*', color='orange', markersize=5)
    plt.show()


def color_attr(filename):
    fig, ax = plt.subplots(figsize=(12, 12))
    specialTown = geopandas.read_file(filename)
    ax = specialTown.plot(ax=ax, column='code', cmap='Reds', legend=True, scheme='NaturalBreaks', k=5,
                          legend_kwds={'loc': 'lower left', 'title': 'GDP(100 Million CNY)', 'shadow': True})
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.show()


if __name__ == '__main__':
    # legend_vector_map()
    # layers_map()
    # ��ȡ���̸�Ŀ¼��·��
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # �����ļ�·��
    dataPath = os.path.abspath(rootPath + r'\ShpData')
    # �л�Ŀ¼
    os.chdir(dataPath)
    # ָ�������ļ�
    vector_filename = "gis_osm_transport_free_1.shp"
    color_attr(vector_filename)
