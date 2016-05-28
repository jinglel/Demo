import psycopg2

import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

conn=psycopg2.connect(host='localhost',
                      database="hw04",user="dbo",password="123456")

with conn.cursor() as cur:
     sql='''
     SELECT a,b
     FROM hw_a as a
     RIGHT JOIN hw_b as b
     ON a.sn=b.sn
     WHERE a.sn is null;
     '''
     cur.execute(sql)
     for row in cur:
          print('%s,%s' %( row[0],row[1]))

conn.commit()
