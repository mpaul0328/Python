''' run movefits.py movedir

    Creates a subset of directories within movedir for all fits
files within the current folder and copies them there based on 
their header information

30-JUL-2015 
    Converted to Python by Manuel Paul (paulm302@coyote.csusb.edu)'''

from astropy.io import fits 
import glob, os, shutil, sys

file_list = glob.glob('*.fts')              # Get fits files

# Check if list is empty
if len(file_list) == 0: 
    print 'No Files Found, aborting...'
    sys.exit()
 
for i in file_list:
    head = fits.open(i)                     # Load the header of the file
    objname = head[0].header["OBJECT"]      # Get the name of the object
    dt = head[0].header["DATE-OBS"]         # Get the date and time of the object
    date = dt[0:4] + dt[5:7] + dt[8:10]
    time = dt[11:13] + dt[14:16] + dt[17:19]
    filter = head[0].header["FILTER"]       # Get the filter of the image
    temp = head[0].header["CCD-TEMP"]       # Get the temperature of the image
    temp = str(abs(int(round(float(temp))))) 
    xbin = str(head[0].header["XBINNING"])  # Get the binning of the image
    ybin = str(head[0].header["YBINNING"])
    exp = head[0].header["EXPTIME"]         # Get the exposure time of the image
    exp = str(int(round(float(exp))))
    
    # Create the file name
    filename = objname + '-' + date + 'at' + time + '-' + 'Temp-' + temp + '-' + 'Bin' + xbin + '-' + 'ExpTime' + exp + '-' + filter + '.fts'

    # Create subset directories
    directory = objname
    if len(sys.argv) != 1: directory = sys.argv[1] + '/' + directory
    if os.path.isdir(directory) == False: os.makedirs(directory)
    directory = directory + '/' + date
    if os.path.isdir(directory) == False: os.makedirs(directory)
    directory = directory + '/' + filter
    if os.path.isdir(directory) == False: os.makedirs(directory)
    directory = directory + '/'

    # Copy the file to the new directory with its new name
    shutil.copy(i, directory + filename)

head.close()