""" Module de build a regular expression. """


def build_pla(spatial_indicators):
    """
    Build a 'positive lookbehind assertion' (pla) regular expression.
    :param spatial_indicators: List of strings
    :return: A 'positive lookbehind assertion' (pla) regular expression
    """
    regex_list = []
    length = len(spatial_indicators)
    for index, word in enumerate(spatial_indicators):
        if index == 0:
            regex_list.append('(?:((?<=\\b{}\\s)[-\\w\\s]*)|'.format(word))
        elif index + 1 < length:
            regex_list.append('((?<=\\b{}\\s)[-\\w\\s]*)|'.format(word))
        else:
            regex_list.append('((?<=\\b{}\\s)[-\\w\\s]*))'.format(word))
    regex = r'' + ''.join(regex_list)
    return regex
