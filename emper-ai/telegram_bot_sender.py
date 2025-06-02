# telegram_bot_sender.py

"""
Sends GPT-matched candidates to recruiter via Telegram Bot.

Uses Telegram Bot API to send text message (or list) to Telegram user ID.

Author: Om Vairagade
"""

import requests

# Replace with your bot token (from BotFather)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


def format_candidates(candidates):
    """
    Formats candidate list into human-readable text.

    Parameters:
    - candidates: list of dicts from GPT output
    Returns:
    - A formatted multiline string
    """
    if not candidates:
        return "❌ No suitable candidates found."

    message_lines = ["🔍 *Your Top Matching Candidates:*", ""]
    for i, c in enumerate(candidates, start=1):
        entry = (
            f"*{i}. {c.get('name', 'Unknown')}* — {c.get('role', '')}\n"
            f"📍 Location: {c.get('city', '')}\n"
            f"💼 Skills: {', '.join(c.get('skills', []))}\n"
            f"💰 Expected Salary: ₹{c.get('expected_salary', 'N/A')}\n"
            f"🆔 ID: `{c.get('id', 'N/A')}`\n"
            "-------------------------"
        )
        message_lines.append(entry)

    return "\n".join(message_lines)


def send_to_telegram(chat_id, candidates):
    """
    Sends the formatted match result to the recruiter via Telegram bot.

    Parameters:
    - chat_id: Telegram user ID of recruiter (integer)
    - candidates: List of candidate dicts
    """

    message = format_candidates(candidates)

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(TELEGRAM_API_URL, json=payload)
        if response.status_code == 200:
            print(f"✅ Sent results to recruiter (Telegram ID: {chat_id})")
        else:
            print(f"❌ Telegram API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Telegram send error: {e}")
