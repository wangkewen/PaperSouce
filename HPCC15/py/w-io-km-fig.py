import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#x=[0,2,4,6,8,10,12,14,16,18,20,22]
x=range(10)
y=[5.11, 3.95, 3.39, 2.51, 1.71, 1.24, 0.91, 0.66, 0.67, 0.66]
y1=[5.31, 4.38, 4.27, 3.92, 3.7, 3.32, 3.1, 2.77, 2.56, 2.32] 
y2=[5.31, 3.88, 3.83, 3.51, 3.29, 2.95, 2.69, 2.29, 2.06, 1.7]
y3=[5.02, 5.2, 4.84, 4.67, 4.38, 4.16, 3.92, 3.72, 3.56, 3.53]
#y4=[5.28, 4.91, 4.8, 4.3, 4.21, 3.81, 3.67, 3.37, 3.16, 2.96]
#y4=[5.16,4.81,4.69,4.19,4.12,3.74,3.59,3.28,3.10,2.89 ]
y4=[5.20   , 0.00   , 4.81   , 0.00   , 4.68   , 0.00   , 4.22   , 0.00   , 4.06   , 0.00   , 3.73   , 0.00   , 3.55   , 0.00   , 3.26   , 0.00   , 3.06   , 0.00   , 2.86   , 0.00]
y4=[y4[i] for i in range(0,len(y4),2)]
plt.axis([-0.2, 10.2, 0, 6])
plt.xticks(range(10),[2,4,6,8,10,12,14,16,18,20,22])
ax.set_xticks(x)
ax.tick_params('both',direction='in', which='both', pad=1, bottom = 'on', top = 'on', left = 'on', right = 'on', labelcolor='black')
ax.yaxis.grid(color='grey', linestyle='-', linewidth=1, alpha=0.5) 
ax.xaxis.grid(color='white', linestyle='', linewidth=1, alpha=1)

plt.plot(x,y,label='Actual',linewidth=2, color='r', marker='x', ms=15, markeredgewidth=3)
plt.plot(x,y1,label='7.5GB',linewidth=2, color='g', marker='^', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y2,label='15GB',linewidth=2, color='b', marker='o', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y3,label='1.25GB',linewidth=2, color='m', marker='s', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y4,label='2.5GB',linewidth=2, color='black', marker='+', ms=15, markeredgewidth=3)
plt.xlabel('Stage')
plt.ylabel('I/O Write (MB)',fontsize=30)
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


