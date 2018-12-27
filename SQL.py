import pymysql


class SQL:
    MYSQLSERVER = 'k8s.geekfan.top'

    MYSQLUSER = 'root'

    MYSQLPASSWORD = 'GeekCloud'

    MYSQLDATABASE = 'SYSTEMLIB'

    db = pymysql.connect(
        host=MYSQLSERVER,
        port=3310,
        user=MYSQLUSER,
        passwd=MYSQLPASSWORD,
        db=MYSQLDATABASE
    )
    cursor = db.cursor()

    def run(self, command):
        try:
            self.cursor.execute(command)
            self.db.commit()

        except:
            print("Run MYSQL error:")
            print(command)


    def update_char(self, table, data_type, context):
        update_sql = "UPDATE "+str(table)+" SET CONTEXT=\'"+str(context)+"\' WHERE TYPE=\'"+str(
            data_type)+"\'"
        self.run(update_sql)

    def update_num(self, table, data_type, context):
        update_sql = "UPDATE " + str(table) + " SET CONTEXT=" + str(context) + " WHERE TYPE=\'" + str(
            data_type) + "\'"
        self.run(update_sql)
    def close(self):
        self.db.close()
