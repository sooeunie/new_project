from flask import Flask, render_template, request
from googlefinance import getQuotes
app = Flask(__name__)
import os
import giphypop
g = giphypop.Giphy()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/results')
def results():
    gifs = []
    search_output = request.values.get('search')
    results = g.search(search_output)


    for result in results:
        gifs.append(result.media_url)

    return render_template('results.html', gifs=gifs)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

