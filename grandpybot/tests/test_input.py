from grandpybot import input

""" Test the input module. """


def test_get_address():
    """ Test if the address from the user's input is properly
    determinate. """
    sentence = "Donne moi l'adresse d'OpenClassrooms en France, s'il te " \
               "plaît GrandPy"
    result = "OpenClassrooms France"
    assert input.get_address(sentence) == result
