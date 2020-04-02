from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

_map = Basemap()
_map.bluemarble()
_map.drawcountries()
_map.drawrivers(color='#87CEFA')
plt.show()

_map = Basemap(projection='ortho', lat_0=33, lon_0=100)
_map.drawmapboundary(fill_color='#0000CD')
_map.fillcontinents(color='#F4A460', lake_color='#87CEFA')
_map.drawcoastlines()
plt.show()
