#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import os.path
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    path = '/home/shiyanlou/files'
    list = os.listdir(path)
    i = 0
    title = []
    for x in list:
        list[i] = os.path.join(path,x)
        i += 1
    for x in list:
        with open(x, 'r') as file:
            temp = json.loads(file.read())
            title.append(temp['title'])
    return render_template('index.html', title=title)

@app.route('/files/<filename>')
def file(filename):
    filepath = '/home/shiyanlou/files/' + filename + '.json'
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            temp = json.loads(file.read())
            content  = temp['content']

    else:
        abort(404)
    return render_template('file.html', content=content)


