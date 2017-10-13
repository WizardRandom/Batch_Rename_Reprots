#!/usr/bin/env python
import glob

#pathing location
pathing = r'S:\projects\NJ Newark\NJ Newark Combined PACP Oct2017\LINE' 

# 
img_path = glob.glob(pathing + r"\*\*.wmv")

#print img_path

#for i in img_path:
#	print "index " + i[30:70] 
# Prints video path


#for i in img_path:
#	print i[len(pathing)+1:len(i)]

bkslh = '\\'
asset = []
videofile = []


# Scrub out image path 
for i in img_path:
#	print i[len(pathing)+1:i.rfind(bkslh)]
	asset.append(i[len(pathing)+1:i.rfind(bkslh)])
	
	
#Scrub out the file name
for i in img_path:
#	print i[len(pathing)+1:i.rfind(bkslh)]
	videofile.append(i[i.rfind(bkslh)+1:len(i)])
	
for i in asset:
	print i
	
for i in videofile:
	print i
	
	
