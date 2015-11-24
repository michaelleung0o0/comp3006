from SQLOp import sqlConnection

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


m = monitoring(00001, 5)
#print(m.requestMList())
var = m.requestMList()
print(var)[0]
                
