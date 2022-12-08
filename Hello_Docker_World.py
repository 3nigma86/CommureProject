#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_webhook():
	return "Hello Docker World\n"
app.run(host="localhost",port=5000)
