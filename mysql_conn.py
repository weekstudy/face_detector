import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    # port=3370,
    user='root',
    passwd='mac123',
    db='check_face',
    charset='utf8'
)
cursor = connect.cursor()


