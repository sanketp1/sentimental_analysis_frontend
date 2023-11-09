from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        result = analyze_sentiment(text)

    return render_template('index.html', result=result)

def analyze_sentiment(text):
    # Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your sentimental analysis API
    api_endpoint = 'https://api-sentimental-analysis-service.onrender.com/api/v1/sentiment'
    payload = {'text': text}
    response = requests.post(api_endpoint, json=payload)

    if response.status_code == 200:
        result = response.json()['data']
        return result
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
