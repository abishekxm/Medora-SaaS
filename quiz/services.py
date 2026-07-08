import json
from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_ai_quiz(topic):
    prompt = f"""
Return ONLY valid JSON.

Generate exactly 10 NEET multiple-choice questions about "{topic}".

Format:

[
  {{
    "question": "...",
    "options": [
      "...",
      "...",
      "...",
      "..."
    ],
    "answer": "..."
  }}
]

Rules:
- Output only JSON.
- No markdown.
- No explanations.
- No headings.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You generate only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()

    content = (
        content.replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(content)