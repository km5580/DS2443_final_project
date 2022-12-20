import mysql.connector
import pandas as pd
import numpy as np

server = 'project4.mysql.database.azure.com'
database = 'project4'
username = 'project4'
password = '12345ssdlh@'
driver= '{ODBC Driver 17 for SQL Server}'
ssl = '/Users/linxia/Downloads/DigiCertGlobalRootCA.crt.pem'
query = """
CREATE TABLE IF NOT EXISTS disease (
age FLOAT(20),
gender CHAR(20),
height INTEGER(20),
weight FLOAT(20),
ap_hi INTEGER(20),
ap_lo INTEGER(20),
chloesterol INTEGER(20),
gluc INTEGER(20),
smoke CHAR(1),
alco  CHAR(1),
active CHAR(1),
cardio CHAR(1)
);
"""

cnx = mysql.connector.connect(user=username, password=password, host=server, port=3306, database=database, ssl_ca=ssl, ssl_disabled=False, autocommit=True)
cursor = cnx.cursor()
df = pd.read_csv("cardio_train.csv", sep = ";")
df = df.drop("id", axis = 1)
df["age"] = np.round(df["age"]/365.25)
df["gender"] = df["gender"].map({2:1, 1:0})

try:
    cursor.execute(query)
    for index, row in df.iterrows():
        insert_query = f"INSERT INTO disease Values ({row.age}, {row.gender}, {row.height}, {row.weight}, {row.ap_hi}, {row.ap_lo}, {row.cholesterol}, {row.gluc}, {row.smoke}, {row.alco}, {row.active}, {row.cardio});"
        cursor.execute(insert_query)
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
