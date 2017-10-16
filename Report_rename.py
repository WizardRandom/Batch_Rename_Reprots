#!/usr/bin/env python
import pyodbc
import glob
import fnmatch
import os

#don't forget pip install pyodbc to set up the import correctly in the enviroment!

# database file - Change as needed 
db_file = r'"C:\Users\bhykes\Desktop\TestingFolder\SJ501723  - MA Worcester PACP 10-12-2017.mdb"'

#pathing location
DataPath = r'C:\Users\bhykes\Desktop\TestingFolder\LINE' 
ReportPath = r'C:\Users\bhykes\Desktop\TestingFolder\Reports'

# 
Rpt_path = glob.glob(ReportPath + r"\*.pdf")

Dat_path = glob.glob(DataPath + r"\*")

#print img_path

for i in Rpt_path:
	print i
	
print ''

#for i in Dat_path:
#	print i
	
	#for i in img_path:
#	print i[len(pathing)+1:len(i)]

bkslh = '\\'
asset = []
newassetname = []


	
# Scrub out report name  
	
for i in Dat_path:
	#print i[i.rfind(bkslh)+1:len(i)]
	newassetname.append(i[i.rfind(bkslh)+1:len(i)])
	

for filename in os.listdir(ReportPath):
	#print filename
	for i in range (0, len(newassetname)):
		if newassetname[i][15:str(newassetname[i]).index('_', 15)] == filename[0:filename.index('_')]:
			#print ReportPath + '\\' + newassetname[i][0:len(str(newassetname[i]))-7] + '_Report_1.pdf'
			#print ReportPath + '\\' + filename
			os.rename(ReportPath + '\\' + filename, ReportPath + '\\' + newassetname[i][0:len(str(newassetname[i]))-7] + '_Report_1.pdf')
			
			
	



	

#for x in range (0, len(NewFileName)):
#	iter = 1
#	print PathData[x][3]
#	if fnmatch.fnmatch(PathData[x][3], regex):
#		NewFileName[x] = NewFileName[x] + str(1 + int(PathData[x][3][len(PathData[x][3]) - 5]))
#	else:
#		NewFileName[x] = NewFileName[x] + '1'
	
#for x in range (0, len(NewFileName)):
#	print NewFileName[x]
	#print PathData[x][3]


	
	
#for x in range (0, len(asset)):
		#print ''
		#print pathing + '\\' + asset[x]
		#print PathData[x][3]
		#print ''
#		for filename in os.listdir(pathing + '\\' + asset[x]):
			#print str(filename)
#			if (str(filename) == PathData[x][3]):
#				os.rename(pathing + '\\' + asset[x] + '\\' + filename, pathing + '\\' + asset[x] + '\\' + NewFileName[x] + '.wmv')
				#print str(filename) + '  ' + PathData[y][3]
				#print pathing + '\\' + asset[x] + '\\' + PathData[x][3] + pathing + '\\' + asset[x] + '\\' + NewFileName[x] + '.wmv'
				#print ''			
		
				

			


