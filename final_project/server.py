from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    Flask server function for English to French translation
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    Flask server function for French to English translation
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text_to_translate)

@app.route("/")
def renderIndexPage():
    """
    Flask server function to render the index page
    """
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
