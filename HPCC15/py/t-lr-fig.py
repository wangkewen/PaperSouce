import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=range(10)
y=[156.11 ,  1.53   ,  1.37   ,  1.32   ,  1.31   ,  1.31   ,  1.30   ,  1.24   ,  1.24   ,  1.24  ]
y1=[149.38 , 1.59   , 1.66   , 1.43   , 1.43   , 1.38   , 1.39   , 1.36   , 1.36   , 1.41  ]
y2=[169.95 , 1.33   , 1.34   , 1.38   , 1.25   , 1.21   , 1.20   , 1.29   , 1.15   , 1.12  ]
y3=[148.85 , 1.37   , 1.67   , 1.48   , 1.50   , 1.46   , 1.49   , 1.46   , 1.53   , 1.48  ]
y4=[164.49 , 0.96   , 1.14   , 1.23   , 1.24   , 1.15   , 1.04   , 1.12   , 1.06   , 1.02]

plt.axis([-0.2, 9.2, 0, 180])
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


