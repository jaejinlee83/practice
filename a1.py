#!/usr/bin/python
import sys

print "hello world"

# sys: system libary (eg. sys.xxx)
# argv: function. passing  argument in the command line
fread = open(sys.argv[1],'r')
fwrite = open(sys.argv[2],'w')
for line in fread:
    if(line.strip()[:1]==">"):
        #fwrite.write(line.strip()+'\n')
        tempcol = line.strip().split(":")
        tempgi = tempcol[0].split("|")
        fwrite.write(tempgi[1]+"\t")
        tempname = tempcol[1].split(",")
        tempname2 = tempname[0].split(" ")
        for i in range(1,len(tempname2)):
            fwrite.write(tempname2[i]+" ")
        fwrite.write("\n")
# python: zero index (starts with 0)
# "\t" : tab, "\n" : return carriage
