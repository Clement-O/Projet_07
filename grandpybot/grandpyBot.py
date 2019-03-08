from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import settings

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        research = request.form.get('research')
        result = address(research)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')


# On F5 resend data => Create a copy of result for "if == POST" and use original to else.


def address(research):
    # Replace/erase the final dot and apostrophe and create a list.
    research_list = research.replace('.', '').replace('\'', ' ').split()

    # Erase useless little words.
    for word in research_list:
        if word in settings.erase_words:
            research_list.remove(word)

    # Save the 'reference' string.
    refined_string = ' '.join(research_list)
    # Copy string to save researched address after comparison with 'reference' one.
    researched_address = refined_string

    for word in research_list:
        if (research_list[0].isnumeric() is False) and (len(researched_address.split()) > 3):
            if word in settings.stop_words:
                researched_address = refined_string[refined_string.index(word):]
            if word.isnumeric():
                researched_address = refined_string[refined_string.index(word):]
            if (word is not research_list[0]) and (word.istitle()):
                researched_address = refined_string[refined_string.index(word):]
        else:
            return researched_address


if __name__ == '__main__':
    app.run(debug=True)
