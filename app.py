from flask import Flask, render_template, request, jsonify, send_file
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
import io

app = Flask(__name__)

# Configure your API key via environment variable
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

# Placeholder for your specific API logic
@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(data.get("prompt"))
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)