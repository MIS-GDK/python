import cx_Oracle  # 引用模块cx_Oracle

conn2 = cx_Oracle.connect("orawms/orawms153@192.168.0.153:1521/zzora")
c2 = conn2.cursor()

x2 = c2.execute("""SELECT sal  FROM Emp where empno = :empno""", empno=7369)
res2 = x2.fetchone()
c2.close()
conn2.close()

# conn=cx_Oracle.connect(‘用户名/密码@主机ip地址：端口号/Service Name（SID)')
# 连接数据库
conn = cx_Oracle.connect("hrhnprod/hrhnprod@192.168.0.190:1525/HRHNDB")

# conn = cx_Oracle.connect("h2_query_hn/query456_hn@10.0.0.196:1521/MDMDB")
# 获取cursor
c = conn.cursor()

# 使用cursor进行各种操作
# x = c.execute("select * from Emp")

# res = x.fetchall()
# print(res[0][0])
# pm = {":1": 2777, ":2": 7369}
# c.execute("update hrhnprod.Emp set sal = :1 where empno = :2", pm)
# 每次返回一行数据
x = c.execute("select * from emp")
# print(res2[0][0])
# pm = {":1": 1000, ":2": 7900}
# pm = {":1": 333}
# res = x.fetchall()
# print(type(res[0]))

# for i in res:
#     pm = {":1": res2[0], ":2": i[0]}
#     c.execute("update emp set sal = :1 where empno = :2", pm)
while True:
    res = x.fetchone()
    pm = {":1": res2[0], ":2": res[0]}
    if res == None:
        break
    elif res[2] == "CLERK":
        res3 = c.execute("update emp set sal = :1 where empno = :2", pm)

# 关闭cursor
c.close()

# 关闭连接
conn.commit()
conn.close()
