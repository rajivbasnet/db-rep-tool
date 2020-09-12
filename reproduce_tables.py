from settings.config import DATABASES
from details.tables import Tables
from details.tables import Columns
from utils.connect_db import get_mysql_conn, get_mysql_engine

def get_create_table_query(table, config):
    """
    this function creates the query in order to create a table with given config
    params: table(string), config(dictionary of column names and their data type (size))
    returns string
    """
    
    #fixes for datatypes and primary key
    text = []
    for key, value in config.items():
        print(value)
        if "mediumtext" in value:   #needs resolution for mediumtext types
            continue
#         if key == 'id':
#             if 'varchar' in value.lower() or 'text' in value.lower():
#                 if 'text' in value.lower():
#                     text.append(f'`{key}` {value.upper()} NOT NULL PRIMARY KEY')
#                 else:
#                     text.append(f'`{key}` {value.upper()} NOT NULL PRIMARY KEY')
#             else:
#                 text.append(f'`{key}` {value.upper()} NOT NULL AUTO_INCREMENT PRIMARY KEY')
            
#         else:
        text.append(f'`{key}` {value.upper()}')
            
    column_spec = ", ".join(text)
    column_spec = f"( {column_spec} );"
    
    create_table_query = f"""CREATE TABLE IF NOT EXISTS `{table}` {column_spec}"""
    return create_table_query


def reproduce():
    read_conn = get_mysql_conn(DATABASES['read_db'])
    if read_conn:
        read_cursor = read_conn.cursor()
    
    write_conn = get_mysql_conn(DATABASES['local_db'])
    if write_conn:
        write_cursor = write_conn.cursor()

    t = Tables(read_cursor)
    
    for each in t.table_names:
        query = get_create_table_query(each, t.tables_config[each])
        print(query, "\n")
        write_cursor.execute(query)
        print(each)

if __name__ == "__main__":
    # USAGE/TEST:
    reproduce()
    print("All tables reproduced successfully")
