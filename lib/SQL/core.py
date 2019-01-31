# You need to change it if you run it on raspberryPi
# by the following command:
#   import MySQLdb as pymysql
import pymysql

# You need to rename settings-example.py
# to the settings.py in the current folder
# and set the database infomation in this file.
from settings import MYSQLConfig


class SQL:
    """
    This class is used to implement CRUD for the database.
    """

    MYSQLSERVER = MYSQLConfig['MYSQLSERVER']
    port = MYSQLConfig['port']
    MYSQLUSER = MYSQLConfig['MYSQLUSER']
    MYSQLPASSWORD = MYSQLConfig['MYSQLPASSWORD']
    MYSQLDATABASE = MYSQLConfig['MYSQLDATABASE']

    # Instantiated class by the para in settings.py
    db = pymysql.connect(
        host=MYSQLSERVER,
        port=3310,
        user=MYSQLUSER,
        passwd=MYSQLPASSWORD,
        db=MYSQLDATABASE
    )
    # Instantiated cursor
    cursor = db.cursor()

    def run(self, command):
        """
        Description: Used to run sql commands.
        :param command: sql command
        :return: SQL command execution status.
        """
        try:
            self.cursor.execute(command)
            return self.db.commit()

        except:
            print("Run MYSQL error:")
            print(command)
            return command

    def update_char(self, table, data_type, context):
        """
        Description: Used to update the data of char type.
        :param table: Data table to which the data belongs.
        :param data_type: Data's type.
        :param context: Data's contexts.
        :return: SQL command execution status.
        """
        sql = "UPDATE "+str(table)+" SET CONTEXT=\'"+str(context)+"\' WHERE TYPE=\'"+str(
            data_type)+"\'"
        return self.run(sql)

    def update_num(self, table, data_type, context):
        """
        Description: Used to update the data of number type.
        :param table: Data table to which the data belongs.
        :param data_type: Data's type.
        :param context: Data's contexts.
        :return: SQL command execution status.
        """
        sql = "UPDATE " + str(table) + " SET CONTEXT=" + str(context) + " WHERE TYPE=\'" + str(
            data_type) + "\'"
        return self.run(sql)

    def create_db(self, db_name):
        """
        Description: Used to create the database.
        :param db_name: database's name you create.
        :return: SQL command execution status.
        """
        sql = "CRATE DATABASE IF NOT EXISTS " + str(db_name)
        return self.run(sql)

    def create_table(self, table_name, list_name):
        """
        Description: Used to create the table.
        :param table_name: table's name you create.
        :param list_name: structure of tables you want to set. e.g: "int(20),float(20)"
        :return: SQL command execution status.
        """
        sql = "CREATE TABLE " + str(table_name) + " ( "+str(list_name) + " ) "
        return self.run(sql)

    def alter_table_field_add(self, table_name, field, type_size):
        """
        Description: Used to add new field of the table.
        :param table_name: table's name.
        :param field: New field name.
        :param type_size: Field type and type size. e.g: int(20)
        :return: SQL command execution status.
        """
        sql = "ALTER TABLE " + str(table_name) + " ADD " + str(field) + " " + str(type_size)
        return self.run(sql)

    def alter_table_rename(self, table_name, new_name):
        """
        Description: Used to rename the table's name.
        :param table_name: old table name
        :param new_name: new table name
        :return: SQL command execution status.
        """
        sql = "ALTER TABLE " + str(table_name) + " RENAME " + str(new_name)
        return self.run(sql)

    def alter_table_field_modify(self, table_name, field, type_size):
        """
        Description: Used to modify the field type and type size.
        :param table_name: the table which the field belongs.
        :param field: the field name.
        :param type_size: field type and field size. e.g: int(20)
        :return: SQL command execution status.
        """
        sql = "ALTER TABLE " + str(table_name) + " MODIFY " + str(field) + " " + str(type_size)
        return self.run(sql)

    def alter_table_field_rename(self, table_name, field_old_name, field_new_name, type_size):
        """
        Description: Used to rename the field name and change the field type
        and type size.
        :param table_name: the table which the field belongs.
        :param field_old_name: the old field name
        :param field_new_name: new field name
        :param type_size: field type and field size. e.g: int(20)
        :return: SQL command execution status.
        """
        sql = "ALTER TABLE " + str(table_name) + " CHANGE " + str(field_old_name) + " "\
              + str(field_new_name) + " " + str(type_size)
        return self.run(sql)

    def delete_table(self, table_name):
        """
        Description: Delete the specified tables.
        :param table_name: table's name.
        :return: SQL command execution status.
        """
        sql = "DROP TABLE " + str(table_name)
        return self.run(sql)

    def delete_table_field(self, table_name, field_name):
        """
        Description: Delete the specified field name.
        :param table_name: the table which the field belongs.
        :param field_name: the field which need to be deleted.
        :return: SQL command execution status.
        """
        sql = "ALTER TABLE " + str(table_name) + " DROP " + str(field_name)
        return self.run(sql)

    def delete_char(self, table, data_type, context):
        """
        Descrption: Delete the specified data of char type.
        :param table: the table which the data belongs.
        :param data_type: data's type.
        :param context: data's context.
        :return: SQL command execution status.
        """
        sql = "DELETE FROM" + str(table) + "\' WHERE " + str(data_type) + \
              " = \'" + str(context)+"\'"
        return self.run(sql)

    def delete_num(self, table, data_type, context):
        """
        Descrption: Delete the specified data of number type.
        :param table: the table which the data belongs.
        :param data_type: data's type.
        :param context: data's context.
        :return: None
        """
        sql = "DELETE FROM" + str(table) + "\' WHERE " + str(data_type) + \
              " = " + str(context)
        return self.run(sql)

    def insert(self, table, context):
        """
        Description: Add the data in the databases.
        :param table: the table which data belongs.
        :param context: the context of the data
        :return: None
        """
        sql = "INSERT INTO " + str(table) + " VALUES (" + str(context) + ")"
        return self.run(sql)

    def delete_db(self, db_name):
        """
        Description: Delete the database.
        :param db_name: the database which need to be deleted.
        :return: SQL command execution status.
        """
        sql = "DROP DATABASE IF EXISTS " + str(db_name)
        return self.run(sql)

    def change_db(self, db_name):
        """
        Description: Change the operation database.
        :param db_name: database name.
        :return: SQL command execution status.
        """
        sql = "USE " + str(db_name)
        return self.run(sql)

    def close(self):
        """
        Description: Close the connection with Database service.
        :return: The status of Closing the connection with Database service.
        """
        return self.db.close()
