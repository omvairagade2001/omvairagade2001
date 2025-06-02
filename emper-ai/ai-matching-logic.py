# ai-matching-logic.py

"""
Main logic to:
1. Load recruiter and job seeker data from Excel
2. Build prompts using recruiter job description
3. Chunk job seeker data
4. Call GPT API for each chunk
5. Merge and rank matches
6. Send results via Telegram

Author: Om Vairagade
"""

import pandas as pd
from prompt_builder import build_prompt
from gpt_chunking import chunk_job_seekers
from telegram_bot_sender import send_to_telegram
from email_reminder import send_payment_reminder
from openai import OpenAI  # Replace with actual GPT library or API wrapper

# Replace with your GPT key and initialization
gpt = OpenAI(api_key="your-openai-api-key")


# Load recruiter and job seeker Excel data
recruiter_df = pd.read_excel("recruiters.xlsx")
job_seeker_df = pd.read_excel("job_seekers.xlsx")


def get_top_n(matches, n):
    """
    Deduplicates and selects top-N matches.
    GPT response must contain ranked profiles or IDs.
    """
    seen = set()
    top_n = []
    for match in matches:
        if match['id'] not in seen:
            top_n.append(match)
            seen.add(match['id'])
        if len(top_n) >= n:
            break
    return top_n


def process_all_recruiters():
    for index, recruiter in recruiter_df.iterrows():
        print(f"\n🚀 Processing recruiter: {recruiter['name']}")

        # 1. Build job prompt
        job_prompt = build_prompt(recruiter)

        # 2. Chunk job seekers
        seeker_chunks = chunk_job_seekers(job_seeker_df, chunk_size=15)

        # 3. Loop GPT over chunks
        all_matches = []
        for chunk in seeker_chunks:
            gpt_input = {
                "job_description": job_prompt,
                "candidates": chunk.to_dict(orient="records")
            }

            try:
                result = gpt.chat_completion(gpt_input)  # or your GPT wrapper
                matches = result.get("matches", [])
                all_matches += matches
            except Exception as e:
                print(f"❌ GPT API Error: {e}")
                continue

        # 4. Filter top N based on recruiter’s plan
        sub_plan = recruiter.get("subscription", "basic").lower()
        top_n = 10 if "basic" in sub_plan else 15 if "pro" in sub_plan else 20
        final_matches = get_top_n(all_matches, n=top_n)

        # 5. Send via Telegram
        if recruiter.get("telegram_id"):
            send_to_telegram(recruiter["telegram_id"], final_matches)
        else:
            print("⚠️ No Telegram ID found — skipping.")

        # 6. Send payment reminder if flagged
        if recruiter.get("payment_due") == "yes":
            send_payment_reminder(recruiter)


if __name__ == "__main__":
    process_all_recruiters()
"""
Dependencies you should have: 
prompt_builder.py
  -Formats job descriptions into GPT-friendly prompts
gpt_chunking.py
  -Splits large seeker datasets into GPT-processable chunks
telegram_bot_sender.py
  -Sends match results via Telegram
email_reminder.py
  -Sends Gmail payment reminders
recruiters.xlsx / job_seekers.xlsx
  -Google Form outputs stored as Excel files
  
Author: Om Vairagade
"""
