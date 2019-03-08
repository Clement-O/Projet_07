from flask import Flask
import json

from config import Config
from grandpybot import regex

app = Flask(__name__)
app.config.from_object(Config)

CONSTANTS = json.load(open('constants.json', 'r', encoding='utf-8'))
REGEX_STOPWORDS = r'\b(' + "|".join(CONSTANTS["stopwords"]) + r')\s'
REGEX_PLACES = r'\b(?=' + "|".join(CONSTANTS["places"]) + r'\s)[\w\s]*'
REGEX_SPATIAL_INDICATORS = regex.build_pla(CONSTANTS['spatial_indicators'])
REGEX_ADDRESS = r'(?=\d)[\w\s]*'

from grandpybot import routes
