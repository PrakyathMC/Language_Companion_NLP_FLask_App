from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    # Pass empty strings for the initial page load
    return render_template('index.html', original_text='', detected_language='', translated_text='')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['language']
    
    # Detect the language
    detected_language = detect(text)
    
    # Translate the text
    translation = translator.translate(text, dest=target_language)

    # Pass the original text, detected language, and translation to the template
    return render_template('index.html', 
                           original_text=text, 
                           detected_language=detected_language, 
                           translated_text=translation.text)

if __name__ == '__main__':
    app.run(debug=True)
