#!/usr/bin/env python
import pyodbc
import glob
import fnmatch

#don't forget pip install pyodbc to set up the import correctly in the enviroment!

# database file - Change as needed 
db_file = r'Z:\Reporting\processing\SJ501723\Exports\SJ501723  - MA Worcester PACP 10-12-2017\SJ501723  - MA Worcester PACP 10-12-2017.mdb'

db_file = r'C:\Users\bhykes\Desktop\SJ501723  - MA Worcester PACP 10-12-2017.mdb'

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
	
	
NewPath = []

for i in PathData:
	NewPath.append('Sewer_segments_' + i[1] + '_' + str(i[2].year))
	
	
for x in range (0, len(Montharray)):
	NewPath[x] = NewPath[x] + Montharray[x] + Dayarray[x] + '_CCTV_' 
	
regex = r'*_?.wmv'


for x in range (0, len(NewPath)):
	iter = 1
	print PathData[x][3]
	if fnmatch.fnmatch(PathData[x][3], regex):
		NewPath[x] = NewPath[x] + str(1 + int(PathData[x][3][len(PathData[x][3]) - 5]))
	else:
		NewPath[x] = NewPath[x] + '1'
	
#for x in range (0, len(NewPath)):
#	print NewPath[x]
	

for x in range (0, len(NewPath)):
	SQL = 'UPDATE PACP_Media_Inspections SET Video_Name = \'' + NewPath[x] + '.wmv\', Video_Location = \'' 
	SQL = SQL + '\\LINE\\' + NewPath[x] + '\\\' WHERE Video_Name = \'' + videofile[x] + '\' and Video_Location = \'\\LINE\\' + asset[x] + '\\\';'
	#print db_file
	crsr.execute(SQL)
	conn.commit()
	print SQL
	
