from sys import argv
from os.path import exists
from cmath import sqrt, log10
from shutil import copy2

script, from_file, to_file = argv

print("Cpoying from %s to %s" %(from_file, to_file))

infile = open(from_file)
indata = infile.read()

print("The input file is %d byte lone" % len(indata))

print("Does the output file exist? %r" % exists(to_file))

outfile = open(to_file,'w')
outfile.write(indata)

print("Alright, all done.")

outfile.close()
infile.close()

#done in one line
#shutil.copy2(from_file,to_file)
#we have to close the file or else it would not save the writen data