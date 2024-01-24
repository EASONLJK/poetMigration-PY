from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
from sklearn.svm import LinearSVC
import pandas as pd
import numpy as np
from itertools import combinations

import json

app = Flask(__name__)
CORS(app, resources=r'/*')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world(): 
    return 'test!'

@app.route('/mapbox/china', methods=['POST','GET'])
def get_geojson():
    # 解析json文件
    with open('./data/china.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/mapbox/province_china', methods=['POST','GET'])
def get_province_geojson():
    # 解析json文件
    with open('./data/china_province.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/mapbox/radial', methods=['POST','GET'])
def get_radial():
    # 解析json文件
    with open('./data/classify_data_detail.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# 高校分类信息，包含地理数据和分类数据
@app.route('/mapbox/china_province', methods=['POST','GET'])
def get_china_province():
    # 解析json文件
    with open('./data/province-geo-info.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/mapbox/province_city', methods=['POST','GET'])
def get_province_city():
    # 解析json文件
    with open('./data/province/province-geo-info.json', 'r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/mapbox/poetMigration',methods=['POST','GET'])
def  get_poet_transatiton():
    with open('./data/poetMigration.json','r',encoding='utf-8') as f:
        data =  json.load(f)
    return jsonify(data)

@app.route('/poetMigration_sequential',methods=['POST','GET'])
def get_poetMigration_sequential():
    with open('./data/poetMigration_sequential.json','r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/mapbox/qinlin_huaihe',methods=['POST','GET'])
def get_qinlin_huaihe():
    with open('./data/qinlin_huaihe.json','r',encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run()