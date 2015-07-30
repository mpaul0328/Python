''' run FileList.py OutputFile 

    Creates a file with a list of .fts files

30-JUL-2015
Written by Manuel Paul (paulm302@coyote.csusb.edu)'''

from sys import argv
import glob

data = open(argv[1], "a")
for i in glob.glob("*.fts"):
    data.write(i + "\n")
data.close()