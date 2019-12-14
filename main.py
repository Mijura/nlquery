from nlquery.nlquery import NLQueryEngine
import os
import sys
from flask import Flask, request
from gevent import monkey

monkey.patch_all()
app = Flask(__name__)
engine = NLQueryEngine('localhost', 9000)

@app.route("/query", methods=['POST'])
def query():
    query = request.json.get('query')
    return engine.query(query, format_='plain')

if __name__ == '__main__':
    app.run()
