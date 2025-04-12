import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_solution(problem: str):
    try:
        prompt = f"Explain step-by-step how to solve this equation: {problem}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Explanation error: {str(e)}"