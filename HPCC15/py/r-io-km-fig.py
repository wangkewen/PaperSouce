import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#x=[1,3,5,7,9,11,13,15,17,19,21]
x=range(10)
y=[4.68, 3.62, 3.11, 2.3, 1.56, 1.14, 0.83, 0.6, 0.61, 0.6]
y1=[4.88, 3.81, 3.71, 3.7, 3.19, 2.97, 2.86, 2.45, 2.33, 1.87] 
y2=[4.86, 3.7, 3.54, 3.22, 3.08, 2.74, 2.55, 2.25, 1.81, 1.55]
y3=[2.44, 2.5, 2.27, 2.3, 2.03, 2.07, 1.89, 1.85, 1.53, 1.78]
#y4=[2.57, 2.51, 2.08, 1.92, 2.28, 2.03, 1.74, 1.5, 1.42, 1.34]
#y4=[3.84,3.52,3.46, 3.11, 3.05 , 2.73, 2.64, 2.41, 2.30, 2.14] 
y4=[4.28   , 0.00   , 3.94   , 0.00   , 3.63   , 0.00   , 3.49   , 0.00   , 3.33   , 0.00   , 3.05   , 0.00   , 2.90   , 0.00   , 2.68   , 0.00   , 2.56   , 0.00   , 2.34  ]
y4=[y4[i] for i in range(0,len(y4),2)]
plt.axis([-0.2, 10.2, 0, 6])
plt.xticks(range(10),[3,5,7,9,11,13,15,17,19,21])
ax.set_xticks(x)
ax.tick_params('both',direction='in', which='both', pad=1, bottom = 'on', top = 'on', left = 'on', right = 'on', labelcolor='black')
ax.yaxis.grid(color='grey', linestyle='-', linewidth=1, alpha=0.5) 
ax.xaxis.grid(color='white', linestyle='', linewidth=1, alpha=1)

plt.plot(x,y,label='Actual',linewidth=2, color='r', marker='x', ms=15, markeredgewidth=3)
plt.plot(x,y1,label='7.5GB',linewidth=2, color='g', marker='^', ms=12, fillstyle='none', markeredgewidth=3)
plt.plot(x,y2,label='15GB',linewidth=2, color='b', marker='o', ms=12, fillstyle='none', markeredgewidth=3)
plt.plot(x,y3,label='1.25GB',linewidth=2, color='m', marker='s', ms=12, fillstyle='none', markeredgewidth=3)
plt.plot(x,y4,label='2.5GB',linewidth=2, color='black', marker='+', ms=15, markeredgewidth=3)
plt.xlabel('Stage')
plt.ylabel('I/O Read (MB)',fontsize=30)
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


