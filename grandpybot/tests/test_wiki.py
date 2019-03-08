from grandpybot import wiki

""" Test wiki module """


def test_get_infos(monkeypatch):
    """ Mock and test if the wiki module works. """
    coordinates = {'lat': 48.8747265, 'lng': 2.3505517}
    page_name = "Cité Paradis"

    def mockreturn(coordinates):
        return page_name

    monkeypatch.setattr('grandpybot.wiki.get_infos', mockreturn)
    assert wiki.get_infos(coordinates) == page_name
