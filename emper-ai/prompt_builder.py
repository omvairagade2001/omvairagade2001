# prompt_builder.py

"""
Generates a GPT-compatible prompt from recruiter data.

This module converts recruiter form input into a structured prompt
that GPT-4 mini can understand and use to match job seekers.

Author: Om Vairagade
"""

def build_prompt(recruiter_row):
    """
    Accepts a single row (Series) from recruiter_df.
    Returns a string prompt formatted for GPT-4 mini.

    Parameters:
    - recruiter_row: Pandas Series (one recruiter's form response)

    Expected recruiter fields:
    - name, city, role, gender_preference, budget, custom_requirement
    """

    name = recruiter_row.get("name", "Recruiter")
    city = recruiter_row.get("city", "")
    role = recruiter_row.get("role", "")
    gender = recruiter_row.get("gender_preference", "any")
    budget = recruiter_row.get("budget", "")
    requirements = recruiter_row.get("custom_requirement", "")

    prompt = f"""
You are an intelligent AI job assistant.

A recruiter named {name} is looking to hire for the following role:

- Role: {role}
- Location: {city}
- Preferred Gender: {gender}
- Budget: ₹{budget}
- Custom Requirements: {requirements}

You are given a list of job seekers in JSON format.

Your task is to:
1. Understand the job description.
2. Match the most relevant candidates.
3. Rank them based on suitability (location, role, skills, gender, budget).
4. Return only the top candidates as a list of JSON objects (max 10 per call).

Respond in the following format:
[
  {{
    "id": "JS123",
    "name": "Priya Sharma",
    "city": "Nagpur",
    "role": "Cook",
    "skills": ["Vegetarian", "Cleaning"],
    "expected_salary": 7000
  }},
  ...
]

Only include candidates who closely fit the job. Be strict about location, salary, and skills. If gender is specified, honor that too.

Reply ONLY with a JSON array. Do not add any explanation or extra text.
"""

    return prompt.strip()
