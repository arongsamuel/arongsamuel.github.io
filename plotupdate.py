from scipy.interpolate import CubicSpline
import numpy as np
import random
import matplotlib.pyplot as plt
gps = open("park2.nmea","r",encoding='latin-1')
import time
#coordinates = [i for i in gps.readlines() if i.split(",")[0]=="$GPGGA"]
#coordinatesx = [i for i in gps.readlines() if i.split(",")[0]=="$GPVTG"]
coordinates = gps.readlines()
x_path=[]
y_path=[]
plt.ion()
for i in coordinates:
    if  i.split(",")[0]=="$GPGGA":
        x_path.append(float(i.split(",")[1]))
        y_path.append(float(i.split(",")[2]))
fig, ax = plt.subplots(figsize=(15, 8))
#line1, = ax.plot(x_path, y_path, )
#line1.set_linewidth(4)
plt.scatter(x_path, y_path, color='gray', alpha=0.3)
#line2, = ax.scatter(x_path, y_path)


for i in range(len(coordinates)-4):
    if  coordinates[i].split(",")[0]=="$GPGGA":
        #print(coordinates[i])
        x = [float(coordinates[i].split(",")[1]),float(coordinates[i+2].split(",")[1]),float(coordinates[i+4].split(",")[1])]
        y = [float(coordinates[i].split(",")[2]),float(coordinates[i+2].split(",")[2]),float(coordinates[i+4].split(",")[2])]
        cs = CubicSpline(x, y)
        new_points = np.random.uniform(low=x[1], high=x[2], size=(5,))
        #line1.set_xdata(new_points)
        #line1.set_ydata(cs(new_points))
        plt.scatter(new_points,cs(new_points), color='blue',)
        plt.draw()
        plt.show()
        plt.pause(0.00001)
        # to flush the GUI events
        print(cs(new_points))
        time.sleep(0.05)
