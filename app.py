from flask import Flask
from flask import request,jsonify
from flask_ngrok import run_with_ngrok
import ktrain

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run

predictor = ktrain.load_predictor('distilbert')

def get_prediction(x):
    sent=predictor.predict([x])
    return sent[0]

# for / root, return Hello Word
@app.route("/")
def root():
    return f"Congrats! EC2 Flask Server is working"

@app.route('/get_sentiment',methods=['POST'])
def get_sentiment():
    tx = request.get_json(force=True)
    text=tx['Review']
    sent=get_prediction(text)
    return jsonify(result = sent)


app.run()
