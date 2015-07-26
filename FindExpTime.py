'''run FindExpTime.py File1 File2 File3... Output File''' 

# DOES NOT OUTPUT TO ANY FILE YET! INPUT EXTRA FILE IN PLACE OF OUTPUT FILE

''' Reads in a bunch of image files and then prints the exposure 
times of each image into another file'''

import sys, numpy as np
from astropy.io import fits 

length = len(sys.argv)
for arg in range(length-1):
    if arg != 0:
        filename = fits.open(sys.argv[arg])
        time = filename[0].header['EXPTIME']
        print sys.argv[arg] + " ExpTime = " + str(time)

