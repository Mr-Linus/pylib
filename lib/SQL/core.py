import pymysql  # import MySQLdb   as pymysql
from settings import MYSQLConfig


class SQL:
    MYSQLSERVER = MYSQLConfig['MYSQLSERVER']
    port = MYSQLConfig['port']
    MYSQLUSER = MYSQLConfig['MYSQLUSER']
    MYSQLPASSWORD = MYSQLConfig['MYSQLPASSWORD']
    MYSQLDATABASE = MYSQLConfig['MYSQLDATABASE']

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

        sql = "UPDATE "+str(table)+" SET CONTEXT=\'"+str(context)+"\' WHERE TYPE=\'"+str(
            data_type)+"\'"
        self.run(sql)

    def update_num(self, table, data_type, context):
        sql = "UPDATE " + str(table) + " SET CONTEXT=" + str(context) + " WHERE TYPE=\'" + str(
            data_type) + "\'"
        self.run(sql)

    def create_db(self, db_name):
        sql = "CRATE DATABASE IF NOT EXISTS " + str(db_name)
        self.run(sql)

    def create_table(self, table_name, list_name):
        sql = "CREATE TABLE " + str(table_name) + " ( "+str(list_name) + " ) "
        self.run(sql)

    def alter_table_field_add(self, table_name, field, type_size):
        sql = "ALTER TABLE " + str(table_name) + " ADD " + str(field) + " " + str(type_size)
        self.run(sql)

    def alter_table_rename(self, table_name, new_name):
        sql = "ALTER TABLE " + str(table_name) + " RENAME " + str(new_name)
        self.run(sql)

    def alter_table_field_modify(self, table_name, field, type_size):
        sql = "ALTER TABLE " + str(table_name) + " MODIFY " + str(field) + " " + str(type_size)
        self.run(sql)

    def alter_table_field_rename(self, table_name, field_old_name, field_new_name, type_size):
        sql = "ALTER TABLE " + str(table_name) + " CHANGE " + str(field_old_name) + " "\
              + str(field_new_name) + " " + str(type_size)
        self.run(sql)

    def delete_table(self, table_name):
        sql = "DROP TABLE " + str(table_name)
        self.run(sql)

    def delete_table_field(self, table_name, field_name):
        sql = "ALTER TABLE " + str(table_name) + " DROP " + str(field_name)
        self.run(sql)

    def delete_char(self, table, data_type, context):
        sql = "DELETE FROM" + str(table) + "\' WHERE " + str(data_type) + \
              " = \'" + str(context)+"\'"
        self.run(sql)

    def delete_num(self, table, data_type, context):
        sql = "DELETE FROM" + str(table) + "\' WHERE " + str(data_type) + \
              " = " + str(context)
        self.run(sql)

    def insert(self, table, context):
        sql = "INSERT INTO " + str(table) + " VALUES (" + str(context) + ")"
        self.run(sql)

    def delete_db(self, db_name):
        sql = "DROP DATABASE IF EXISTS " + str(db_name)
        self.run(sql)

    def change_db(self, db_name):
        sql = "USE " + str(db_name)
        self.run(sql)

    def close(self):
        self.db.close()
