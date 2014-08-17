Project: WebCrawlerText
Author: Chetan Singh
Contact: chetansingh954@gmail.com
Platform: Python 2

This project is disributed under Creative Commons License Attribution-NonCommercial-ShareAlike 3.0. The legal code is
provided in the main directory as legalCode.txt.

##Released as free software.
##Further details about the license and usage rights can be viewed in creative commons website.
##Visit https://creativecommons.org/

Ver 1.0

This is a text crawler made on python as main scripting language. The aim of this crawler is to crawl through the
web and while crawling do links extraction and html parsing for each page. The indexing of the keywords is done,
and the data is stored on the server specified. Although this project is intended to be a text crawler, modifications
can be made (i intend to do so) pretty easily for multimedia.

##Note that this script DOES NOT use Beautiful Soup for html parsing whatsoever.
##Manual functions are used with standard library functions to do so.

##Although this is a project of a webcrawler, to access the results i have used html and php as interface.
##Although it looks like a serch engine it does not uses any algorithm for page ranking whatsoever.

The complete code is divided into a few files.

<1>. The main crawler and its extenstions (other scripts), are stored in 'script' folder. The contents of the folder
are given below;

--> webCrawler.py
This file is main script. It calls for all the functions and enters the data into database. The script handles most
of the part of code.

##It uses MySQLdb to enter the data and for other database related operations.

--> meta.py
This script is imported by webCrawler.py. Its function is to get the meta tag keywords of the webpage. Then those
are stored into a list and returned.

--> links.py
This script is also imported by webCrawler.py. Its function is to extract the links of the page and get the data
associated with those links, e.g., <a href"...>data</a>. Then the data is stored in a list and returned.

--> htmlParser.py
This script is imported by webCrawler.py. The content of the page is extracted and the tags are removed. After
that the contents are filtered and formatting (e.g., removing duplicates, common words etc.) is done. The keywords
are stored in a list and the list is returned.

##This script filters the content pretty much, though its not perfect, but it is still good.

##The html tags removing function and class, as specified in file, are taken from Eloff's answer on STACKOVERFLOW.
##The link for the answer is; http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
##The usage rights are as per standard stackoverflow rules (cc by-sa 3.0 with attribution required).

--> removeTag.py
This script is imported by webCrawler.py. This script removes any tags whose whole script along with content is
not required and returns the page as string.

--> lastModified.py
This script is imported by links.py. This script checks the last modified date of the webpage and returns the date. If the date is not provided by server,
it returns 0.


<2>. The accessing of the data from the database is done through a html and php page combo. Both are in the
'interface' folder.

--> searchPage.html
This page is used to search from the database. It is the interface for the communication of client with database.

--> dbConnect.php
This file takes the form input from searchPage.html and accesses the query from database. It retrives the data and
prints out the result.


<3>. There is a python script to check the last modified status of pages, that is, it checks if the
indexing done is of latest page or not. There is also a script to create the database schema. They are in the
'miscellaneous' folder.

--> sqlSchema.py
This script creates the sql table schema for the database and return confirmation status.

##The database used for the purpose is 'searchEngine' with latin1_swedish_ci collation.

--> modifiedCheck.py
This script checks weather the index of database is up to date or not.

##This script uses lastModified.py as a library. So a copy of lastModified.py is kept in this folder.


NOTE: 1. This project is made under standard python compiler for python ver. 2.7.
2. This project is intended as a personal project for the author. Any kind of mistakes on the part of author are
not subjeced to any warranties or claim to that matter.