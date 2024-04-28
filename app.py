from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    isbn = request.form['isbn']
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}")
    data = response.json()
    return render_template('results.html', books=data.get('items', []))

if __name__ == '__main__':
    app.run(debug=True)
