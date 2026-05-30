import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)


def generate_ai_report(repo_data, metrics, prediction):

    try:

        model = genai.GenerativeModel("models/gemini-1.5-flash")

        prompt = f"""
        Analyze this GitHub repository.

        Repository Name: {repo_data["name"]}
        Owner: {repo_data["owner"]}
        Stars: {repo_data["stars"]}
        Forks: {repo_data["forks"]}
        Open Issues: {repo_data["open_issues"]}
        Language: {repo_data["language"]}

        Metrics:
        {metrics}

        ML Prediction:
        {prediction}

        Give:
        1. Repository health summary
        2. Risk analysis
        3. Improvement suggestions
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"