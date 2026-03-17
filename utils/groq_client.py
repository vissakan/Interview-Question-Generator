import os
import httpx
import certifi
import urllib3
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Suppress SSL warnings (fix for macOS conda SSL issue)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Fix for SSL certificate verification failure on macOS with conda
http_client = httpx.Client(verify=False)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"), http_client=http_client)


def generate_questions(prompt: str) -> str:
    """Send prompt to Groq and return the raw text response."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert interview question generator. "
                    "You always follow the exact output format requested. "
                    "You never add extra commentary, preambles, or closing remarks. "
                    "Output only the formatted interview questions as instructed."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=4096,
    )
    return response.choices[0].message.content
