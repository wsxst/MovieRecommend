from flask import Flask,request,jsonify,make_response
import json
import copy
import datetime
import random
from flask_sqlalchemy import SQLAlchemy
import pymysql
import predict
import time
import csv
import os
from flask_cors import *

host = '127.0.0.1'
username = 'root'
password = 'password'
database = 'recommend'
port = 3306
app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/')
def hello_world():
    return 'Hello World'

def movie_info(movie_id):
    # 打开数据库连接
    db = pymysql.connect(host,username,password,port)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = """select * from movie where movieid = %s"""%(int(movie_id))
    print(sql)
    data = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        row = results[0]
        data["movieid"] = row[0]
        data["moviename"] = row[1]
        data["showyear"] = row[2]
        #data["nation"] = row[3]
        data["director"] = row[4]
        data["leadactors"] = row[5]
        #data["screenwriter"] = row[6]
        data["picture"] = row[7]
        data["averating"] = row[8]
        data["numrating"] = row[9]
        data["description"] = row[10]
        data["typelist"] = row[11]

    except:
        print("error")
    db.close()
    return data

def get_moviename(movie_id):
    # 打开数据库连接
    db = pymysql.connect(host,username,password,port)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = """select * from movie where movieid = %s"""%(int(movie_id))
    print(sql)
    data = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        row = results[0]
        data["movieid"] = row[0]
        data["moviename"] = row[1]
        data["showyear"] = row[2]
        #data["nation"] = row[3]
        data["director"] = row[4]
        data["leadactors"] = row[5]
        #data["screenwriter"] = row[6]
        data["picture"] = row[7]
        data["averating"] = row[8]
        data["numrating"] = row[9]
        data["description"] = row[10]
        data["typelist"] = row[11]

    except:
        print("error")
    db.close()
    return data

def get_username(user_id):
        # 打开数据库连接
    db = pymysql.connect(host,username,password,port)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = """select * from user where userid = %s"""%(int(user_id))
    print(sql)
    data = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        row = results[0]
        name = row[1]
    except:
        print("error")
    db.close()
    return name

@app.route('/get_recommend',methods=['GET'])
def get_recommend():
    print("======")
    print(request.headers)
    # log = {}
    # log["host"] = request.headers.get("Host")
    # log["route"] = "get_recommend"
    # log["userid"] = request.args.get("userid")
    # print(log)
    # with open("back_log","a+") as f:
    #     f.write(str(log)+'\n')
    print("======")
    user_id = request.args.get("userid")
    result = predict.movie_predict(int(user_id),5)
    info = []
    for re in result:
        a = movie_info(re)
        if a:
            info.append(a)
    res = {}
    res["code"] = 0
    res["data"] = info
    resp = jsonify(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/get_movie',methods=['GET'])
def add():
    print("======")
    print(request.headers)
    print("======")
    movie_id = request.args.get("movieid")
    user_id = request.args.get("userid")
    # 打开数据库连接
    db = pymysql.connect(host,username,password,port)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = """select * from movie where movieid = %s"""%(int(movie_id))
    print(sql)
    data = {}
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        row = results[0]
        data["movieid"] = row[0]
        data["moviename"] = row[1]
        data["showyear"] = row[2]
        #data["nation"] = row[3]
        data["director"] = row[4]
        data["leadactors"] = row[5]
        #data["screenwriter"] = row[6]
        data["picture"] = row[7]
        data["averating"] = row[8]
        data["numrating"] = row[9]
        data["description"] = row[10]
        data["typelist"] = row[11]

    except:
        print("error")

 #       review”:true/false,（当前用户是否对该电影进行打分）
#“user_rating”:5（当前用户对该电影的打分）
    sql = """SELECT * FROM rating WHERE movieId = %s and userId = %s"""%(int(movie_id),int(user_id))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) == 0:
            data["review"] = False
        else:
            data["review"] = True
            data["user_rating"]=results[0][2]
    except:
        print("error")
    res = {}
    res["code"] = 0
    res["data"] = data
    resp = jsonify(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    #写入log文件
    # log = {}
    # log["host"] = request.headers.get("Host")
    # log["route"] = "get_movie"
    # log["movieid"] = request.args.get("movieid")
    # log["userid"] = request.args.get("userid")
    millis = int(round(time.time() * 1000))
    log = str(millis) + '\t' +  get_username(user_id) + '\t'+ data["moviename"] 
    print(log)
    with open("back_log","a+") as f:
        f.write(str(log)+'\n')
    return resp

def handle_chain_data(data):
    with open('./ratings.csv','a+') as csvfile:
        fieldnames=["userId","movieId","rating","timestamp"]
        write=csv.DictWriter(csvfile,fieldnames=fieldnames)
        write.writerow(data)


@app.route('/user_rate',methods=['GET'])
#@cross_origin()
def user_rate():
    print("======")
    print(request.headers)
    print("======")
    print("*****")
    movie_id = request.args.get("movieid")
    user_id = request.args.get("userid")
    star = request.args.get("star")
    # 打开数据库连接
    db = pymysql.connect(host,username,password,port)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = """insert into rating(userId,movieId,rating) values(%s,%s,%s) """%(int(user_id),int(movie_id),float(star))
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
    res= {}
    res["code"] = 0
    resp = jsonify(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    moviename = movie_info(movie_id)["moviename"]
    print(moviename)
    millis = int(round(time.time() * 1000))
    log = str(millis) + '\t' +  get_username(user_id) + '\t'+str(moviename)
    print(log)
    with open("back_log","a+") as f:
        f.write(str(log)+'\n')
    # write to ratings.csv
    newdata={}
    newdata["userId"] = user_id
    newdata["movieId"] = movie_id
    newdata["rating"] = star
    newdata["timestamp"] = int(time.time())
    handle_chain_data(newdata)
    # train
    os.system("nohup python3 train.py &")
    return resp
if __name__ == '__main__':
   app.run(host="0.0.0.0",port = 18999)
