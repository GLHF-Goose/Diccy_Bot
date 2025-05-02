from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
    print("Running on port:")
    print(os.environ['PORT'])
    app.run(host='0.0.0.0',port=os.environ['PORT'])

def keep_alive():
    run()
    print("Keeping alive")
    t = Thread(target=run)
    t.start()
    print("Started thread")
