##############################################################
#FILENAME : modifiedCheck.py
#CREATED TO CHECK LAST MODIFIED DATE OF PAGES IN DATABASE
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

import MySQLdb
import lastModified as mod

#---------------------------------------------------------------------------------------------------------------

#DB INITIALIZATION

# Open database connection
db = MySQLdb.connect("localhost","root","","searchEngine")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#---------------------------------------------------------------------------------------------------------------

sql = "SELECT linkName, date FROM linksList"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   rows = cursor.fetchall()
   print rows

except:
   print "Error: unable to fecth data"

i,j = 0,0
lst = []

while i<len(rows):
    date = mod.chkDate(rows[i][0])#GET THE LAST MODIFIED DATE OF WEBPAGE
    if date:
        if date != rows[i][1]:
            lst[j] = rows[i][0]
            j+=1
    i+=1

print 'The links needed to be updated are:\n'
print lst

#---------------------------------------------------------------------------------------------------------------

# DISCONNECT FROM SERVER

db.commit()
db.close()

