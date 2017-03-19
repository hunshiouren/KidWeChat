#! python3
# -*- coding:utf-8 -*-
import requests
import json


key = '042c8822f369426aa4ff5396880c84ad'

def autoreply(text):
    response = requests.get('http://www.tuling123.com/openapi/api?key={}&info={}'.format(key, text))
    reply = response.json()['text']
    return reply