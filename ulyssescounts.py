#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:05:17 2018

@author: moroa
"""
from htmlpage import htmlPage
import os,re
import urllib.parse


class ulyssesCountsPage (htmlPage):

    def __init__ (self,episodeN=0):
        htmlPage.__init__ (self, "Joyce's Ulysses word counts ",
			    "Joyce's Ulysses word counts")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        textFile = open(dir_path+"/4300-0.txt","r")
        self.lines = textFile.read().split("\n")
        self.counts = dict()
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
        
    def word_count(self,string):
   
        words = re.split("\W+",string)
    
        for word in words:
            if word in self.counts:
                self.counts[word] += 1
            else:
                self.counts[word] = 1
    
        return 1

    def count(self,ep) :
        for line in self.lines:
            self.word_count(line) 
        wcsort = sorted(self.counts,key=self.counts.__getitem__,reverse=True)
        return (wcsort)

    def generate_body (self):
        sortedLines = self.count(0)

        html = ""
        html += "<div id='list'><h2> Word counts </h2>\n"
        count = 999999999999
        for line in sortedLines:
            thiscount = p.counts[line]
            if  thiscount <count :
                count = thiscount
                html+= "<h3>"+str(count)+"</h3>"
            html+= "<a href='ulyssespage.py?w="+line+"'>"+line+"</a>&nbsp;\n"
        html+= "</div>\n<div id='sandbox'> </div>\n"
        return html


if __name__ == "__main__":
    p = ulyssesCountsPage(episodeN=0)
    print(p.generate())
 
