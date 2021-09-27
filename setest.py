import psycopg2

try:
  conn = psycopg2.connect("dbname='bc_db' user='jc' host='52.141.16.47' password='keti'")
except:
  print ("not connect")

cur = conn.cursor()

try:
  #sqlString = "INSERT INTO spec (ID, Process information, Process Architecture, RAM Size) VALUES (%s, %s, %s, %s);"
  print("first check point ok")
  #cur.execute(sqlString, ("test2", "cpu", "intel","12(gb)") )
  cur.execute("select * from spec")
  print("second check point ok")

  rows = cur.fetchall()
  for row in rows:
    print(row)
except:
  print ("cannot SQL Execute")

conn.commit()
cur.close()
conn.close()
