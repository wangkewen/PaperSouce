import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=range(2)
y=[214,      17]
y1=[188    , 31 ]
y2=[213    , 13 ]
y3=[175    , 19 ]
y4=[205    , 10]
plt.axis([-0.2, 1.2, 0, 250])
ax.set_xticks(x)
ax.tick_params('both',direction='in', which='both', pad=1, bottom = 'on', top = 'on', left = 'on', right = 'on', labelcolor='black')
ax.yaxis.grid(color='grey', linestyle='-', linewidth=1, alpha=0.5) 
ax.xaxis.grid(color='white', linestyle='', linewidth=1, alpha=1)
#ax.set_xticklabels( [-20, 0, 20，40, 80, 120, 160, 200, 400, 600, 800, 1000, 3000, 5000], fontproperties=font)
plt.plot(x,y,label='Actual',linewidth=2, color='r', marker='x', ms=15, markeredgewidth=3)
plt.plot(x,y1,label='7.5GB',linewidth=2, color='g', marker='^', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y2,label='15GB',linewidth=2, color='b', marker='o', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y3,label='1.25GB',linewidth=2, color='m', marker='s', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y4,label='2.5GB',linewidth=2, color='black', marker='+', ms=15, markeredgewidth=3)
plt.xlabel('Stage')
plt.ylabel('Time (s)',fontsize=30)
#plt.title('Stage Actual time VS predict time',fontsize=40)
#plt.xticks(index + bar_width, range(2),fontsize=30)
#plt.ylim(0,40)
plt.rcParams['font.size'] = 30 
#plt.rc('ytick', labelsize=10)
#ax.get_yticklabels().set_fontsize(30)
plt.legend(fontsize=30,frameon=False,labelspacing=0,columnspacing=0,borderpad=0) 

#plt.tight_layout()

#plt.grid(True,which='both', color='0.0')
plt.show()

