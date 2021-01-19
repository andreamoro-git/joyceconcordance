#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:05:17 2018

@author: moroa
"""
from ulyssespage import ulyssesPage
import os,re
import urllib.parse


class ulyssesCountsPage (ulyssesPage):

    def __init__ (self,episodeN=0,resetcache=0):
        ulyssesPage.__init__ (self,t= "Joyce's Ulysses word counts ",
			    h="Joyce's Ulysses word counts")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        textFile = open(dir_path+"/4300-0.txt","r")
        self.lines = textFile.read().split("\n")
        self.counts = {}
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
        if 'cs' in query :
            self.casesens = query['cs'][0]
        else :
            self.casesens = 'off'
        self.resetcache = 0
        if 'resetcache' in query :
            self.resetcache = 1

#    #Test case
#        self.lines = list()
#        self.lines.append("aaa aaa Aaa -bca dea aaa Introibo")
#        self.epbounds[0] = 0

    def word_count(self,string):

        if self.casesens == 'off':
            string = string.lower()

        words = re.split("\W+",string)

        for word in words:
            if word in self.counts and word != '' :
                self.counts[word] += 1
            else:
                self.counts[word] = 1
        return 1


    def count(self,ep) :
        if ep==0:
            fromline = self.epbounds[0]
            toline = self.epbounds[18]
        else :
            fromline = self.epbounds[ep-1]
            toline = self.epbounds[ep]
        for line in self.lines[fromline:toline-1]:
            self.word_count(line)
        wcsort = sorted(self.counts,key=self.counts.__getitem__,reverse=True)
        return (wcsort)

    def generate_body (self):

        dir_path = os.path.dirname(os.path.realpath(__file__))+'/cache'
        # try to get from cache
        if not self.resetcache :
            try :
                textFile = open(dir_path+"/count-e"+str(self.episodeN)+"-cs"+str(self.casesens),"r")
                return textFile.read()+"<p style='font-size:10px'>(cached)</p>"
            except :
                1
        sortedLines = self.count(self.episodeN)

        html = ""
        html += self.printEpisodeList()

        html+= "<div id='form'>\n"
        html+= self.printCountForm()
        html+= self.printForm()
        html+= "</div>\n"

        html += "<div id='text'> "
        html += "<h2> Word counts"
        if self.episodeN>0 :
            html+= ": "+self.epnames[self.episodeN-1]+" "
        html += "</h2>\n"
        count = 1E10
        for line in sortedLines:
            thiscount = p.counts[line]
            if  thiscount <count :
                count = thiscount
                html+= "<h3>"+str(count)+"</h3>"
            html+= "<a href='ulyssespage.py?cs="+str(self.casesens)+"&w="+line+"'>"+line+"</a>&nbsp;\n"

        try:
            textFile = open(dir_path+"/count-e"+str(self.episodeN)+"-cs"+str(self.casesens),"w")
            textFile.write(html)
        except :
            1
        return html


if __name__ == "__main__":
    p = ulyssesCountsPage(episodeN=0,resetcache=1)
    print(p.generate())
