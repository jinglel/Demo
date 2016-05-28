import psycopg2

conn=psycopg2.connect(host='localhost',database="hw04",
                      user="dbo",password="123456")
cur=conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a(
     sn      INTEGER,
     name    VARCHAR(5),
     PRIMARY KEY(sn)
);
           ''')
ins_sql='INSERT INTO hw_a(sn,name) VALUES (%s,%s)'
for i in range(6):
     sn=10+i*10
     name='A%d' % sn
     cur.execute(ins_sql,(sn,name))

     
cur.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b(
     sn      INTEGER,
     name    VARCHAR(5),
     PRIMARY KEY(sn)
);
           ''')
ins_sql='INSERT INTO hw_b(sn,name) VALUES (%s,%s)'
for i in range(5):
     sn=40+i*10
     name='B%d' % sn
     cur.execute(ins_sql,(sn,name))



conn.commit()
