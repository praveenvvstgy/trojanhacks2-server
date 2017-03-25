from flask import Flask
app = Flask(__name__)
from facebook import *
import json

@app.route("/")
def hello():
	graph = GraphAPI("EAAF18IdZCWz8BAGdIMMbLK8nmtP1oPYzaKUi6pHsQ9sgv4QWNflJmpOPziMZAdfOZAuwHfztfRE7nvG1iZAy7l4MgvscYCB1ZAiyzGANZCjBtuJa9CbMUH7Uwae6GcnLs3SyOvFOZC1UxhWpBdnfZAAdwl4nyYOus6UZD")
	return json.dumps(graph.get('333039026750643/feed'))

@app.route("/callback")
def callback():
	return ""

if __name__ == "__main__":
    app.run(debug=True)