from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the cities dataset
ds = pd.read_csv("iran_cities.csv")

# Create the figure and map
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(llcrnrlon=40.,llcrnrlat=20., urcrnrlon=70.,urcrnrlat=45.,
            rsphere=(6378137.00,6356752.3142), resolution='l',
            projection='merc', lat_0=40., lon_0=50., lat_ts=20.)

m.drawcoastlines()
m.fillcontinents(color='lightgray', lake_color='lightblue')
m.drawcountries()
m.drawstates()

# Convert lat/lon to map projection coords
x, y = m(ds["lon"].values, ds["lat"].values)

# Normalize population for size scaling (adjust the multiplier as needed)
sizes = ds["population"] / ds["population"].max() * 1000  # scaled sizes

# Plot with scatter, scaling size by population
m.scatter(x, y, marker='o', c='red', s=sizes, alpha=0.7, edgecolor='k', zorder=5)

# Add city labels
for i, city in enumerate(ds["city"]):
    plt.text(x[i]+10000, y[i]+10000, city, fontsize=9)

ax.set_title('Major Iranian Cities by Population')
plt.show()
