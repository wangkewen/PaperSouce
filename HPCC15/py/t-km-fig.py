import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=range(22)
y=[150.59 ,  0.97   ,  5.89   ,  1.11   ,  4.09   ,  0.68   ,  3.99   ,  0.41   ,  3.96   ,  0.35   ,  3.94   ,  0.32   ,  3.97   ,  0.30   ,  3.91   ,  0.28   ,  3.87   ,  0.27   ,  3.88   ,  0.27   ,  3.90   ,  0.28   ]
y1=[154.63 , 1.97   , 10.86  , 1.06   , 7.74   , 0.66   , 5.61   , 0.48   , 5.23   , 0.52   , 5.43   , 0.42   , 5.23   , 0.41   , 4.57   , 0.47   , 5.32   , 0.31   , 4.65   , 0.37   , 4.89   , 0.44    ]
y2=[157.45 , 1.73   , 7.64   , 0.77   , 4.74   , 0.72   , 4.16   , 0.49   , 4.07   , 0.61   , 4.50   , 0.37   , 4.34   , 0.40   , 4.23   , 0.35   , 4.13   , 0.34   , 3.92   , 0.31   , 3.90   , 0.33 ]
y3=[148.08 , 2.03   , 9.84   , 0.83   , 7.21   , 0.58   , 5.59   , 0.47   , 4.86   , 0.39   , 4.86   , 0.37   , 3.25   , 0.38   , 4.42   , 0.30   , 4.65   , 0.26   , 4.09   , 0.21   , 3.35   , 0.28   ]
y4=[160.75 , 1.18   , 5.98   , 0.45   , 5.18   , 0.29   , 4.15   , 0.21   , 4.17   , 0.21   , 4.80   , 0.23   , 4.83   , 0.19   , 4.14   , 0.17   , 4.58   , 0.15   , 4.50   , 0.18   , 4.66   , 0.14   ]

plt.axis([-0.2, 21.2, 0, 180])
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

