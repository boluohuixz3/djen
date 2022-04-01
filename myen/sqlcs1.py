import os
import sqlite3
import time
t1=time.time()

#ml=os.getcwd()+"\db.sqlite3"
ml=os.getcwd()+"\\myen\\db.sqlite3"
print(ml)
#    ml=ml.replace("\\",r"\\")
conn=sqlite3.connect(ml)
sj = conn.cursor()    
zd1=[]
#显示全部表
# sj.execute("SELECT * FROM timu limit 1")
# zd1=sj.fetchall()
# print(zd1)

sj.execute("update timu set cuowu=0 ")
zd1=sj.fetchall()
conn.commit()  
# #sj.execute("SELECT count(danci) FROM danci where chuti >100")
# sj.execute("SELECT count(danci) FROM danci where chuti <100")
# zd1=sj.fetchall() 
# print((zd1))
# print(time.time()-t1)


