from details.columns import Columns

from details.columns import Columns


class Tables:
    def __init__(self, cursor, tables='all'):
        """
        params: cursor object of the database connection and list of table names or a string 'all' that gets all tables
        """
        self.cursor = cursor
        if isinstance(tables, str) and 'all' in tables.lower():
            self.get_table_names()
        elif isinstance(tables, list):
            self.table_names = tables
        else:
            print('please provide a list of the name of tables...')
            return
        self.get_tables_config()

    def get_table_names(self):
        """
        this function gets the list of tables from a provider cursor of a database connection object
        assigns a list ot tables in the cursor to tables attribute
        """

        query = 'show tables;'

        try:
            self.cursor.execute(query)
            tables = self.cursor.fetchall()
            tables = [each for (each, ) in tables]
            self.table_names = tables
        except (Exception) as error:
            print("error retrieving table names...", error)

    def get_tables_config(self):
        """
        this function gets the dictionaty of tables with the config of its columns from a list of tables names
        assigns dictionary to tables_config attribute that contains the configuration for each columns of all tables
        """
        tables_config = {}

        for each in self.table_names:
            cols = Columns(self.cursor, each)
            col_type_config = cols.columns_type_config
            col_size_config = cols.columns_size_config
            if not bool(col_type_config):
                print(
                    f'cannot retrive columns config for table: \'{each}\', please check if table \'{each}\' exists..')
                continue
            else:
                print(f'config retrieved successfully for table: \'{each}\'')

            # to fix column size while getting table configuration dictionary
            for col_name, col_type in col_type_config.items():
                if col_name in col_size_config.keys():
                    col_type_config[col_name] = col_type_config[col_name] + \
                        f"({col_size_config[col_name]})"

            tables_config[each] = col_type_config

        self.tables_config = tables_config
        self.table_names = [*self.tables_config]
