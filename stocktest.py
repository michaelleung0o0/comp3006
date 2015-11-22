from xmlReader import xmlReader
#http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=00001
#url = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode=00002"
url = "http://202.125.90.199/securityQuote/genStockXMLHK.php?stockcode="
con = None

class searchStock():
    def __init__(self, url, stockCode):
        self.xmlread = xmlReader(url, stockCode, stockCode + '.xml')
        self.url = url
        self.stockCode = stockCode
        self.xmlread.requestXML()
        
    def displayAllXML(self):
        #print url
        with open (self.stockCode + '.xml', "r") as myfile:
            content = myfile.read().decode('utf-8')
        
        return content
    def getSymbol(self):
        symbol = self.displayAllXML()
        symbol = self.findAndCutString(symbol, "<symbol>", "</symbol>")
        return symbol
    def getEnName(self):
        name = self.displayAllXML()
        name = self.findAndCutString(name, "<english><![CDATA[", "]]></english>")
        return name
    def getTCName(self):
        name = self.displayAllXML()
        name = self.findAndCutString(name, "<chinese><![CDATA[", "]]></chinese>")
        return name
    def getSCName(self):
        name = self.displayAllXML()
        name = self.findAndCutString(name, "<sChinese><![CDATA[", "]]></sChinese>")
        return name
    def getSSPN(self):
        sspn = self.displayAllXML()
        sspn = self.findAndCutString(sspn, "<sspn>", "</sspn>")
        return sspn
    def getPrice(self):
        price = self.displayAllXML()
        price = self.findAndCutString(price, "<price>", "</price>")
        return price
    def getChange(self):
        change = self.displayAllXML()
        change = self.findAndCutString(change, "<change>", "</change>")
        return change
    def getPctChange(self):
        pctChange = self.displayAllXML()
        pctChange = self.findAndCutString(pctChange, "<pct_change>", "</pct_change>")
        return pctChange
    def getPexit(self):
        pexit = self.displayAllXML()
        sspn = self.findAndCutString(pexit, "<pexit>", "</pexit>")
        return sspn
    def getOpen(self):
        openv = self.displayAllXML()
        openv = self.findAndCutString(openv, "<open>", "</open>")
        return sspn
    def getHigh(self):
        high = self.displayAllXML()
        high = self.findAndCutString(high, "<high>", "</high>")
        return sspn
    def getLow(self):
        low = self.displayAllXML()
        low = self.findAndCutString(sspn, "<low>", "</low>")
        return sspn
    def getBid(self):
        bid = self.displayAllXML()
        bid = self.findAndCutString(bid, "<bid>", "</bid>")
        return sspn
    def getAsk(self):
        ask = self.displayAllXML()
        ask = self.findAndCutString(ask, "<ask>", "</ask>")
        return sspn
    def getYearHigh(self):
        yearHigh = self.displayAllXML()
        sspn = self.findAndCutString(yearHigh, "<year_high>", "</year_high>")
        return yearHigh
    def getYearLow(self):
        yearLow = self.displayAllXML()
        yearLow = self.findAndCutString(yearLow, "<year_low>", "</year_low>")
        return yearLow
    def getVolume(self):
        volume = self.displayAllXML()
        volume = self.findAndCutString(volume, "<volume>", "</volume>")
        return volume
    def getTurnover(self):
        turnover = self.displayAllXML()
        turnover = self.findAndCutString(turnover, "<turnover>", "</turnover>")
        return turnover
    def getPE(self):
        pe = self.displayAllXML()
        pe = self.findAndCutString(pe, "<pe>", "</pe>")
        return pe
    def getMarketCapital(self):
        marketCapital = self.displayAllXML()
        marketCapital = self.findAndCutString(marketCapital, "<market_capital>", "</market_capital>")
        return marketCapital
    def getMonthHigh(self):
        monthHigh = self.displayAllXML()
        monthHigh = self.findAndCutString(monthHigh, "<month_high>", "</month_high>")
        return monthHigh
    def getMonthLow(self):
        monthLow = self.displayAllXML()
        monthLow = self.findAndCutString(monthLow, "<month_low>", "</month_low>")
        return monthLow
    def getLot(self):
        lot = self.displayAllXML()
        lot = self.findAndCutString(lot, "<lot>", "</lot>")
        return lot
    def getDPS(self):
        dps = self.displayAllXML()
        dps = self.findAndCutString(dps, "<dps>", "</dps>")
        return dps
    def getEPS(self):
        eps = self.displayAllXML()
        eps = self.findAndCutString(eps, "<eps>", "</eps>")
        return eps
    def getRSI10(self):
        rsi10 = self.displayAllXML()
        rsi10 = self.findAndCutString(rsi10, "<rsi>", "</rsi>")
        rsi10 = self.findAndCutString(rsi10, "<d10>", "</d10>")
        return rsi10
    def getRSI14(self):
        rsi14 = self.displayAllXML()
        rsi14 = self.findAndCutString(rsi14, "<rsi>", "</rsi>")
        rsi14 = self.findAndCutString(rsi14, "<d14>", "</d14>")
        return rsi14
    def getRSI20(self):
        rsi20 = self.displayAllXML()
        rsi20 = self.findAndCutString(rsi20, "<rsi>", "</rsi>")
        rsi20 = self.findAndCutString(rsi20, "<d20>", "</d20>")
        return rsi20
    def getMA10(self):
        ma10 = self.displayAllXML()
        ma10 = self.findAndCutString(ma10, "<ma>", "</ma>")
        ma10 = self.findAndCutString(ma10, "<d10>", "</d10>")
        return ma10
    def getMA20(self):
        ma20 = self.displayAllXML()
        ma20 = self.findAndCutString(ma20, "<ma>", "</ma>")
        ma20 = self.findAndCutString(ma20, "<d20>", "</d20>")
        return ma20
    def getMA50(self):
        ma50 = self.displayAllXML()
        ma50 = self.findAndCutString(ma50, "<ma>", "</ma>")
        ma50 = self.findAndCutString(ma50, "<d50>", "</d50>")
        return ma50
    def getRelatedStock(self):
        relatedStock = self.displayAllXML()
        relatedStock = self.findAndCutString(relatedStock, "<relatedStock>", "</relatedStock>")
        return relatedStock
    def getIssuedShare(self):
        issueShare = self.displayAllXML()
        issueShare = self.findAndCutString(issueShare, "<issueShare>", "</issueShare>")
        return issueShare
    def getGearing(self):
        gearing = self.displayAllXML()
        gearing = self.findAndCutString(gearing, "<gearing>", "</gearing>")
        return gearing
    def getPremium(self):
        premium = self.displayAllXML()
        premium = self.findAndCutString(premium, "<premium>", "</premium>")
        return sspn
    def getCurrency(self):
        currency = self.displayAllXML()
        currency = self.findAndCutString(currency, "<currency>", "</currency>")
        return currency
    def getDate(self):
        date = self.displayAllXML()
        date = self.findAndCutString(date, "<date>", "</date>")
        return date
    
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





ss = searchStock(url, '00001')
#print ss.displayAllXML()
print ss.getSymbol()
print ss.getEnName()
print ss.getTCName()
print ss.getSCName()
print ss.getSSPN()
print ss.getMA50()



