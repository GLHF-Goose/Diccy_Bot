from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

port=os.environ['PORT']

#def run():
#  app.run(host='0.0.0.0',port=os.environment['PORT'])

def keep_alive():
    t = Thread(target=run)
    t.start()
