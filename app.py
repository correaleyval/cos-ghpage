from flask import Flask, render_template

import requests

app = Flask(__name__)

app.config.from_object('settings')

@app.route('/')
def index():
    print(app.config['API_URI'])
    return render_template('index.html')

@app.route('/developers')
def developers():
    res = requests.get("{}{}".format(
        app.config['API_URI'],
        'users'
    ))

    data = res.json()

    return render_template('developers.html', users=data['users'])

@app.route('/proyects')
def proyects():
    return render_template('proyects.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
