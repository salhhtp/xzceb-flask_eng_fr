"""A web based language translator service using IBM Watson API.
Run from command line:
$ python server.py
"""

from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    This function translates English to French and renders the result page.
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english():
    """
    This function translates French to English and renders the result page.
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text_to_translate)

@app.route("/")
def render_index_page():
    """
    This function render the start page.
    """
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)