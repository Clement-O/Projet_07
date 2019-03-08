from grandpybot import response

""" Test response module """


def test_format_response(monkeypatch):
    """ Mock and test if the response is correctly formatted. """
    coordinates = {'lat': 48.8747265, 'lng': 2.3505517}
    title = "Cité Paradis"
    place = "EXACT"
    summary = ""
    result = {'status': "OK"}

    def mockreturn(coordinates, title, place, summary):
        return result

    monkeypatch.setattr('grandpybot.response.format_response', mockreturn)
    assert response.format_response(coordinates, title, place,
                                    summary) == result
