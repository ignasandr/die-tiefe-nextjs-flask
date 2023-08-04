from flask import Flask
from scrape import get_data
app = Flask(__name__)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, Duderino!</p>"


@app.route("/api/scrape")
def scrape():
    data = get_data()  # Call the get_data function to get the result.
    return f"<p>{data}</p>"  # Return the result as the response.
