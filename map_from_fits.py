import numpy as np
import matplotlib.pyplot as plt
import healpy as hp




#read the map header too
m100,header=hp.read_map('HFI_SkyMap_100-field-IQU_2048_R3.00_full.fits',field=(0,1,2), nest=True, h=True)

hp.read_map


hp.mollview(m100[0],cbar=True,nest=True, min=-3e-4,max=3e-4, title='I map',cmap='RdYlBu_r')
plt.show()
hp.mollview(m100[1],cbar=True,nest=True, min=-3e-5,max=3e-5, title='Q map',cmap='RdYlBu_r')
plt.show()
hp.mollview(m100[2],cbar=True,nest=True, min=-3e-5,max=3e-5, title='U map',cmap='RdYlBu_r')
plt.show()


 
