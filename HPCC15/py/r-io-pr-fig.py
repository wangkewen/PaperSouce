import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x=range(13)
y=[0      ,  746    ,  830    ,  674    ,  735    ,  735    ,  735    ,  735    ,  734    ,  733    ,  732    ,  732    ,  735]
y1=[0      , 741    , 814    , 637    , 673    , 669    , 670    , 665    , 663    , 661    , 660    , 657    , 653 ]
y2=[0      , 749    , 817    , 651    , 713    , 713    , 713    , 712    , 709    , 705    , 705    , 706    , 703  ]
y3=[0      , 397    , 439    , 339    , 312    , 295    , 288    , 281    , 270    , 278    , 255    , 254    , 249   ]
#y4=[0      , 416    , 441    , 345    , 343    , 334    , 316    , 327    , 321    , 303    , 301    , 311    , 309    ]
#y4=[0.00   , 601.53 , 665.77 , 522.43 , 519.23 , 505.91 , 499.52 , 494.79 , 485.76 , 479.09 , 473.29 , 471.52 , 465.49]
y4=[0.00   , 674.51 , 734.13 , 573.23 , 591.13 , 582.37 , 572.25 , 577.60 , 569.86 , 563.74 , 561.27 , 558.17 , 556.32 ]
plt.axis([-0.2, 12.2, 0, 900])
ax.set_xticks(x)
ax.tick_params('both',direction='in', which='both', pad=1, bottom = 'on', top = 'on', left = 'on', right = 'on', labelcolor='black')
ax.yaxis.grid(color='grey', linestyle='-', linewidth=1, alpha=0.5) 
ax.xaxis.grid(color='white', linestyle='', linewidth=1, alpha=1)

plt.plot(x,y,label='Actual',linewidth=2, color='r', marker='x', ms=15, markeredgewidth=3)
plt.plot(x,y1,label='7.5GB',linewidth=2, color='g',marker='^', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y2,label='15GB',linewidth=2, color='b',marker='o', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y3,label='1.25GB',linewidth=2, color='m',marker='s', ms=12, fillstyle='none',markeredgewidth=3)
plt.plot(x,y4,label='2.5GB',linewidth=2, color='black',marker='+', ms=15, markeredgewidth=3)
plt.xlabel('Stage')
plt.ylabel('I/O Read (MB)',fontsize=30)
#plt.title('Stage Actual time VS predict time',fontsize=40)
#plt.xticks(index + bar_width, range(2),fontsize=30)
#plt.ylim(0,40)
plt.rcParams['font.size'] = 30 
#plt.rc('ytick', labelsize=10)
#ax.get_yticklabels().set_fontsize(30)
plt.legend(fontsize=23,frameon=False,labelspacing=0,columnspacing=0,borderpad=0,loc='lower right') 

#plt.tight_layout()

#plt.grid(True,which='both', color='0.0')
plt.show()


