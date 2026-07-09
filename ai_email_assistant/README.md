# ✉️ Local AI Email Assistant

A local Generative AI application that converts rough notes into well-structured emails using **Llama 3** running locally via **Ollama**. The application is built with **Streamlit** and operates entirely offline without relying on external AI APIs.

## Features

* Generate professional emails from rough notes
* Multiple email tones (Professional, Friendly, Apologetic, Direct)
* Powered by a local LLM using Ollama
* Offline AI inference
* Download generated emails as a `.txt` file

## Tech Stack

* Python
* Streamlit
* Ollama
* Llama 3
* Prompt Engineering

## Installation

```bash
git clone <repository-url>
cd local-ai-email-assistant

python -m venv venv

# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download the model
ollama pull llama3

# Run the application
streamlit run app.py
```

## How It Works

1. Enter rough notes.
2. Select an email tone.
3. The application builds a prompt based on the selected tone.
4. Ollama sends the prompt to the local Llama 3 model.
5. The generated email is displayed and can be downloaded.

## Author

**Aishwarya Hakkaladaddi**
