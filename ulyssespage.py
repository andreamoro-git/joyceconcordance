#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:05:17 2018

@author: moroa
"""
from htmlpage import htmlPage
import os
import urllib.parse

class ulyssesPage (htmlPage):

    def __init__ (self,episodeN=0,word=""):
        htmlPage.__init__ (self, "Joyce's Ulysses concordance",
			    "Joyce's Ulysses concordance")
        textFile = open("/Users/moroa/Dropbox/misc/Ulysses/cgi-bin/4300-0.txt","r")
        self.lines = textFile.read().split("\n")

        try :
            self.url = os.environ['QUERY_STRING']
            query = urllib.parse.parse_qs(self.url)
        except :
            query = list()
            print('')

        if 'e' in query :
            self.episodeN = int(query['e'][0])
        else :
            self.episodeN = episodeN
        if 'w' in query :
            self.word = query['w'][0]
        else :
            self.word = word

#        self.epbounds = list()
#        for episode in range(18) :
#            searchString = '[ '+str(episode+1)+' ]'
#            self.epbounds.append(lines.index(searchString))
#        print(self.epbounds)
        self.epbounds =  [6, 1119, 1781, 2412, 3154, 3894, 5357, 6987, 8596, 10310,
                             12120, 14068, 16635, 18129, 19852, 25261, 27531, 30613]
        self.epnames = ["Telemachus","Nestor","Proteus","Calypso","Lotus Eaters",
            "Hades","Aeolus","Lestrygonians","Scylla and Charybdis",
            "Wandering Rocks","Sirens","Cyclops","Nausicaa",
            "Oxen of the Sun","Circe","Eumaeus","Ithaca","Penelope"]
    
    def findEpisode(self,row) :
        for ep in range(18) :
            if row >= self.epbounds[ep]:
                thisep= ep
        return thisep
    
    def addEpLink(self,num,text="") :
        ep = self.findEpisode(num)
        
        rowtext = ""
        rowtext += "<span class='rownp' id='row'" + str(num) + "'>  \n"
        rowtext += "[<a href='?e="+str(ep)+"#row" + str(num)+ "'>"+str(num)+"</a>]\n"
        rowtext += "("+self.epnames[ep]+")"
        rowtext += "</span>\n"
        rowtext += '<span class="row">'+text+'</span><br />'
        
        return rowtext
    
    def addNameAnchor(self,num,text="") :
        return('<span class="rown" id="row'+str(num)+'">['+str(num)+']</span>'
           +'<span class="row">'+text+'</span><br />')

    def generate_body (self):
        episodeN = self.episodeN
        lines = self.lines

        html = ""
        html += "<div>Word search:<form action ='ulyssespage.py'> \n"
        html += "<input type='text' name='w'> \n"
        html += "<input type='submit' value='Submit' \n"
        html += "</form></div>\n"

        html += "<ul>\n"
        for bound in range(18) :
          
            html += "<li>Episode "+str(bound+1)+ " : "
            html += "<a href='?e="+str(bound+1)+"'> "+self.epnames[bound]+ "</a> \n"
        html += "</ul>\n"

        if self.episodeN == 0 and self.word != '':
            searchString = self.word
            foundLines = [lines.index(x) for x in lines if searchString in x]
            html+= "<h2>Word search: "+self.word+" ("+str(len(foundLines))+")</h2>"
            for line in foundLines :
                html+= self.addEpLink(line,lines[line]) + "\n"
        elif self.episodeN > 0 :
            #string to search
            start = self.epbounds[self.episodeN-1]
            if episodeN<18 :
                end = self.epbounds[self.episodeN]
            else :
                end = len(lines)-1

            for lineN in range(start,end):
                html+= self.addNameAnchor(lineN,lines[lineN]) + "\n"

        return html


if __name__ == "__main__":
    p = ulyssesPage(episodeN=0,word='')
    print(p.generate())
