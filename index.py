from flask import Flask, render_template, request
import spacy

nlp = spacy.load("en_core_web_sm")
app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)

@app.route('/')
def hi():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def hi_post():
    input = request.form['CityBorn']
    checkText(input)
    return render_template('index.html', result = input)
#     I live in Bristol but my birth was given in London

def checkText(inp):
    """
    Takes text from user input in the form and extracts cities based on words 'live/living' and 'born/birth'
    """
    text = nlp(inp)
    city_born_in, city_living_in, city_birth, city_life = '','','',''
    for i, word in enumerate(text):
        if word.text == "born" or word.text == "birth":
            city_born_in = text[i:]
            for token in city_born_in:
                if (token.pos_ == "PROPN" and token.dep_ == "pobj"):
                        city_birth = token
                        break
        if word.text == "live" or word.text == "living":
            city_living_in = text[i:]
            for token in city_living_in:
                if (token.pos_ == "PROPN" and token.dep_ == "pobj"):
                        city_life = token
                        break
    print("User was born in " + city_birth.text)
    print("User lives in " + city_life.text)

if __name__ == '__main__':
    app.run()


# POST request is when html is sending to backend
# GET request is when backend is sending to html

# 1) Implement a full chat window with your chatbot
# So you can type multiple things to it and all the responses come back on the web page

# 2) Make it so you don't need to look in the python console to know what it's up to - 
#   so if it has problems with the text provided, it displays a nice message in your new UI

# 3) make it a bit more conversational
# So if you type "hello" it will respond