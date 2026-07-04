from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_review():
    data = request.json
    review = data.get("review")

    prompt = """
    Analyze the resturant review

    Return ONLY:
    POSITIVE
    NEGATIVE
    MIXED

    Review:
    {review}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json = {
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    return jsonify({
        "review": review,
        "sentiment": result.strip()
    })

if __name__ == '__main__':
    app.run(debug=True)

