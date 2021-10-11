#!flask/bin/python
from flask import Flask, jsonify
from pronoun_analysis import tweet_analysis
import subprocess
import sys, time
import json
app = Flask(__name__)

@app.route('/result_flask_app', methods=['GET'])
def result_flask_app():
    result = tweet_analysis.delay()
    while result.ready() == False:
        print("Executing..")
        time.sleep(8)
    data = result.get(timeout=1)
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)
