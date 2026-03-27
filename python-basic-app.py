from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Ashir app for Assignment 06. TRIGGERED VIA WEBHOOK using CLOUDFLARED!!! 9th BUILD" 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



