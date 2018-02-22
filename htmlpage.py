#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:51:23 2018

@author: moroa
@modified from http://www.tldp.org/LDP/LG/issue19/python.html
"""



#!/usr/bin/python
#
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
        tempstr+= '<!DOCTYPE html> \n <html lang="en">'
        tempstr+= ("<html>\n")
        tempstr+=  ("<head>\n")
        tempstr+= '<meta charset="UTF-8">\n'
        tempstr+= '<link href="css/ulysses.css" type="text/css" rel="stylesheet">\n'
        tempstr+=  ("<title>" + self.title + "</title>\n")
        tempstr+=  ("</head>\n")
        tempstr+=  ("<body>\n")
        tempstr+=  ("<h1>" + self.heading + "</h1>\n")
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
        tempstr =  ("</body>\n")
        tempstr+=  ("</html>\n")
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
