from grandpybot import regex

""" Test the regex module. """


def test_build_positive_lookbehind_assertion():
    """ Test if the regex building function works as intended. """
    spatial_indicators = ["adresse", "situe"]
    result = r'(?:((?<=\badresse\s)[-\w\s]*)|((?<=\bsitue\s)[-\w\s]*))'
    assert regex.build_pla(spatial_indicators) == result
