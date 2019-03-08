from random import choice

from grandpybot import CONSTANTS
from config import Config

""" Module to format the response before being used by client side script. """


def format_response(coordinates, title, place, summary):
    """
    Format the response.
    :param coordinates: Original coordinates dictionary
    :param title: Wiki page title to build wiki url
    :param place: String to select a correct sentence for the title
    :param summary: Wiki page summary
    :return: formatted response
    """
    # Create response dictionary &
    # keep the formatted address from coordinates
    response = {'formatted_address': coordinates['formatted_address']}

    # Get random sentence/response for GrandPy
    if place == 'EXACT':
        grandpy_title = choice(CONSTANTS['grandpy_sentences']['exact_places'])
    else:
        grandpy_title = choice(CONSTANTS['grandpy_sentences']['near_places'])

    # Build URLs
    url_map_start = "https://www.google.com/maps/embed/v1/place?q=place_id:"
    url_map_end = "&key=" + Config.GOOGLE_API_KEY
    url_map = url_map_start + coordinates['place_id'] + url_map_end
    url_wiki_base = "https://fr.wikipedia.org/wiki/"
    url_wiki = url_wiki_base + title.replace(' ', '_')
    # Build random source sentence
    source_name = choice(CONSTANTS['source_names'])
    source_number = choice(CONSTANTS['source_number'])
    source = "— Source : " + source_name + " " + source_number
    # Update dictionary
    response.update({
        'map_url': url_map,
        'wiki_title': grandpy_title,
        'wiki_summary': summary,
        'wiki_source': source,
        'wiki_url': url_wiki,
        'status': "OK"
    })
    return response
