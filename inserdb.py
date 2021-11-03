import psycopg2
import json
from typing import ItemsView, KeysView, ValuesView

#connected
try:
  conn = psycopg2.connect("dbname='bc_db' user='jc' host='52.141.16.47' port = '5433' password='keti'")
except:
  print ("not connect")

#Creating a cursor object using the cursor() method and open json_file
with open("records.json", 'r', encoding= 'UTF-8' ) as json_file:
  cursor = conn.cursor()
  data = json.load(json_file)
  ID = data['ID']
  PI = data['Process_Information']
  PA = data['Process_Architecture']
  RAM = data['RAM_Size']
  sqlString = ('''INSERT INTO sb.spec("ID", "Process_Information", "Process_Architecture", "RAM_Size") VALUES ( %s, %s, %s, %s ) ''')
  cursor.execute( sqlString, ( ID , PI , PA , RAM ))

# Commit your changes in the database
conn.commit()
print("Records inserted........")
print("Record complite!")

# Closing the connection
conn.close()
