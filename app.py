from flask import *
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        review = request.form.get("review")
        sia = SentimentIntensityAnalyzer()	
        ps = sia.polarity_scores(review)

        if ps["compound"] >= 0.05:
            feedback = "thanks for positive review"
        elif ps["compound"] <= -0.05:
            feedback = "sorry for your negative review"
        else:
            feedback = "neutral"

        msg = "Got it: " + feedback 
        return render_template("home.html", msg=msg)
    else:
        return render_template("home.html")
