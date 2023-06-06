from flask import Flask, render_template, request
import json
from machinetranslation import translator
from markupsafe import escape

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return f"Translated text to French: {translator.english_to_french(textToTranslate)}" 

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return f"Translated text to English: {translator.french_to_english(textToTranslate)}"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
