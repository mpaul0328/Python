''' run data.py OutputFile 

    Creates a file with a list of .fts files'''

from sys import argv
import glob

data = open(argv[1], "a")
for i in glob.glob("*.fts"):
    data.write(i + "\n")

data.close()

