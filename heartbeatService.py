from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Bot is alive!"

def run():
    app.run(port=9000)

def initialiseBeating():
    server = Thread(target=run)
    server.start()