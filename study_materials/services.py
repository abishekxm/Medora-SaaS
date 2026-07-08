from chatbot.services import get_ai_response


def generate_ai_study_material(subject, topic, difficulty):
    prompt = f"""
You are Medora AI, an expert NEET tutor.

Generate complete study material.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Generate in this format:

1. Topic Overview
2. Important Concepts
3. Key Points for NEET
4. Memory Tricks
5. 10 NEET MCQs
6. Answers with Explanation
7. Revision Tips

Keep the response well formatted and easy to understand.
"""

    return get_ai_response(prompt)