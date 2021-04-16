from app import app
from flask import render_template, request
from app.models import get_entry
from app.static.text.text import eng_dict, fin_dict


@app.route("/")
def index():
    return render_template("index.html", dict=eng_dict)


@app.route("/translate", methods=['GET'])
def translate():
    word = request.args.get("word")
    return render_template("index.html", dict=eng_dict, results=get_entry(word, route='eng'))


@app.route("/fin")
def fin():
    return render_template("fin.html", dict=fin_dict)


@app.route("/fin/translate", methods=['GET'])
def fin_translate():
    word = request.args.get("word")
    return render_template("fin.html", dict=fin_dict, results=get_entry(word, route='fin'))
