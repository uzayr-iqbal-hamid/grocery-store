import mysql.connector as c

def create_connection(password):
    conn = c.connect(host="localhost", user="root", passwd=password)
    return conn

def create_database_if_not_exists(conn, dbname):
    mycsr = conn.cursor()
    mycsr.execute("SHOW DATABASES")
    databases = [x[0] for x in mycsr]
    if dbname not in databases:
        mycsr.execute(f"CREATE DATABASE {dbname}")
    conn.database = dbname

def create_tables_if_not_exists(conn):
    mycsr = conn.cursor()
    mycsr.execute("SHOW TABLES")
    tables = [x[0] for x in mycsr]

    table_queries = {
        'inv_cooking_essentials': """
            CREATE TABLE inv_cooking_essentials (
                item_code VARCHAR(10) PRIMARY KEY,
                item_name VARCHAR(250) NOT NULL,
                cost_price INT NOT NULL,
                selling_price INT NOT NULL,
                quantity INT NOT NULL,
                expiry_date VARCHAR(11) NOT NULL
            )
        """,
        # Add similar entries for other categories
        'inv_household_supplies': """
            CREATE TABLE inv_household_supplies (
                item_code VARCHAR(10) PRIMARY KEY,
                item_name VARCHAR(250) NOT NULL,
                cost_price INT NOT NULL,
                selling_price INT NOT NULL,
                quantity INT NOT NULL,
                expiry_date VARCHAR(11) NOT NULL
            )
        """,
        'inv_stationery': """
            CREATE TABLE inv_stationery (
                item_code VARCHAR(10) PRIMARY KEY,
                item_name VARCHAR(250) NOT NULL,
                cost_price INT NOT NULL,
                selling_price INT NOT NULL,
                quantity INT NOT NULL,
                expiry_date VARCHAR(11) NOT NULL
            )
        """,
        'inv_snacks': """
            CREATE TABLE inv_snacks (
                item_code VARCHAR(10) PRIMARY KEY,
                item_name VARCHAR(250) NOT NULL,
                cost_price INT NOT NULL,
                selling_price INT NOT NULL,
                quantity INT NOT NULL,
                expiry_date VARCHAR(11) NOT NULL
            )
        """,
        'inv_beauty_products': """
            CREATE TABLE inv_beauty_products (
                item_code VARCHAR(10) PRIMARY KEY,
                item_name VARCHAR(250) NOT NULL,
                cost_price INT NOT NULL,
                selling_price INT NOT NULL,
                quantity INT NOT NULL,
                expiry_date VARCHAR(11) NOT NULL
            )
        """,
        'inv_drinks': """
            CREATE TABLE inv_drinks (
                item_code VARCHAR(10) PRIMARY KEY,
                item_name VARCHAR(250) NOT NULL,
                cost_price INT NOT NULL,
                selling_price INT NOT NULL,
                quantity INT NOT NULL,
                expiry_date VARCHAR(11) NOT NULL
            )
        """
    }

    for table, query in table_queries.items():
        if table not in tables:
            mycsr.execute(query)

