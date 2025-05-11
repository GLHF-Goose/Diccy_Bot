
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
    app.run(host='0.0.0.0', port=os.environ['8080'])
    print("Port created.")

def keep_alive():
    run()
    print("Keeping alive")
    t = Thread(target=run)
    t.start()
    print("Started thread")
