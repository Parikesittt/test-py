from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/analisa-data')
def analisa_data():
    return 'kesit'

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000)