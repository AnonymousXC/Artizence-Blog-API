from flask import Flask, jsonify, request
from pathlib import Path
import re

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        {
            'server': '200',
            'status': 'running',
            'github': 'https://github.com/AnonymousXC/Artizence-Blog-API' 
        }
    )

@app.route('/blog', methods=['GET', 'POST'])
def getBlog():

    data = request.args

    if data.get('blogID') is None:
        return jsonify({
            'status': '404',
            'error': 'missing data'
        })
    print(data['blogID'] + ".md")

    for child in Path('blogs').iterdir():
        if child.is_file() and child.name == data['blogID'] + '.md':

            markdown = child.read_text()
            rm_markdown = re.sub(r'---\n.*\n.*\n.*\n---', "", markdown)
            heading = 'something'

            return jsonify({
                'heading': heading,
                'author': 'somebody',
                'markdown': rm_markdown
            })
    
    return "<b>dsad</b>"
