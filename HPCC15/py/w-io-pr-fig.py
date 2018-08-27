import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=range(13)
y=[817    ,  906    ,  740    ,  806    ,  807    ,  807    ,  807    ,  805    ,  804    ,  804    ,  803    ,  803    ,  0 ]
y1=[805    , 890    , 693    , 734    , 731    , 729    , 729    , 722    , 719    , 718    , 717    , 716    , 0  ]
y2=[816    , 894    , 711    , 776    , 778    , 776    , 777    , 774    , 772    , 769    , 771    , 770    , 0  ]
y3=[804    , 893    , 681    , 632    , 598    , 579    , 565    , 546    , 532    , 517    , 511    , 504    , 0    ]
#y4=[806    , 895    , 700    , 695    , 678    , 669    , 663    , 651    , 642    , 636    , 632    , 629    , 0   ]
#y4=[798.00 , 893.14 , 697.66 , 693.32 , 675.54 , 667.16 , 660.89 , 648.85 , 639.98 , 632.45 , 629.93 , 623.73 , 0.00  ]
y4=[806.96 , 885.47 , 686.82 , 708.23 , 697.97 , 693.24 , 693.49 , 682.83 , 675.41 , 672.31 , 668.65 , 668.85 , 0.00 ]
plt.axis([-0.2, 12.2, 0, 1000])
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
plt.legend(fontsize=30,frameon=False,labelspacing=0,columnspacing=0,borderpad=0,loc='lower left') 

#plt.tight_layout()

#plt.grid(True,which='both', color='0.0')
plt.show()


