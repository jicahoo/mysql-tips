
#!/usr/bin/python
import MySQLdb

# sudo apt-get install python-mysqldb

def gen_insert_sql(size):
    sql = "INSERT INTO world (device,temperature,high) values "
    import random
    rows = []
    for i in range(1,size):
        d_i = random.randint(1,100)
        d_v = 'dev_%s' % str(d_i)
        t_v = random.randint(1,100)
        h_v = True if random.randint(1,100)%2 == 0 else False
        row = "('%s',%s, %s)" % (d_v, t_v, str(h_v).lower())
        rows.append(row)

    sql += ','.join(rows)
    sql += ';'
    return sql

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="123456",  # your password
                     db="newdatabase")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM hello")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]
sql = gen_insert_sql(10)
cur.execute(sql);
db.commit()

db.close()
~
