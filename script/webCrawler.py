##############################################################
#FILENAME : webCrawler.py
#MAIN FILE TO CALL ALL FUNCTIONS, ACTS AS CRAWLER
#FOR WEBCRAWLER PROJECT : WebCrawlerText
##############################################################

import urllib
import meta
import links
import htmlParser as tag
import removeTag as rem
import MySQLdb

#---------------------------------------------------------------------------------------------------------------

crawled = []#GLOBAL URL LIST TO CHECK WEATHER CRAWLED OR NOT

#---------------------------------------------------------------------------------------------------------------

#DB INITIALIZATION

# Open database connection
db = MySQLdb.connect("localhost","root","","searchEngine")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#---------------------------------------------------------------------------------------------------------------

#DATABASE DATA ENTRY FUNCTIONS

def linksData(lnkLst,url):
    #ENTER DATA INTO DB
    i,j=0,0
    while i<len(lnkLst):
        sql = "INSERT INTO linksList(sourceLink, \
               linkName, dataLink, date) \
               VALUES ('%s', '%s', '%s', '%s')"
        cursor.execute(sql,(url,lnkLst[i][0],lnkLst[i][1],lnkLst[i][2]))
        i+=1
    db.commit()

def metatagData(lst,url):
    #ENTER DATA INTO DB
    i,j=0,0
    while i<len(lst):
        sql = "INSERT INTO metaData(sourceLink, \
               keyword) \
               VALUES ('%s' , '%s')"
        cursor.execute(sql,(url,lst[i]))
        i+=1
    db.commit()

def keyword(lst,url):
    #ENTER DATA INTO DB
    i,j=0,0
    while i<len(lst):
        sql = "INSERT INTO keywords(sourceLink, \
               keyword) \
               VALUES ('%s','%s')"         
        cursor.execute(sql,(url,lst[i]))
        i+=1
    db.commit()

#---------------------------------------------------------------------------------------------------------------

#PAGE ACCESSING FUNCTIONS

def pageContent(url):#EXTRACTS HTML CODE
    f = urllib.urlopen(url)
    page = f.read()
    f.close()
    return page

def perPage(url):#ADD SOMETHING TO CHECK WEATHER URL VALID OR NOT
    print 'page'
    page = pageContent(url)

    page = rem.rmvTag(page) 

    metaLst = meta.metaContent(page, url)
    print metaLst
#    metatagData(metaLst,url)

    lnkLst = links.linksExt(page, url)
    print lnkLst

    filPg = tag.filterContent(page, url)
    print filPg

    print '\n---------------------------------------------------------'
    return lnkLst

def mainFunc(depth,url):#FOR THE DEPTH MANIPULATION
    global crawled
    print 'main'
    if (depth):
        lst = perPage(url)
        crawled.append(url)
        i = 0
        if (depth-1):
            while i<len(lst):
                if lst[i][1] not in crawled:
                    mainFunc(depth-1,lst[i][1])
                i+=1

#---------------------------------------------------------------------------------------------------------------

#INPUT DATA AND FUNCTION CALLING

url = raw_input("Enter the seed page:")
depth = int(raw_input("Enter the depth:"))
mainFunc(depth,url)

#---------------------------------------------------------------------------------------------------------------

# DISCONNECT FROM SERVER

db.commit()
db.close()

