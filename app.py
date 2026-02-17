from flask import *
from  nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		review = request.form.get("review")
		sia = SentimentIntensityAnalyzer()	
		ps = sia.polarity_scores(review)
		feedback = ""
		if ps["compound"] >= 0.05:
			feedback = "thanks for positive review"
		elif ps["compound"] <= -0.05:
			feedback = "sorry for ur negative review "
		else:
			feedback = "neutral"
		msg = " got it " + feedback 
		return render_template("home.html", msg=msg)
	else:
		return render_template("home.html")
		
# app.run(debug=True, use_reloader=True)