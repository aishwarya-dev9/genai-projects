from ollama import chat

#review= "The food was amazing but the service was slow."
reviews = [
    "Food was amazing and staff were friendly.",
    "Very bad service and cold food.",
    "Average experience, nothing special.",
    "Great ambiance but expensive prices."
]
for review in reviews:
    prompt = f"""
    You are a sentiment analysis expert.
    Review:
    {review}

    Return ONLY in this format:

    Sentiment: Positive/Negative/Neutral/Mixed
    Reason: One sentence explanation
    """

    response = chat(
        model="phi3",
        messages=[
            {"role": "user",
            "content": prompt}
        ]
    )
    print(response["message"]["content"])