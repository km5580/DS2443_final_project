import mysql.connector
import pandas as pd

server = 'project4.mysql.database.azure.com'
database = 'project4'
username = 'project4'
password = '12345ssdlhi@'
driver= '{ODBC Driver 17 for SQL Server}'
ssl = '/Users/linxia/Downloads/DigiCertGlobalRootCA.crt.pem'
query = """
CREATE TABLE IF NOT EXISTS Insurance (
age INTEGER(20),
sex CHAR(20),
bmi FLOAT(20),
children INTEGER(20),
smoker CHAR(20),
region CHAR(20),
charges FLOAT(20)
);
"""

cnx = mysql.connector.connect(user=username, password=password, host=server, port=3306, database=database, ssl_ca=ssl, ssl_disabled=False, autocommit=True)
cursor = cnx.cursor()
df = pd.read_csv("insurance.csv")

try:
    cursor.execute(query)
    for index, row in df.iterrows():
        insert_query = f"INSERT INTO Insurance Values ({row.age}, \"{row.sex}\", {row.bmi}, {row.children}, \"{row.smoker}\", \"{row.region}\", {row.charges});"
        cursor.execute(insert_query)
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
