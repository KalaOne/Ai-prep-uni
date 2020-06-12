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


# 2) Build a user interface in Python/Flask to accept input from the user and get the response back from the NLP processing you did in Assignment. Refactor if necessary.

# 3) Expand on the capability of your NLP. I want to be able to type a sentence like “I was born in Mansfield and now I live in Norwich” and your code should try and recognise which is the city I was born in and which I now live in.

# The actual sentence itself will vary, so try and come up with some ways of figuring out what is what in a sentence with two cities in.
