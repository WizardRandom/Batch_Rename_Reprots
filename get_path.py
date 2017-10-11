#!/usr/bin/env python
import glob

# 
img_path = glob.glob(r"C:\Users\kcoury\Pictures\*.png")

#print img_path

#for i in img_path:
#	print "index " + i[30:70] 
# Prints video path
for i in img_path:
	print i
