from SQLOp import sqlConnection
from stocktest import searchStock

host = "localhost"
user = "admin"
pw = "123456"
db = "stockdb"


class monitoring():
    def __init__(self, stockCode, refreshRate):
        self.refreshRate = refreshRate
        self.sql = sqlConnection(host, user, pw, db)
        
        
    def requestMList(self):
        i = 1
        findUIDSQL = "select uid from userinfo where username = '" + user +"'"
        uidL = self.sql.runSQL(findUIDSQL).fetchall()[0]
        uid = uidL[0]
        findMList = "select s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 from monitoring where uid = '" + str(uid) +"'"
        MListResult = self.sql.runSQL(findMList).fetchall()
        return MListResult[0]

#BELOW METHODS ARE NOT FINISHED!!!!!!!!!!!!!!!!!!!!

    def getMCName(self):
        return MCNameList
    def getMSCName(self):
        return MSCNameList
    def getMEName(self):
        return MENameList
    def getMPrice(self):
        return MPriceList
    def getMSSPN(self):
        return MSSPNList
    def getMChange(self):
        return MChangeList
    def getMPctChange(self):
        return MPctChangeList
    def getMPexit(self):
        return MPexitList
    def getMOpen(self):
        return MOpenList
    def getMHigh(self):
        return MHighList
    def getMLow(self):
        return MLowList
    def getMYearHigh(self):
        return MYearHighList
    def getMyearLow(self):
        return MYearLowList
    def getMVolume(self):
        return MVolumeList
    def getMTurnover(self):
        return MTurnoverList
    def getMPE(self):
        return MPEList
    def getMMonthHigh(self):
        return MMonthHighList
    def getMMonthLow(self):
        return MMonthLowList
    def getMLot(self):
        return MLotList
    def getMDPS(self):
        return MDPSList
    def getMEPS(self):
        return MEPSList
    def getMRSI10(self):
        return MRSI10List
    def getMRSI14(self):
        return MRSI14List
    def getMRSI20(self):
        return MRSI20List
    def getMA10(self):
        return MMA10List
    def getMA20(self):
        return MMA20List
    def getMA50(self):
        return MMA50List
    def getMIssuedShare(self):
        return MIssuedShareList
    def getMDate(self):
        return MDateList

#END NOT DONE METHODS!!!!!!!!!!!!



    

#m = monitoring(00001, 5)
#print(m.requestMList())
#var = m.requestMList()
#print(var)[0]
                
