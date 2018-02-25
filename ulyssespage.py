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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        textFile = open(dir_path+"/4300-0.txt","r")
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
        if 'cs' in query :
            self.casesens = query['cs'][0]
        else : 
            self.casesens = 0

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
   
    def addEpLink(self,num,text="",word="") :
        ep = self.findEpisode(num)
        if text == '' :
            text = '[ ]'
        rowtext = ""
        rowtext += "<div><span class='rownp' id='row'" + str(num) + "'>  \n"
        rowtext += " ("+self.epnames[ep]+") "
        rowtext += "[<a href='?w="+word+"&e="+str(ep+1)+"#row" + str(max(self.epbounds[ep],num-5))+ "'>"+str(num)+"</a>]\n"

        rowtext += "</span>\n"
        rowtext += '<span class="row">'+text+'</span></div>'
        rowtext += "\n"

        return rowtext
    
    def addNameAnchor(self,num,text="") :
        if text == '' :
            text = '&nbsp;'
        rowtext =  ""
        rowtext += '<div><span class="rown" id="row'+str(num)+'">['+str(num)+']</span>'
        rowtext += '<span class="row">'+text+'</span></div>'
        rowtext += "\n"
        
        return rowtext

    def generate_body (self):
        episodeN = self.episodeN
        lines = self.lines
        if self.casesens :
            checked = 'checked'
        else:
            checked = ''

        html = ""
        html += "<div id='list'><h2> Episodes text </h2><ol>\n"
            
        for bound in range(18) :
            html += "<li>"
            html += "<a href='?e="+str(bound+1)+"'> "+self.epnames[bound]+ "</a> \n"
        html += "</ol>\n</div>\n"

        html += "<div id='form'>\n<h2>String search</h2>\n<form action ='ulyssespage.py'> \n"
        inputvalue = ' '
        if self.word != '' :
            inputvalue = 'value = "'+self.word+'">'
        html += "<input type='text' name='w'"+inputvalue+"  \n"
        html += "<input type='checkbox' name='cs'" + checked +"> case sensitive \n"
        html += "<input type='submit' class='addlinks' value='Submit' > \n"
        html += "<p><span class='addlinks' id='addlinks'>Link every word</span> (may take a few seconds)</p> \n"
        html += "</form>\n </div>\n"
        html += "<div id='text'>\n"

        if self.episodeN == 0 and self.word != '':
            searchString = self.word
            if self.casesens :
                foundLines = [lines.index(x) for x in lines if searchString in x]
                notifystring = ' (case sensitive)'
            else :                
                foundLines = [lines.index(x) for x in lines if searchString.lower() in x.lower()]
                notifystring = ' (not case sensitive) '
                
            html+= "<h2>String search: "+self.word+" ("+str(len(foundLines))+" matches) "+notifystring+"</h2>\n"
            for line in foundLines :
                html+= self.addEpLink(line,lines[line],self.word) + "\n"
        elif self.episodeN > 0 :
            html+= "<h2>"+str(self.episodeN)+". "+self.epnames[self.episodeN-1]+"</h2>\n"
            start = self.epbounds[self.episodeN-1]
            if episodeN<18 :
                end = self.epbounds[self.episodeN]
            else :
                end = len(lines)-1

            for lineN in range(start,end):
                html+= self.addNameAnchor(lineN,lines[lineN]) + "\n"

        html+= "</div>\n<div id='sandbox'> </div>\n"
        return html


if __name__ == "__main__":
    p = ulyssesPage(episodeN=0,word='')
    print(p.generate())
