from flask import Flask, render_template, request, url_for
from json import dumps
from messages import Messages

bottled_messages = Messages()

app = Flask(__name__)

@app.route('/')
def nothing():
    return 'try again dumbass'

@app.route('/send/', methods=['POST'])
def send_message():

    content = request.get_json()

    long_val = float(content['long'])
    lat_val = float(content['lat'])
    long_lat = (long_val, lat_val)

    text = content['text']

    bottled_messages.add_message(long_lat, text)

    return 'Successfully sent message: ' + text + '\nat: ' + str(long_lat) + '\n'

@app.route('/open/', methods=['GET'])
def open_message():

    content = request.get_json()

    long_val = float(content['long'])
    lat_val = float(content['lat'])
    long_lat = (long_val, lat_val)

    msgs = bottled_messages.get_messages(long_lat)

    return dumps(msgs)

if __name__ == "__main__":
    app.run()
