# _*_ coding: cp936 _*_
import os
import matplotlib.pyplot as plt
import geopandas
from geopandas import GeoSeries
from fiona.crs import from_epsg
from shapely.geometry import Polygon


# 投影转换函数
def transfer_projection(df, code):
    result = df.to_crs(from_epsg(code))
    return result


# 缓冲区函数
def vector_buffer(filename, radius):
    # geopandas 打开数据，如有中文，则加上中文编码方式，如有特殊字符，如网站链接 等，则用 utf-8 方式
    vector = geopandas.read_file(filename, encoding="GB2312")
    print(vector.crs)
    # ESPG:3857:WGS 84 / Pseudo-Mercator -- Spherical Mercator, Google Maps, OpenStr eetMap, Bing, ArcGIS, ESRI
    vector_CGCS = transfer_projection(vector, 3857)
    print(vector_CGCS.head())
    print(vector_CGCS.crs)
    g = GeoSeries(vector_CGCS['geometry'])
    buffer = g.buffer(radius)
    base = vector_CGCS.plot(color='white', edgecolor='black')
    buffer.plot(ax=base, color='green')
    plt.show()
    vector_buffer = vector_CGCS.set_geometry(buffer)
    print(vector_buffer.head())
    vector_buffer.crs = "EPSG:3857"
    print(vector_buffer.crs)
    filename_prefix = filename.split('.')[0]
    buffer_vector_filename = filename_prefix+"_buffer_"+str(radius)+"m.shp"
    vector_buffer.to_file(buffer_vector_filename, 'ESRI Shapefile', encoding="utf-8")


# 叠加函数
def overlay():
    polys1 = geopandas.GeoSeries([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]), Polygon([(2, 2), (4, 2), (4, 4), (2, 4)])])
    polys2 = geopandas.GeoSeries([Polygon([(1, 1), (3, 1), (3, 3), (1, 3)]), Polygon([(3, 3), (5, 3), (5, 5), (3, 5)])])
    df1 = geopandas.GeoDataFrame({'geometry': polys1, 'df1': [1, 2]})
    df2 = geopandas.GeoDataFrame({'geometry': polys2, 'df2': [1, 2]})
    ax = df1.plot(color='red')
    df2.plot(ax=ax, color='green', alpha=0.5)
    plt.title('data')
    # 联合
    res_union = geopandas.overlay(df1, df2, how='union')
    ax = res_union.plot(alpha=0.5, cmap='tab10')
    df1.plot(ax=ax, facecolor='none', edgecolor='k')
    df2.plot(ax=ax, facecolor='none', edgecolor='k')
    plt.title('union')
    # 相交
    res_intersection = geopandas.overlay(df1, df2, how='intersection')
    ax = res_intersection.plot(alpha=0.5, cmap='tab10')
    df1.plot(ax=ax, facecolor='none', edgecolor='k')
    df2.plot(ax=ax, facecolor='none', edgecolor='k')
    plt.title('intersection')
    # 交集取反
    res_symdiff = geopandas.overlay(df1, df2, how='symmetric_difference')
    ax = res_symdiff.plot(alpha=0.5, cmap='tab10')
    df1.plot(ax=ax, facecolor='none', edgecolor='k')
    df2.plot(ax=ax, facecolor='none', edgecolor='k')
    plt.title('symmetric_difference')
    plt.show()


def interacte(shp_a,shp_b):
    df_a = geopandas.read_file(shp_a, encoding="GB2312")
    print(df_a)
    df_a = transfer_projection(df_a, 4326)
    df_b = geopandas.read_file(shp_b, encoding="utf-8")
    print(df_b)
    df_b = transfer_projection(df_b, 4326)
    ax = df_a.plot(color='white', edgecolor='black')
    df_b.plot(ax=ax, color='green', edgecolor='red', alpha=0.5)
    df_b['same'] = 'dissolveall'
    df_b_CGCS_dissolve = df_b.dissolve(by='same')
    df_b_CGCS_dissolve.plot(alpha=0.5, cmap='tab10')
    print('------------dissolve 结果---------')
    print(df_b_CGCS_dissolve.head())
    res_intersection = geopandas.overlay(df_a, df_b_CGCS_dissolve, how='intersection')
    print('-----------------------相交结果----------------------------')
    print(res_intersection)
    ax = df_a.plot(alpha=0.7, facecolor='lime')
    res_intersection.plot(ax=ax, alpha=0.5, facecolor='tomato')
    plt.title('intersection')
    plt.show()


if __name__ == '__main__':
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dataPath = os.path.abspath(rootPath + r'\ShpData')  # 数据文件路径
    os.chdir(dataPath)  # 切换目录
    # vector_filename = "xicha.shp"
    # vector_buffer(vector_filename, 500)
    # overlay()
    interacte("1diandian_buffer_500m.shp", "xicha_buffer_500m.shp")