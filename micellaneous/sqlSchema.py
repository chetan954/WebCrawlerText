##############################################################
#FILENAME : sqlSchema.py
#CREATES THE SQL TABLE SCHEMA FOR THE DATABASE
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

import MySQLdb

#---------------------------------------------------------------

#CONNECT TO DB SERVER
# Open database connection
db = MySQLdb.connect("localhost","root","","searchEngine")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#---------------------------------------------------------------

#CREATE TABLES FOR DATA

#<1>
#STORES LINKS AND DATA
sql="""CREATE TABLE linksList(
         sourceLink CHAR(100) NOT NULL,
         linkName CHAR(100) NOT NULL,
         dataLink CHAR(100),
         date CHAR(15))"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print "Table linkList created\n"
except:
   # Rollback in case there is any error
   db.rollback()

#<2>
#STORES META DATA
sql="""CREATE TABLE metaData(
         sourceLink CHAR(100) NOT NULL,
         keyword CHAR(100) NOT NULL)"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print "Table metaData created\n"
except:
   # Rollback in case there is any error
   db.rollback()

#<3>
#STORES words
sql="""CREATE TABLE keywords(
         sourceLink CHAR(100) NOT NULL,
         keyword CHAR(100) NOT NULL)"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print "Table WORDS created\n"
except:
   # Rollback in case there is any error
   db.rollback()

#---------------------------------------------------------------

#DISCONNECT FROM SERVER
db.close()
