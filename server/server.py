from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def nothing():
    return 'try again dumbass'

if __name__ == "__main__":
    app.run()
