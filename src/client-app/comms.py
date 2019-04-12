from flask import Flask, request
from .src.keys import VirtualKeys
import json


app = Flask(__name__)


@app.route("/", methods=['POST'])
def gesture():
    data = json.loads(request.data)
    VirtualKeys.send_key(data['gesture_id'])
    return "Gesture complete!"


app.run(host='0.0.0.0')
