import MySQLdb

class sql_connector():
    def __init__(self):
        self.db = 'spaceapp_laravel'
        self.user = 'spaceapp'
        self.password = 'spaceapp'
        self.host = 'localhost'

    def Q(self,sql):
        try:
            db = MySQLdb.connect(self.host, self.user, self.password, self.db)
            curs = db.cursor()
            curs.execute(sql)
            results = curs.fetchall()
            db.commit()
            curs.close()
            db.close()
            return results
        except:
            print("kupa")


    def read(self):
        print("")
    def write(self,sql):
        print("write")
    def test(self):
        try:
            db = MySQLdb.connect(self.host, self.user,
                                 self.password, self.db)
            cursor = db.cursor()
            cursor.execute("SELECT VERSION()")
            results = cursor.fetchone()
            # Check if anything at all is returned
            if results:
                return results
            else:
                return False
        except MySQLdb.Error:
            print("ERROR IN CONNECTION")
        return False
if __name__ == "__main__":

    s = sql_connector()
    sql = "SELECT * FROM `test`"
    #sql = "SELECT * FROM `test`"
    k = s.Q(sql=sql)
    print(k)
    #ww = s.test()
    #print(ww)
