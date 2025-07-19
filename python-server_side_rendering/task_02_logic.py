#!/usr/bin/env python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_list = data.get('items', [])
    except Exception as e:
        item_list = []
    
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

