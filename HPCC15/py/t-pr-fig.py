import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=range(13)
y=[75.61  ,  16.53  ,  14.29  ,  13.04  ,  12.81  ,  12.71  ,  12.23  ,  12.40  ,  12.46  ,  12.90  ,  12.10  ,  12.67  ,  8.99 ]
y1=[72.82  , 18.22  , 14.90  , 10.06  , 9.13   , 8.77   , 8.82   , 8.24   , 8.15   , 8.19   , 8.15   , 8.43   , 11.05 ]
y2=[96.31  , 15.63  , 12.74  , 8.21   , 8.72   , 8.10   , 8.50   , 8.40   , 8.03   , 7.93   , 7.90   , 7.92   , 8.49 ]
y3=[56.57  , 13.00  , 13.51  , 11.92  , 8.59   , 9.37   , 10.84  , 11.81  , 11.15  , 11.94  , 7.59   , 7.96   , 9.40  ]
y4=[58.58  , 12.37  , 10.91  , 8.83   , 7.75   , 8.02   , 6.54   , 7.99   , 7.24   , 7.63   , 6.63   , 6.83   , 10.22  ,]

plt.axis([-0.2, 12.2, 0, 100])
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

