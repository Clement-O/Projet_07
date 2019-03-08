from grandpybot import map

""" Test the map module. """


def test_get_coordinates(monkeypatch):
    """ Mock and test if the 'get_coordinates' function works. """
    address = "OpenClassrooms France"
    result = {'lat': 48.8747265, 'lng': 2.3505517}

    def mockreturn(address):
        return result

    monkeypatch.setattr('grandpybot.map.get_coordinates', mockreturn)
    assert map.get_coordinates(address) == result
