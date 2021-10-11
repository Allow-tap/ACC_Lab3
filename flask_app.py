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
<<<<<<< HEAD
        print("Executing..")
        time.sleep(8)
    data = result.get(timeout=1)
    return jsonify(data)
    #return json.dumps(data, sort_keys=True)
=======
        print("Executing and gathering results, please wait, sleeping for 8 seconds...")
        time.sleep(8)
    data = result.get(timeout=1)
    return json.dumps(data)
>>>>>>> 0703d70d6c8c168c29a9f379386b4ffbcc75926c

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)