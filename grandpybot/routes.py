from flask import render_template, request, jsonify

from grandpybot import app
from grandpybot import CONSTANTS
from grandpybot.form import InputForm
from grandpybot.input import get_address
from grandpybot.map import get_coordinates
from grandpybot.wiki import get_infos

""" Main module for Flask to create the website. """


@app.route('/')
@app.route('/index')
def index():
    """
    Render the website following the 'index.html' file
    :return: Website template
    """
    form = InputForm()
    return render_template("index.html", form=form)


@app.route('/process', methods=['POST'])
def process():
    """
    Call all the functions to analyze, get the map & the infos
    from the user's input.
    :return: JSON response
    """
    address = get_address(request.form['formInput'])
    coordinates = get_coordinates(address)
    if coordinates['status'] == 'FAIL':
        response = {"status": "error",
                    "message": CONSTANTS['errors']['geocode']}
    else:
        response = get_infos(coordinates)
        if response['status'] == 'FAIL':
            response = {"status": "error",
                        "message": CONSTANTS['errors']['mediawiki']}
    return jsonify(response)
