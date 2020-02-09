from flask import Flask, render_template
import os
from scrabblehelp import get_counts, get_scores, get_sowpods

app =  Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)


@app.route('/howmuch')
def howmuch():
    """Explains how many points each letter is worth."""
    letters = get_scores()
    return render_template("scores.html", letters=letters)


@app.route('/sowpods')
def sowpods():
    """Shows words in sowpods dictionary."""
    allsowpods = get_sowpods()
    return render_template("sowpods.html", allsowpods=allsowpods)


@app.route('/howmany')
def howmany():
    """Explains how many of each letter there is."""
    counts = get_counts()
    return render_template("counts.html", counts=counts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)