#!/usr/bin/env python
import glob

# 
img_path = glob.glob(r"C:\Users\gescobar\Documents\SJ501723 - MA Worcester PACP 9-26-2017\LINE\*\*.wmv")

#print img_path

#for i in img_path:
#	print "index " + i[30:70] 
# Prints video path
for i in img_path:
	print i
