import pymysql

map = {
    # Data Type int
    'CPUNUM': 'SYSTEMINT',
    'CPULNUM': 'SYSTEMINT',
    'CPUPER': 'SYSTEMINT',
    'MEMPER': 'SYSTEMINT',
    # Data Type float
    'MEMUSED': 'SYSTEMFLOAT',
    'MEMFREE': 'SYSTEMFLOAT',
    'MEMTOTAL': 'SYSTEMFLOAT',
    'SWAPUSED': 'SYSTEMFLOAT',
    'SWAPFREE': 'SYSTEMFLOAT',
    'SWAPTOTAL': 'SYSTEMFLOAT',
    'GCARDFREE': 'SYSTEMFLOAT',
    'GCARDUSED': 'SYSTEMFLOAT',
    'GCARDTOTAL': 'SYSTEMFLOAT',
    'NETSEND': 'SYSTEMFLOAT',
    'NETRECV': 'SYSTEMFLOAT',
    # Data Type String
    'HOSTNAME': 'SYSTEMCHAR',
    'IP': 'SYSTEMCHAR',
    'GCARDNAME': 'SYSTEMCHAR',
    'GCARDVERSION': 'SYSTEMCHAR',
    # Data Type Time
    'UPTIME': 'SYSTEMTIME',
}


class SQL:
    MYSQLSERVER = 'k8s.geekfan.top'

    MYSQLUSER = 'root'

    MYSQLPASSWORD = 'GeekCloud'

    MYSQLDATABASE = 'SYSTEMLIB'

    db = pymysql.connect(MYSQLSERVER, MYSQLUSER, MYSQLPASSWORD, MYSQLDATABASE)

    cursor = db.cursor()

    def run(self, command):
        try:
            self.cursor.execute(command)
            self.db.commit()

        except:
            self.db.rollback()

    def update(self, table, data_type, context):
        update_sql = "UPDATE "+str(table)+" SET CONTEXT="+str(context)+"WHERE TYPE="+str(data_type)
        self.run(update_sql)

    def close(self):
        self.db.close()
