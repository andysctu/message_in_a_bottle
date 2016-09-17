from flask import Flask, render_template, request, url_for

from messages import Messages

bottled_messages = Messages()

app = Flask(__name__)

@app.route('/')
def nothing():
    return 'try again dumbass'

@app.route('/send/', methods=['POST'])
def send_message():

    long_val = float(request.form['long'])
    lat_val = float(request.form['lat'])
    long_lat = (long_val, lat_val)

    text = request.form['text']

    bottled_messages.add_message(long_lat, text)

    return 'Successfully sent message: ' + text + '\nat: ' + str(long_lat) + '\n'

@app.route('/open/', methods=['GET'])
def open_message():

    long_val = float(request.form['long'])
    lat_val = float(request.form['lat'])
    long_lat = (long_val, lat_val)

    text = bottled_messages.get_messages(long_lat)

    return 'The message in the bottle is: ' + text + '\n'

if __name__ == "__main__":
    app.run()
