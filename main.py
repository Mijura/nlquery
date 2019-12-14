from nlquery.nlquery import NLQueryEngine
import os
import sys
from flask import Flask, request, render_template
from gevent import monkey

monkey.patch_all()
app = Flask(__name__)
engine = NLQueryEngine('localhost', 9000)

@app.route("/query", methods=['POST'])
def query():
    query = request.json.get('query')
    answer = engine.query(query, format_='plain')
    
    if answer=="None":
        answer = "Sorry, we can't find answer. Try other question."

    return { "answer": answer}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
