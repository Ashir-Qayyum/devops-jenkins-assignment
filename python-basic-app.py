from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Ashir app for Assignment 06. Modified to test Pipeline Manually! Now Modified to test Automatic CI/CD Trigger via Webhook!!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



