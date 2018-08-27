import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+0.1*rect.get_width(), height+1, '%s' % height, fontsize=30)

fig, ax =plt.subplots()
#plt.subplot(121)
n_groups = 4
#time_real = (214,      17)
A_predict = (81, 97, 92, 92)
B_predict = (72, 99, 97, 97)
C_predict =(80, 89, 76, 41)
D_predict=(69, 98, 85, 46)
index = np.arange(n_groups)
print(index)
bar_width = 0.2
opacity = 1.0
#plt.axis([-0.3, 2.3, 0, 100])
plt.axis([-0.5, 4, 0, 115])
ax.yaxis.grid(color='black', linestyle='--', linewidth=1, alpha=1)
ax.xaxis.grid(color='white', linestyle='', linewidth=1, alpha=1)
ax.tick_params('both',direction='in', which='both', pad=10, bottom = 'on', top = 'on', left = 'on', right = 'on', labelcolor='black') 
#rects1 = plt.bar(index, time_real, bar_width, align='center', alpha=0.8*opacity, color='black',label= 'Actual')
rects2 = plt.bar(index , A_predict, bar_width, align='center', alpha=0.5*opacity,  color='grey',label='7.5GB',hatch='x')
rects3 = plt.bar(index + bar_width, B_predict, bar_width, align='center', alpha=opacity,color='black',label='15GB')
rects4 = plt.bar(index + 2*bar_width, C_predict, bar_width, align='center', alpha=0.2*opacity,color='black',label='1.25GB')
rects5 = plt.bar(index + 3*bar_width, D_predict, bar_width, align='center', alpha=opacity,color='grey',label='2.5GB', hatch='\\')
#autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
#plt.xlabel('Stage')
plt.ylabel('Prediction Accuracy (%)',fontsize=30)
#plt.title('Stage Actual time VS predict time',fontsize=40)
plt.xticks(1.5*bar_width+index, ('Time', 'Mem', 'I/O Write', 'I/O Read'),fontsize=30)
#plt.ylim(0,40)
plt.rcParams['font.size'] = 25 
#plt.rc('ytick', labelsize=10)
#ax.get_yticklabels().set_fontsize(30)
plt.legend(fontsize=25,frameon=False,labelspacing=0,columnspacing=0.1,borderpad=0,handletextpad=0.2,loc='upper left',ncol=2)  
#plt.tight_layout()

plt.grid(True,which='both', color='0.0')
plt.show()
