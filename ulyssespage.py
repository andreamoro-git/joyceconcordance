#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:05:17 2018

@author: Andrea Moro, andrea at andreamoro.net
"""

from htmlpage import htmlPage
import os,re
import urllib.parse

class ulyssesPage (htmlPage):

    def __init__ (self,episodeN=0,word="",wholeword='on',t='',h=''):
        htmlPage.__init__ (self, t,h)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        textFile = open(dir_path+"/4300-0.txt","r")
        self.lines = textFile.read().split("\n")

        try :
            self.url = os.environ['QUERY_STRING']
            query = urllib.parse.parse_qs(self.url)
        except :
            query = list()
            print('')

        self.episodeN = 0
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
            self.casesens = 'off'
        if 'ww' in query :
            self.wholeword = query['ww'][0]
        else :
            self.wholeword = wholeword

        # uncomment this code to find episode bounds, later saved in self.epbounds
#        self.epbounds = list()
#        for episode in range(18) :
#            searchString = '[ '+str(episode+1)+' ]'
#            self.epbounds.append(self.lines.index(searchString))
#        self.epbounds.append(self.lines.index('End of the Project Gutenberg EBook of Ulysses, by James Joyce'))
#        print(self.epbounds)
#        return

        self.epbounds =  [43, 1156, 1818, 2449, 3191, 3931, 5394, 7024, 8633, 10347,
                          12157, 14105, 16672, 18166, 19889, 25298, 27568, 30650, 32354]
        self.epnames = ["Telemachus","Nestor","Proteus","Calypso","Lotus Eaters",
            "Hades","Aeolus","Lestrygonians","Scylla and Charybdis",
            "Wandering Rocks","Sirens","Cyclops","Nausicaa",
            "Oxen of the Sun","Circe","Eumaeus","Ithaca","Penelope"]


    def findEpisode(self,row) :
        thisep = 0
        for ep in range(18) :
            if row >= self.epbounds[ep]:
                thisep= ep
        return thisep

    def addEpLink(self,num,text="",word="") :
        ep = self.findEpisode(num)
        if text == '' :
            text = '[ ]'
        rowtext = ""
        rowtext += "<div><span class='rown' id='row" + str(num) + "'>  \n"
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

    def printEpisodeList(self) :
        html = ""
        html += "<div id='list'><h2> Episodes text </h2><ol>\n"

        for bound in range(18) :
            html += "<li>"
            html += "<a href='ulyssespage.py?e="+str(bound+1)+"'> "+self.epnames[bound]+ "</a> \n"
        html += "</ol>\n</div>\n"

        return html

    def printForm(self) :
        if self.casesens =='on' :
            checked = 'checked'
        else:
            checked = ''
        if self.wholeword != 'off' :
            wwchecked = 'checked'
        else:
            wwchecked = ''
        html = ''
        html += "<h2>String search</h2>\n<form action ='ulyssespage.py'> \n"
        inputvalue = ' '
        if self.word != '' :
            inputvalue = 'value = "'+self.word+'"'
        html += "<input type='text' name='w' "+inputvalue+" > \n"
        html += "<input type='submit' class='addlinks' value='Search' > \n"
        html += " <input type='checkbox' name='cs' " + checked +"> case sensitive \n"
        html += " <input type='checkbox' name='ww' " + wwchecked +"> whole word \n"
        html += "<input type='hidden' name='ww' value='off' >"
        html += "</form>\n "

        return html

    def printCountForm(self) :
        if self.casesens=='on' :
            checked = 'checked'
        else:
            checked = ''
#        if self.wholeword != 'off' :
#            wwchecked = 'checked'
#        else:
#            wwchecked = ''
        html = ''
        html += "<h2>Words count</h2>\n<form action ='ulyssescounts.py'> \n"

        #episode
        html += '<select name="e">\n'
        selected = ''
        if self.episodeN == 0 :
            selected = ' selected '
        else :
            selected = ' '
        html+= '<option value="0" '+selected+' >All text</option>\n'
        for ep in self.epnames :
            selected = ''
            if ( ep == self.epnames[self.episodeN-1] and self.episodeN>0 ) :
                selected = ' selected '
            html+= '<option value="'+str(self.epnames.index(ep)+1)+'" '+selected+' >'
            html+= str(self.epnames.index(ep)+1)+'. '+ep+"</option>\n"
        html += "</select>\n"

        #checkboxes
        html += " <input type='checkbox' name='cs' " + checked +"> case sensitive \n"
#        html += " <input type='checkbox' name='ww' " + wwchecked +" disabled> whole word \n"
        html += "<input type='hidden' name='ww' value='off' >"
        html += "<input type='submit' class='addlinks' value='Count' > \n"
        html += "</form>\n"

        return html

    def generate_body (self):
        episodeN = self.episodeN

        # remove title and author
        lines = self.lines[self.epbounds[0]:self.epbounds[18]]
        p.epbounds=[x - p.epbounds[0] for x in p.epbounds]

        html = ""

        html+= self.printEpisodeList()

        html+= "<div id='form'>\n"
        html+= self.printCountForm()
        html+= self.printForm()
        html+= "</div>\n"

        html += "<div id='text'>\n"

        # word search
        if self.episodeN == 0 and self.word != '':
            searchString = self.word
            if self.casesens == 'on' :
                foundLines = [lines.index(x) for x in lines if searchString in x]
                notifystring = ' - case sensitive'
            else :
                foundLines = [lines.index(x) for x in lines if searchString.lower() in x.lower()]
                notifystring = ' - not case sensitive '

            # remove instances where not the whole word
            if self.wholeword == 'on':
                notifystring +=  ' - whole word '
                keepFoundLines = list(foundLines)
                for fline in foundLines:
                    if self.casesens =='on' :
                        if not self.word in re.split("\W+",lines[fline]) :
                            keepFoundLines.remove(fline)
                    else :
                        if not self.word.lower() in re.split("\W+",lines[fline].lower()) :
                              keepFoundLines.remove(fline)
                foundLines = keepFoundLines

            #count hits
            counthits = 0
            for fline in foundLines:
                if self.casesens =='on' :
                    counthits+= lines[fline].count(self.word)
                else :
                    counthits+= lines[fline].lower().count(self.word.lower())


            # display output
            html+= "<h2>String search: "+self.word+" - "+str(counthits)+" matches "+notifystring+"</h2>\n"
            html+= "<p><span class='addlinks' id='addlinks'>Link every word</span></p> \n"

            thisEpisode = -1
            for line in foundLines :
                lineEpisode = self.findEpisode(line)
                if lineEpisode > thisEpisode:
                    html+= "<h3>"+str(lineEpisode+1)+". "+self.epnames[lineEpisode]+"</h3>"
                    thisEpisode = lineEpisode

                html+= self.addEpLink(line,lines[line],self.word) + "\n"

        # display full episode
        elif episodeN > 0 :
            html+= "<h2>"+str(episodeN)+". "+self.epnames[episodeN-1]+"</h2>\n"
            html+= "<p><span class='addlinks' id='addlinks'>Link every word</span> (may take a few seconds)</p> \n"
            start = self.epbounds[episodeN-1]
            end = self.epbounds[episodeN]

            for lineN in range(start,end):
                html+= self.addNameAnchor(lineN,lines[lineN]) + "\n"

        html+= "</div>\n"
        if episodeN<18 and episodeN>0:
            html+= "<div id='sandbox'>\n"
            html+= "<a href='ulyssespage.py?e="+str(episodeN+1)
            html+= "'>Next: "+str(episodeN+1)+". "+self.epnames[episodeN]+"</a>\n"
            html+= "</div>\n"

        return html


if __name__ == "__main__":
    p = ulyssesPage(episodeN=0,word='',t="Joyce's Ulysses Concordance",
                    h="Joyce's Ulysses Concordance")
    print(p.generate())
