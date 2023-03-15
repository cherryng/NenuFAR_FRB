from scipy.io import readsav
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import pylab as plt
import numpy as np
import sys

FILE = sys.argv[1]
sav_data = readsav(FILE)
print(sav_data.keys())

mpl.rcParams.update({'font.size': 13,'font.family': 'serif'})
fig = plt.figure(figsize=[6,6])
ax = fig.add_subplot(1, 1, 1)

f = sav_data['f']
nnt2 = sav_data['nnt2']
nnf2 = sav_data['nnf2']
nnt = sav_data['nnt']
nnf = sav_data['nnf']
x = sav_data['x']
t = sav_data['t']

x2 = x[0:nnf2*nnf-1,0:nnt2*nnt-1]

im=plt.imshow(x2, extent=[ np.min(t), np.max(t), np.min(f), np.max(f)] , aspect='auto',origin='lower')

plt.ylabel('Frequency (MHz)')
plt.xlabel('Time (sec)')
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.5)
plt.colorbar(im, cax=cax)

plt.savefig('Waterfall.png',bbox_inches='tight')
plt.show()



