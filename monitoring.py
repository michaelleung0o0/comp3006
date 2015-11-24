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
        findMList = "select * from monitoring where uid = '" + str(uid) +"'"
        MListResult = self.sql.runSQL(findMList).fetchall()
        return MListResult


m = monitoring(00001, 5)
print(m.requestMList())
                
