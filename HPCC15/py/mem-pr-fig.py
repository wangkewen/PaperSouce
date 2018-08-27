import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+0.05*rect.get_width(), height+1, '%s' % height, fontsize=30)

fig, ax =plt.subplots()
#plt.subplot(121)
n_groups = 5
time_real = (28.4,29.2,28.7,31.4,29.0) 
#A_predict = (29.16)
#B_predict = (28.69)
#C_predict =(31.43)
#D_predict=(29.00) 
index = np.arange(n_groups)
print(index)
bar_width = 0.3
opacity = 1.0
ax.grid(color='black', linestyle='--', linewidth=1, alpha=1)
ax.tick_params('both',direction='in', which='both', pad=10, bottom = 'on', top = 'on', left = 'on', right = 'on', labelcolor='black') 
rects1 = plt.bar(index, time_real, bar_width, align='center', alpha=0.8*opacity, color='black',label= 'Actual')
autolabel(rects1)

#plt.xlabel('Stage')
plt.ylabel('Mem (GB)',fontsize=30)
#plt.title('Stage Actual time VS predict time',fontsize=40)
plt.xticks(index , ('Actual', '30%', '60%', '5%', '10%'),fontsize=30)
#plt.ylim(0,40)
plt.rcParams['font.size'] = 30 
#plt.rc('ytick', labelsize=10)
#ax.get_yticklabels().set_fontsize(30)
#plt.legend(fontsize=25,frameon=False,labelspacing=0,columnspacing=0,borderpad=0)  
#plt.tight_layout()

plt.grid(True,which='both', color='0.0')
plt.show()

