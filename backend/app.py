""" 
Flask Backend
Testing if everything works
"""
from flask import Flask, jsonify
# Imports specific class Flash from the flask library, jsonify is a function that converts python dictionaries to JSON format
app = Flask(__name__)
# __name__ is a special variable in Python that represents the name of the current file

@app.route('/')
def home():
    return """
    <h1> RiftInsights Backend </h1>
    <p> Server is running </p>
    <p> Try: <a href = "/test">test</a> </p>
"""

@app.route('/test')
def test():
    return jsonify({
        "status": "success",
        "message": "Backend is working!",
        "stack": {
            "backend": "Flask",
            "ai": "OpenAI GPT-4",
            "data": "JSON files"
        }
    })

if __name__ == '__main__':
    print("=" * 50)
    print("RiftInsights Backend Starting...")
    print("=" * 50)
    app.run(debug=True, port=5000)