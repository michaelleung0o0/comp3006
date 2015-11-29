from xmlReader import xmlReader
url = 'http://cn.wsj.com/big5/rssHKstock.xml'

class readNews():
    #xmlReader = None

    def __init__(self, url):
        self.xmlread = xmlReader(url,'news.xml')
        self.xmlread.requestXML()

    def displayAllXML(self):
        #content = self.xmlread.requestXML()
        #content = self.xmlread.decodeBig5(content)
        #print content
        with open ('news.xml', "r") as myfile:
            content = myfile.read().decode('big5')
        #return content
        return content
        #print "readXML -----------------------------------"
    def imptXML(self):
        allXML = self.displayAllXML()
        imptXML = self.findAndCutString(allXML, "</channel>")
        return imptXML

    def getPubDate(self):
        i = 1
        text = self.imptXML()
        pubDateList = []
        while i <= self.countNumOfNews():
            tmp = self.findAndCutString(text, "<pubDate>", "</pubDate>")
            pubDateList.append(tmp)
            text = self.findAndCutString(text, "</pubDate>")
            i +=1
        j = 0
        for j in pubDateList:
            print j + "\n"
        return pubDateList

    def getTitle(self):
        i = 1
        text = self.imptXML()
        titleList = []
        while i <= self.countNumOfNews():
            tmp = self.findAndCutString(text, "<title>", "</title>")
            titleList.append(tmp)
            text = self.findAndCutString(text, "</title>")
            i +=1
        #j = 0
        #for j in titleList:
            #print j + "\n"
        return titleList

    def getLink(self):
        i = 1
        text = self.imptXML()
        linkList = []
        while i <= self.countNumOfNews():
            tmp = self.findAndCutString(text, "<link>", "</link>")
            linkList.append(tmp)
            text = self.findAndCutString(text, "</link>")
            i +=1
        #j = 0
        #for j in linkList:
            #print j + "\n"
        return linkList
    def getDesc(self):
        i = 1
        text = self.imptXML()
        descList = []
        while i <= self.countNumOfNews():
            tmp = self.findAndCutString(text, "<description>", "</description>")
            descList.append(tmp)
            text = self.findAndCutString(text, "</description>")
            i +=1
        #j = 0
        #for j in descList:
            #print j + "\n"
        return descList
    def findAndCutString(self, data, findStartWord, findEndWord=None):
        wordStartingPosition = data.find(findStartWord)
        lengthOfFindStartWord = len(findStartWord)
        cutStartPosition = wordStartingPosition + lengthOfFindStartWord
        if findEndWord is None:
            outputText = data[cutStartPosition:]
        else:
            wordEndPosition = data.find(findEndWord)
            cutEndPosition = data.find(findEndWord)
            outputText = data[cutStartPosition:cutEndPosition]

        return outputText
    def countNumOfNews(self):
        counter = self.imptXML().count("<title>")
        #print "there are %d news from RSS." % counter
        return counter
    def RSSReader(self):
        totalNews = self.countNumOfNews()
        print "There are %d news in total." % totalNews
        tmpTitle = self.getTitle()
        tmpLink = self.getLink()
        tmpDesc = self.getDesc()
        i = 1
        while i <= totalNews:

            print "%d. %s" % (i, tmpTitle[i-1])
            print "%s" % tmpDesc[i-1]
            print "Link: %s\n" % tmpLink[i-1]
            i +=1
# reader = readNews(url)
# reader.RSSReader()
#reader.getPubDate()
#print reader.imptXML()

