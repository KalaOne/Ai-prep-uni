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

def checkText(inp):
    text = nlp(inp)
    cities = []
    for word in inp:
        if (word ==" born " or " birth "):
            cityBornIn = inp.split(word)                
        if (word == " live " or " living "):
            cityLivingIn = inp.split(word)
    for token in text:
        # print(token.text, token.pos_, token.dep_)
        if (token.pos_ == "PROPN" and token.dep_ == "pobj"):
                cities.append(token)
    print(cities)
    print("Birth Sentence: " + " ".join(cityBornIn))
    print("Life Sentence: " + " ".join(cityLivingIn))

if __name__ == '__main__':
    app.run()


# POST request is when html is sending to backend
# GET request is when backend is sending to html


# 2) Build a user interface in Python/Flask to accept input from the user and get the response back from the NLP processing you did in Assignment. Refactor if necessary.

# 3) Expand on the capability of your NLP. I want to be able to type a sentence like “I was born in Mansfield and now I live in Norwich” and your code should try and recognise which is the city I was born in and which I now live in.
# I live in Birmingham and my birth was given in South Lake City

# The actual sentence itself will vary, so try and come up with some ways of figuring out what is what in a sentence with two cities in.
