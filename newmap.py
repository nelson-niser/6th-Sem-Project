import pandas as pd
import healpy as hp
import numpy as np
import matplotlib.pyplot as plt


import warnings
warnings.filterwarnings("ignore")

plt.style.use('seaborn-talk')

input_cl = pd.read_csv("COM_PowerSpect_CMB_TT_full_R3_01.txt",
                       delim_whitespace=True, index_col=0)
print(input_cl)

input_cl.head()
input_cl.plot(logx=True, logy=True, grid=True);
plt.show()

input_cl.l.plot(logx=False, logy=False, grid=True)
plt.ylabel(r"$\dfrac{\ell(\ell+1)}{2\pi} C_\ell~[\mu K^2]$")
plt.xlabel(r"$\ell$")

plt.xlim([50, 2500]);
plt.show()

input_cl.head()

print(len(input_cl))

lmax = int(input_cl.index[-1])
print(lmax)

cl = input_cl.divide(input_cl.index * (input_cl.index+1) / (np.pi*2), axis="index")
cl /= 1e12
cl.head()
cl = cl.reindex(np.arange(0, lmax+1))
cl.head()
cl = cl.fillna(0)
cl.head()
print(input_cl)

seed = 583
np.random.seed(seed)

alm = hp.synalm((cl.l, cl.Dl, cl.ndDl, cl.pdDl), lmax=lmax, new=True)

high_nside = 1024
cmb_map = hp.alm2map(alm, nside=high_nside, lmax=lmax)

hp.mollview(cmb_map[0], min=-300*1e-6, max=300*1e-6, unit="K", title="CMB Temperature")
plt.show()

cl_from_map = hp.anafast(cmb_map, lmax=lmax, use_pixel_weights=True) * 1e12 # in muK^2
ell = np.arange(cl_from_map.shape[1])
cl_from_map *= ell * (ell+1) / (2*np.pi)

np.median(cl_from_map, axis=1)

plt.plot(cl_from_map[0], label="map Cl")
input_cl.l.plot(logx=False, logy=False, grid=True, label="Input Cl")
plt.ylabel(r"$\dfrac{\ell(\ell+1)}{2\pi} C_\ell~[\mu K^2]$")
plt.xlabel(r"$\ell$")
plt.legend();
plt.show()