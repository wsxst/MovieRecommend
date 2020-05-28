from pyhive import hive
import flask
from flask_cors import CORS
from flask import request, Flask, jsonify

app = Flask(__name__)
CORS(app, resources='/*')

@app.route('/user', methods=['GET'])
def get_users():
    start_time=request.args.get("s")
    end_time=request.args.get("e")
    sql="select user_name,count(*) as count from logs where log_id>='"+start_time+"' and log_id<='"+end_time+"' group by user_name order by count desc limit 10"
    cursor=conn.cursor()
    cursor.execute(sql)
    res_json={}
    res_json["user_id_list"]=[]
    res_json["user_access_num_list"]=[]
    print("start!!!")
    for res_row in cursor.fetchall():
        res_json["user_id_list"].append(res_row[0])
        res_json["user_access_num_list"].append(res_row[1])
    cursor.close()
    print("end!!!")
    return jsonify(res_json)

@app.route('/movie', methods=['GET'])
def get_movies():
    start_time=request.args.get("s")
    end_time=request.args.get("e")
    sql="select movie_name,count(*) as count from logs where log_id>='"+start_time+"' and log_id<='"+end_time+"' group by movie_name order by count desc limit 10"
    cursor=conn.cursor()
    cursor.execute(sql)
    res_json={}
    res_json["movie_id_list"]=[]
    res_json["movie_access_num_list"]=[]
    for res_row in cursor.fetchall():
        res_json["movie_id_list"].append(res_row[0])
        res_json["movie_access_num_list"].append(res_row[1])
    cursor.close()
    return jsonify(res_json)

if __name__ == "__main__":
    conn = hive.Connection(host='192.168.0.222', port=10000, username='hive', auth='NOSASL',database='recommend')
    app.run("0.0.0.0", port=16666, debug=True)

