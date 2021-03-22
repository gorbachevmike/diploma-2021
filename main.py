from json import dumps

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root():
    with open("db.txt", "a", encoding="utf-8") as fd:
        print(dumps(request.get_json()), file=fd)
    return "thanks"
