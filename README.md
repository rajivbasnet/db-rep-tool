### Database Reproduction/Migration Tool

Use Case: To configure the Tables in a local Database exactly as a remote Database for testing purposes
(Currently works for MySQL Databases)


#### File Structure:

.          
├──  details\
│   ├─ columns.py\
│   ├─ tables.py\
├── settings      
│   ├─ config.py\
├── utils    
│   ├─ connect_db.py \
├── reproduce_tables.py\
├── README.md


columns.py contains Columns Class that gives nesesscary attributes and functions to get the configuration for a provided table name
tables.py contains Tables Class for getting all configurations for provided list of tables or all tables


#### Getting Started (Unix environment)
Must be a python 3.8.x environment.

Install pipenv -

    pip install pipenv
Clone repo -

    git clone https://github.com/rajivbasnet/db-rep-tool.git
    cd db-rep-tool
Install all dependencies -

    pipenv install


#### Fill in necessary connection attributes in config.py file: 
* 'read_db' is for the Database to be read and 'local_db' if for the one where you want the tables to be reproduced
*  run reproduce_tables.py to carry out the configuration and reproduction of exact tables in write_db
         ```
         python -m reproduce_tables
         ```
