import mysql.connector
import typing as t
import json


server = 'project4.mysql.database.azure.com'
database = 'project4'
username = 'project4'
password = '12345ssdlh@'
driver= '{ODBC Driver 17 for SQL Server}'
ssl = '/Users/maokeying/Downloads/DigiCertGlobalRootCA.crt.pem'

select_all_query = """
SELECT * FROM %s;
"""

find_range = """
SELECT MAX(charges)-MIN(charges) FROM Insurance
"""

    
def get_cnx():
    cnx = mysql.connector.connect(user=username, 
                                    password=password, 
                                    host=server, 
                                    port=3306, 
                                    database=database, 
                                    ssl_ca=ssl, 
                                    ssl_disabled=False, 
                                    autocommit=True)
    return cnx

def run_query(query: str):
    cnx = mysql.connector.connect(user=username, 
                                    password=password, 
                                    host=server, 
                                    port=3306, 
                                    database=database, 
                                    ssl_ca=ssl, 
                                    ssl_disabled=False, 
                                    autocommit=True)
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    json_results = json.dumps(result)
    return json_results

def get_range_for_charge():
    cnx = mysql.connector.connect(user=username, 
                                    password=password, 
                                    host=server, 
                                    port=3306, 
                                    database=database, 
                                    ssl_ca=ssl, 
                                    ssl_disabled=False, 
                                    autocommit=True)
    cursor = cnx.cursor()
    cursor.execute(find_range)
    result = cursor.fetchall()
    return result[0][0]
