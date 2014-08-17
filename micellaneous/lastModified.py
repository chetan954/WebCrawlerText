##############################################################
#FILENAME : lastModified.py
#CREATED TO CHECK LAST MODIFIED DATE OF PAGES
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

import urllib

def chkDate(url):
    url = 'http://css-tricks.com/snippets/php/return-only-one-variable-from-mysql-query/'
    response = urllib.urlopen(url)
    headers = response.info()
    print headers

    headers = str(headers)
    headers = headers.split()

    i,j = 0,0

    ch='Last-Modified:'
    while i<len(headers):
        if headers[i]==ch:
            lst = [headers[i+2],headers[i+3],headers[i+4]]
            j = 1
            break
        i+=1

    if j:
        lst='-'.join(lst)
        return lst
    else:
        return 0

print chkDate('')
