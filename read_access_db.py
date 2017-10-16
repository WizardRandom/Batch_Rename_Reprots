#!/usr/bin/env python
import pyodbc
import glob
import fnmatch
import os

#don't forget pip install pyodbc to set up the import correctly in the enviroment!

# database file - Change as needed 
db_file = r'Z:\Reporting\processing\SJ501723\Exports\SJ501723  - MA Worcester PACP 10-12-2017\SJ501723  - MA Worcester PACP 10-12-2017.mdb'

#pathing location
pathing = r'Z:\Reporting\processing\SJ501723\Exports\SJ501723  - MA Worcester PACP 10-12-2017\LINE' 

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
	
#for i in asset:
#	print i
	
#for i in videofile:
#	print i
	
	

# Access specific driver With connection Strint
connstr = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
#Connect in
conn = pyodbc.connect(connstr)
# cursor to run SQL commands
crsr = conn.cursor()

# prints out header info
# for table_info in crsr.tables(tableType='TABLE'):
#   print(table_info.table_name)
# print(SELECT * FROM Inspections;)

# returns 3rd row
SQL = 'SELECT PACP_Inspections.InspectionID, PACP_Inspections.Pipe_Segment_Reference, PACP_Inspections.Inspection_Date, PACP_Media_Inspections.Video_Name, '
SQL = SQL + 'PACP_Media_Inspections.Video_Location '
SQL = SQL + 'FROM PACP_Inspections INNER JOIN PACP_Media_Inspections ON PACP_Inspections.InspectionID = PACP_Media_Inspections.InspectionID;'

PathData = []
Output = []

for row in crsr.execute(SQL):
	PathData.append(row)

	
Montharray = []
Dayarray = []

for i in PathData:
	if len(str(i[2].month)) == 1:
		Montharray.append('0' + str(i[2].month))
	else:
		Montharray.appendstr(i[2].month)
		
for i in PathData:
	if len(str(i[2].day)) == 1:
		Dayarray.append('0' + str(i[2].day))
	else:
		Dayarray.appendstr(i[2].day)
	
	
NewFileName = []
NewPath = []

for i in PathData:
	NewFileName.append('Sewer_segments_' + i[1] + '_' + str(i[2].year))
	
	
for x in range (0, len(Montharray)):
	NewFileName[x] = NewFileName[x] + Montharray[x] + Dayarray[x] + '_CCTV_' 
	
for x in range (0, len(NewFileName)):
	NewPath.append(NewFileName[x])
	
regex = r'*_?.wmv'


for x in range (0, len(NewFileName)):
	iter = 1
#	print PathData[x][3]
	if fnmatch.fnmatch(PathData[x][3], regex):
		NewFileName[x] = NewFileName[x] + str(1 + int(PathData[x][3][len(PathData[x][3]) - 5]))
	else:
		NewFileName[x] = NewFileName[x] + '1'
	
#for x in range (0, len(NewFileName)):
#	print NewFileName[x]
	#print PathData[x][3]



for x in range (0, len(asset)):			
	SQL = 'UPDATE PACP_Media_Inspections SET Video_Name = \'' + NewFileName[x] + '.wmv\', Video_Location = \'' 
	SQL = SQL + '\\LINE\\' + NewPath[x] + '1\\\' WHERE Video_Name = \'' + videofile[x] + '\' and Video_Location = \'\\LINE\\' + asset[x] + '\\\';'
	#print db_file
	crsr.execute(SQL)
	conn.commit()
	#print SQL
	#print NewPath[x]
	
	
for x in range (0, len(asset)):
		#print ''
		#print pathing + '\\' + asset[x]
		#print PathData[x][3]
		#print ''
		for filename in os.listdir(pathing + '\\' + asset[x]):
			#print str(filename)
			if (str(filename) == PathData[x][3]):
				os.rename(pathing + '\\' + asset[x] + '\\' + filename, pathing + '\\' + asset[x] + '\\' + NewFileName[x] + '.wmv')
				#print str(filename) + '  ' + PathData[y][3]
				#print pathing + '\\' + asset[x] + '\\' + PathData[x][3] + pathing + '\\' + asset[x] + '\\' + NewFileName[x] + '.wmv'
				#print ''

					
		
				
				
for x in range (0, len(asset)):
	for filename in os.listdir(pathing):
		if str(filename) == asset[x]:
			#print str(pathing + '\\' + filename)
			#print (pathing + '\\' + NewPath[x] + '1')
			os.rename(pathing + '\\' + filename, pathing + '\\' + NewFileName[x])
			#print ''

