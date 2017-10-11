#!/usr/bin/env python
import pyodbc

# database path
db_file = r"C:\Users\kcoury\Pictures\SJ501723 - MA Worcester PACP 9-26-2017.mdb"
# Access specific driver
conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};DBQ='+db_file)
# cursor to run SQL commands
crsr = conn.cursor()

# prints out header info
# for table_info in crsr.tables(tableType='TABLE'):
#   print(table_info.table_name)
# print(SELECT * FROM Inspections;)

# returns 3rd row
SQL = 'SELECT Pipe_Segment_Reference, Date FROM Inspections;'
PathData = []
for row in crsr.execute(SQL):
	PathData.append(row)
print(PathData[2])
