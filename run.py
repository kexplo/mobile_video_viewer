#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, url_for, send_from_directory
app = Flask(__name__)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

VIDEO_DIR = u'./video'

@app.route('/')
def index():
    fileList = [f for f in os.listdir(VIDEO_DIR) if os.path.isfile(os.path.join(VIDEO_DIR,f))]
    return render_template('index.html', fileList=fileList)

@app.route('/v/<string:file_name>')
def get_video(file_name):
    return send_from_directory('./video', file_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
