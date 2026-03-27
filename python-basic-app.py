from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Ashir app for Assignment 06. TRIGGERED VIA WEBHOOK using CLOUDFLARED!!! 11th BUILD -Again Check" 



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



