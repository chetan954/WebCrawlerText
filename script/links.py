##############################################################
#FILENAME : links.py
#CREATED TO FILTER THE LINKS OF PAGE
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

import lastModified as mod

def linksExt(page,url):#EXTRACTS LINKS FROM PAGES
    lst=[]

    #EXTRCTS DATA BETWEEN LINKS
    end=0
    while page.find("a href",end)!=-1:
            startLnk=page.find("a href",end)
            start=page.find('>',startLnk)
            end=page.find('<',start)
            lnkData=page[start+1:end]
            lst.append(lnkData)

    #EXTRACTS LINKS
    lst2=[]
    while page.find("a href")!=-1:
            start_link=page.find("a href")
            start_quote=page.find('"',start_link)
            end_quote=page.find('"',start_quote+1)
            tst=page[start_quote+1:end_quote]
            page=page[end_quote:]
            lst2.append(tst)

    #MAKE LIST OF LINKS
    i=0
    lnkLst=[]
    while i<len(lst):
            date = mod.chkDate(lst2[i])#GETS THE LAST MODIFIED DATE
            lnkLst.append([lst[i],lst2[i],date])
            i+=1
    return lnkLst
