import os
import pandas as pd
from chatbot.services import get_ai_response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "neet_cutoffs.csv")


def predict_colleges(score, category, state, quota):
    df = pd.read_csv(CSV_PATH)

    # Filter by user inputs
    df = df[
        (df["state"].str.lower() == state.lower()) &
        (df["category"].str.lower() == category.lower()) &
        (df["quota"].str.lower() == quota.lower())
    ]

    results = []

    for _, row in df.iterrows():
        cutoff = row["cutoff_score"]

        if score >= cutoff + 15:
            chance = "Safe"
        elif score >= cutoff - 10:
            chance = "Moderate"
        else:
            chance = "Dream"

        results.append({
            "college_name": row["college_name"],
            "type": row["type"],
            "fees": row["fees"],
            "cutoff": cutoff,
            "chance": chance,
        })

    return sorted(results, key=lambda x: x["cutoff"], reverse=True)

def get_ai_college_recommendation(score, category, state, quota, colleges):
    prompt = f"""
You are an expert NEET counselling advisor.

Student Details:
- NEET Score: {score}
- Category: {category}
- State: {state}
- Quota: {quota}

Predicted Colleges:
{colleges}

Provide:
1. The best college choice.
2. The safest option.
3. The dream option.
4. A short counselling advice.

Keep the answer under 150 words.
"""

    return get_ai_response(prompt)

from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_ai_roadmap(score, category, state, college):
    prompt = f"""
You are Medora AI.

Student Details:
- NEET Score: {score}
- Category: {category}
- State: {state}
- Target College: {college}

Generate a detailed roadmap with:

1. Admission Chances
2. Safe College Strategy
3. Dream College Strategy
4. Counselling Timeline
5. Required Documents
6. Preparation Tips
7. Final AI Advice

Keep it clear and well formatted.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert NEET counselling advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=700,
    )

    return response.choices[0].message.content

def get_ai_college_details(college):
    prompt = f"""
You are Medora AI.

Explain this medical college to a NEET student.

College:
{college}

Write:
1. Overview
2. Advantages
3. Who should choose this college?
4. Career opportunities
5. Final AI advice

Keep it under 200 words.
"""

    return get_ai_response(prompt)
