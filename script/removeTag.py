##############################################################
#FILENAME : removeTag.py
#CREATED TO FILTER OTHER TAGS AND THEIR CONTENT
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

##OTHER TAGS MAY BE ADDED IF REQUIRED FOR THIS FILE

def scriptTag(page):
    #REMOVES CONTENT BETWEEN SCRIPT TAGS
    flg = 0
    while page.find("<script",flg)!= -1:
            start = page.find("<script",flg)
            end = page.find("</script>",flg)
            end = end+9
            i,k = 0,end-start
            page = list(page)
            while i<k:
                    page.pop(start)
                    i = i+1
            page = ''.join(page)
            flg = start
    return page

def styleTag(page):
    #REMOVES CONTENT BETWEEN STYLE TAGS
    flg = 0
    while page.find("<script",flg)!= -1:
            start = page.find("<style",flg)
            end = page.find("</style>",flg)
            end = end+9
            i,k = 0,end-start
            page = list(page)
            while i<k:
                    page.pop(start)
                    i = i+1
            page = ''.join(page)
            flg = start
    return page

def rmvTag(page):#MAIN FUNCTION TO REMOVE TAGS
    page = scriptTag(page)
    page = styleTag(page)
    return page
