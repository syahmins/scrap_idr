import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('base.html', TITLE='Scrap IDR rates')


@app.route("/idrrates")
def idrrates():
    # tautan yang akan diambil datanya
    rate_source = requests.get('http://www.floatrates.com/daily/idr.json')

    json_data = rate_source.json()

    return render_template('idr_rates.html', rates=json_data.values())


if __name__ == '__main__':
    app.run(debug=True)
