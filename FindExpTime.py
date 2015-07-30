''' run FindExpTime.py InputListFile OutputFile

    Reads in a bunch of image files and then prints the exposure 
times of each image into another file'''

from sys import argv
from astropy.io import fits 

flist = open(argv[1], 'r')
outfile = open(argv[2], 'a')
for file in flist:
    file = file.replace("\n","")
    filename = fits.open(file)
    time = filename[0].header['EXPTIME']
    outfile.write(file + " ExpTime = " + str(time) + "\n")
flist.close()
filename.close()
outfile.close()
        
        
