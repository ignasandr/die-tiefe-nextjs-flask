from flask import Flask, jsonify
from scrape import get_data
app = Flask(__name__)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, Duderino!</p>"


@app.route("/api/scrape")
def scrape():
    data = get_data()  # Call the get_data function to get the result.
    # return jsonify(data)  # Return the result as the response.
    return jsonify(data)
