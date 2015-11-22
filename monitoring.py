from SQLOp import sqlConnection

host = 


class monitoring():
    def __init__(self, stockCode, refreshRate):
        self.refreshRate = refreshRate
        self.sql = sqlConnection(host, user, pw, db)
    def requestMList:
        i = 1
        findUIDSQL = "select uid from userinfo where username = '" + user +"'"
        uid = sql.printSQLResult(findUIDSQL)[0]
        findMList = "select * from monitoring where uid = '" + user +"'"
        while i <=20:
            
