# -*- coding: utf-8 -*-
import json
from twitter import *
from pymongo import MongoClient
from datetime import datetime

with open("auth.json") as f:
    secretjson = json.load(f)

t = Twitter(auth=OAuth(
            secretjson["access_token"],
            secretjson["access_token_secret"],
            secretjson["consumer_key"],
            secretjson["consumer_secret"]))

client = MongoClient()
db = client.mayoiga

#初回のみ
last_id = 0

#最終保存ツイートID
last_one = db.mayoiga.find().sort('tweet.id', -1).limit(1)

for doc in last_one:
    last_id = doc['tweet']['id']

if last_id:
    results = t.statuses.home_timeline(count=600, since_id=last_id)
else:
    results = t.statuses.home_timeline(count=600)

if results:
    db.mayoiga.insert_many([{'tweet': tweet} for tweet in results])
