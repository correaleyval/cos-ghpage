from flask import Flask, render_template

import requests

app = Flask(__name__)

app.config.from_object('settings')

@app.route('/')
def index():
    print(app.config['API_URI'])
    return render_template('index.html')

@app.route('/developers.html')
def developers():
    res = requests.get("{}{}".format(
        app.config['API_URI'],
        'users'
    ))

    data = res.json()

    return render_template('developers.html', users=data['users'])

@app.route('/proyects.html')
def proyects():
    res = requests.get("{}{}".format(
        app.config['API_URI'],
        'repos'
    ))

    data = res.json()

    return render_template('proyects.html', repos=data['repos'])

if __name__ == '__main__':
    app.run(debug=True, port=3000)
