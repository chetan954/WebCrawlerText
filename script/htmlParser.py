##############################################################
#FILENAME : htmlParser.py
#CREATED TO FILTER THE CONTENT OF THE PAGE, REMOVES TAGS
#FOR WEBCRAWLER PROJECT : webCrawler.py (WebCrawlerText)
##############################################################

##PART OF THIS FILE (class MLStripper and strip_tags()) IS
##TAKEN FROM STACKOVERFLOW. READ readme.txt FOR MORE DETAILS.

from HTMLParser import HTMLParser

#REMOVES HTML TAGS
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):#FUNCTION CALLED TO REMOVE TAGS
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def filterContent(page,url):#FILTERS THE CONTENT OF THE REMAINING PORTION
    phrase = ['to','a','an','the',"i'm",\
        'for','from','that','their',\
        'i','my','your','you','mine',\
        'we','okay','yes','no','as',\
        'if','but','why','can','now',\
        'are','is','also']

    #CALLS FUNC TO REMOVE HTML TAGS
    page = strip_tags(page)

    #CONVERT TO LOWERCASE
    page = page.lower()

    #REMOVES WHITESPACES
    page = page.split()
    page = " ".join(page)

    #REMOVES IDENTICAL WORDS AND COMMON WORDS
    page = set(page.split())
    page.difference_update(phrase)

    #CONVERTS FROM SET TO LIST
    lst = list(page)

    return lst
