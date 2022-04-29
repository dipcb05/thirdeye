import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error as error


class Database:
    def __init__(self):
        self.p = None
        self.u = None
        self.d = None
        self.un = "root"
        self.pw = "abcdef12"
        self.localhost = "127.0.0.1"
        self.dbname = "tech_eye"

    def db_connect(self):

        try:
            mydb = mysql.connector.connect(
                host=self.localhost,
                user=self.un,
                password=self.pw,
                database=self.dbname
            )

        except error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something wrong with your username or password, want to create user?")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        else:
            self.u = self.un
            self.p = self.pw
            self.d = self.dbname

        return self.u, self.p, self.d


if __name__ == '__main__':
    t = Database()
    a = t.db_connect()
