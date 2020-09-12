class Columns:
    def __init__(self, cursor, table_name):
        """
        params: cursor object of the database connection and name of the table
        """
        self.cursor = cursor
        self.table_name = table_name
        self.get_column_names()
        self.get_columns_config()

    def get_column_names(self):
        """
        this function gets the list of all columns from a given table
        assigns a list ot columns in the cursor to columns attribute
        """

        query = f"""SELECT column_name
                FROM information_schema.columns
                WHERE table_name = '{self.table_name}'"""

        try:
            self.cursor.execute(query)
            columns = self.cursor.fetchall()
            columns = [each for (each, ) in columns]
            self.column_names = columns
        except (Exception) as error:
            print(
                f"error retrieving columnn names for table: \'{self.table_name}\' ", error)

    def get_columns_config(self):
        """
        this function gets the dictionaty of column names and their data types form given tablename
        assigns a dictionary of all columns with their data_type to columns_type_config attribute
        assigns a dictionary of all columns with their data_type to columns_size_config attribute (if size is not None and col_size != 65535)
        """

        query = f"""SELECT column_name, data_type, character_maximum_length
                FROM information_schema.columns
                WHERE table_name = '{self.table_name}'"""

        try:
            self.cursor.execute(query)
            details = self.cursor.fetchall()
            columns_type_config = {col_name: col_type for col_name, col_type, col_size in details}
            columns_size_config = {col_name: col_size for col_name, col_type, col_size in details if col_size is not None}
            self.columns_type_config = columns_type_config
            self.columns_size_config = columns_size_config
        except (Exception) as error:
            print(
                f"error retrieving columnn configurations for table: \'{self.table_name}\' ", error)


if __name__ == "__main__":
    # USAGE/TEST:
    from utils.connect_db import get_mysql_conn, get_mysql_engine
    from settings.config import DATABASES
    conn = get_mysql_conn(DATABASES['read_db'])
    cursor = conn.cursor()
    print("enter table name to get info: ")
    t = input()
    c = Columns(cursor, t)
    print("TABLE NAME :\n", c.table_name)
    print("COLUMNS: \n", c.column_names)
    print("DATA TYPE: \n", c.columns_size_config)
    print("SIZE: \n", c.columns_type_config)
