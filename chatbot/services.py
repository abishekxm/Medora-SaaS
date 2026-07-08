from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def get_ai_response(user_input, context_history=None):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Medora AI, a helpful medical assistant. "
                        "Provide general medical information only. "
                        "Do not diagnose diseases or prescribe medicines. "
                        "Always recommend consulting a qualified doctor for emergencies."
                    ),
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
            temperature=0.5,
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
    
    