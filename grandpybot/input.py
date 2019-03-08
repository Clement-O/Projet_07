import re

from grandpybot import REGEX_STOPWORDS
from grandpybot import REGEX_PLACES
from grandpybot import REGEX_SPATIAL_INDICATORS
from grandpybot import REGEX_ADDRESS

""" Module to obtain address from the user's input. """


def get_address(sentence):
    """
    Determinate address.
    :param sentence: User's input
    :return: Address to work with
    """
    replaced_sentence = sentence.replace('.', '').replace('\'', ' ')
    refined_sentence = re.sub(REGEX_STOPWORDS, '', replaced_sentence,
                              flags=re.IGNORECASE)

    # Regex looking for places
    if re.search(REGEX_PLACES, refined_sentence, flags=re.IGNORECASE):
        address = re.search(REGEX_PLACES, refined_sentence,
                            flags=re.IGNORECASE).group()
        return address.strip()
    # If there is no places, look for spatial indicators
    elif re.search(REGEX_SPATIAL_INDICATORS, refined_sentence,
                   flags=re.IGNORECASE):
        address = re.search(REGEX_SPATIAL_INDICATORS, refined_sentence,
                            flags=re.IGNORECASE).group()
        while re.search(REGEX_SPATIAL_INDICATORS, address,
                        flags=re.IGNORECASE):
            address = re.search(REGEX_SPATIAL_INDICATORS, address,
                                flags=re.IGNORECASE).group()
        return address.strip()
    # If everything fails, look for numbers
    elif re.search(REGEX_ADDRESS, refined_sentence, flags=re.IGNORECASE):
        address = re.search(REGEX_ADDRESS, refined_sentence,
                            flags=re.IGNORECASE).group()
        return address.strip()
    # Else return the full string
    else:
        return refined_sentence.strip()
