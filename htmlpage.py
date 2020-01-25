#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:51:23 2018
@author: Andrea Moro, andrea at andreamoro.net
@modified from http://www.tldp.org/LDP/LG/issue19/python.html

"""

# this is how I import google analytics code
try: 
    from gan import addga
except :
    1

#  Class for generating HTML pages
#
    
class htmlPage:

    def __init__ (self, t="", h=""):
        self.title = t
        self.heading = h

    def generate_header (self):
	#
	# Generate heading for a page
	#
        tempstr = ""
        tempstr+= "Content-type:text/html\r\n\r\n"
        tempstr+= "<!DOCTYPE html> \n "
        tempstr+= "<html lang='en'>\n"
        tempstr+= "<head>\n"
        tempstr+= '<meta charset="UTF-8">\n'
        
        # add google analytics
        try :
            tempstr+= addga()
        except :
            1
        
        tempstr+= "<meta name='keywords' content='joyce ulysses concordance literature modernism'>\n"
        tempstr+= '<link href="/css/ulysses.css" type="text/css" rel="stylesheet">\n'
        tempstr+= "<title>" + self.title + "</title>\n"
        tempstr+= '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
        tempstr+= "<script src='/js/linkwords.js'></script> \n"
        tempstr+= '<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Arvo">'+"\n"
        tempstr+= '<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Raleway">'+"\n"
        tempstr+= "</head>\n"
        tempstr+= "<body>\n"
        tempstr+= "<h1>" + self.heading + "</h1>\n"
        return tempstr

    def generate_body (self):
	#
	# Empty function - to be redefined in a descendant
	#
        return ""

    def generate_footer (self):
	#
	# generate the footer for a page
	#
        tempstr = ""
        tempstr += "<div id='footer'>\n"
        tempstr += "<p>Ulysses text from <a href='http://www.gutenberg.org/files/4300'>gutenberg.org</a>\n"
        tempstr += "(<a href='http://www.gutenberg.org/wiki/Gutenberg:The_Project_Gutenberg_License'>license</a>)</p>\n"
        tempstr += "<p>By <a href='http://andreamoro.net'>Andrea Moro</a>, Vanderbilt University, "
        tempstr += "<a href='mailto:andrea@andreamoro.net'>andrea at andreamoro dot net </a>"
        tempstr += " - <a href='https://github.com/andreamoro-git/joyceconcordance'>Github code</a></p>\n"
        tempstr += "<a href='https://litconcordance.andreamoro.net''>Other concordances</a></p>\n</div>\n"
        tempstr +=  ("</body>\n")
        tempstr +=  ("</html>\n")
        return tempstr

    def generate (self):
        tempstr = self.generate_header()
        tempstr+= self.generate_body()
        tempstr+= self.generate_footer()
        return tempstr

#
# Code to test this class
#

if __name__ == "__main__":
    p = htmlPage ("This is the title", "<i>This is the top heading</i>")
    p.generate()
    print(p.generate())
