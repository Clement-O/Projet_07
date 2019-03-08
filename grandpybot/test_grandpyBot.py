import grandpyBot


def test_address():

    research_sentence = "Où se situe le jardin Bruyant."
    assert grandpyBot.address(research_sentence) == "jardin Bruyant"

    research_capitalized = "Situe moi le Nom propre"
    assert grandpyBot.address(research_capitalized) == "Nom propre"

    research_words = "Central Park NY"
    assert grandpyBot.address(research_words) == "Central Park NY"

    research_address = "5 Avenue Anatole France"
    assert grandpyBot.address(research_address) == "5 Avenue Anatole France"

    # TODO: Add test ?
