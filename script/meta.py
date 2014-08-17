##############################################################
#FILENAME : meta.py
#CREATED TO FILTER THE META TAGS
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

def metaContent(page,url):#EXTRACTS META TAG CONTENT
    lst=''
    while page.find("<meta")!=-1:
            start_link=page.find("<meta")
            page=page[start_link:]
            start_link=page.find("content=")
            start_quote=page.find('"',start_link)
            end_quote=page.find('"',start_quote+1)
            metaTag=page[start_quote+1:end_quote]
            page=page[end_quote:]
            lst = lst + metaTag
    lst = lst.split()
    return lst
