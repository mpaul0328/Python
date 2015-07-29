''' run FindExpTime.py File1 File2 File3... OutputFile

    Reads in a bunch of image files and then prints the exposure 
times of each image into another file'''

from sys import argv
from astropy.io import fits 

l = len(argv)
outfile = open(argv[l -1], 'a')
for i in range(l - 1):
    if i != 0:
        filename = fits.open(argv[i])
        time = filename[0].header['EXPTIME']
        outfile.write(argv[i] + " ExpTime = " + str(time) + "\n")
filename.close()        
outfile.close()
        
