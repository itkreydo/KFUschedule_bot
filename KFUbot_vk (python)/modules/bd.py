import sqlite3

class bd:
    def __init__(self,file):
        self.conn = sqlite3.connect(file)
        self.c = self.conn.cursor()
        self.file=file
    def select(self,sql,args,isset=False):
        if (self.c.execute(sql,args)):
            results = self.c.fetchall()
            if (isset==True):
                return True if len(results) !=0 else False
            return results
        else:
            return False
    def insert(self,sql,args):
        if (self.c.execute(sql,args)):
            self.conn.commit()
            return True
        else:
            self.conn.commit()
            return False
    def update(self,sql,args):
        if (self.c.execute(sql,args)):
            self.conn.commit()
            return True
        else:
            self.conn.commit()
            return False
    def createConn(self):
        self.conn = sqlite3.connect(self.file)
        self.c = self.conn.cursor()
    def close(self):
        self.c.close()
        self.conn.close()



