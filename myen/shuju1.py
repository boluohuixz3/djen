import os
import sqlite3

print(os.getcwd() )
conn=sqlite3.connect("db.sqlite3") #创建指定数据库 硬盘
sj = conn.cursor()
sj.execute("update  danci set chuti=100,cuowu=1")
conn.commit()
print("噢可")
 