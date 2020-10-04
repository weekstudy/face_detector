from flask import Flask, request, jsonify
import mysql_conn
app = Flask(__name__)



@app.route('/update_url')
def update_url():
    import face_recognition as face
    origin_url = request.args.get("origin_url", 0)
    # sql = "SELECT * from img where origin_url= '%s' "
    # data = (origin_url)
    # mysql_conn.cursor.execute(sql % data)
    # resSql = mysql_conn.cursor.fetchall()
    # todo 判断 origin_url 数据是否被检查
    # url='http://json119.com/images/img/2020/10/03/23b1cbda-d58f-4fe1-ba23-3673d94ea1bb.jpg'
    # res=face.face_detector('F:/Python/object_detection/openCV_tutorial/lena.jpg')
    check_res = face.face_detector(origin_url)
    res = {"result": check_res}
    print(res)
    # 修改数据
    # sql = "UPDATE img SET is_switch = 2 where origin_url= 'http://localhost:8112/images/img/2020/10/03/058f7150-d66a-4222-bc8b-0ea951316c9b.jpg'"
    sql = "UPDATE img SET check_res = '%s', is_switch= %d where origin_url= '%s' "
    data = (check_res, 1, origin_url)
    mysql_conn.cursor.execute(sql % data)
    mysql_conn.connect.commit()
    print('成功修改', mysql_conn.cursor.rowcount, '条数据')
    # cursor.close()
    # connect.close()
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content=res)

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            debug=True,
            port=8081)