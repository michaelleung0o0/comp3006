import MySQLdb

class sqlConnection:
    def __init__(self, host, user, pw, db):
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db

    def connectProcess(self):
        db = MySQLdb.connect(self.host, self.user, self.pw, self.db)
        return db

    def runSQL(self, SQLStatement):
        cur = self.connectProcess().cursor()
        cur.execute(SQLStatement)
        #for row in cur.fetchall():
            #print row[0]
            #print row[1]
        return cur
    def printSQLResult(self, SQLStatement):
        for row in self.runSQL(SQLStatement).fetchall():
            print row[0]
            print row[1]


sc = sqlConnection("localhost", "admin", "123456", "comp2018db")
#sc.runSQL("select * from bookmark")
sc.printSQLResult("select * from bookmark")
        
