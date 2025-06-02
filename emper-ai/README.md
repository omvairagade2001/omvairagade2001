# 🧠 Emper.ai – GPT-Powered Hiring Platform

> The future of hiring — fully automated, form-based GPT matchmaking that delivers top candidates over Telegram, every weekend. No apps, no filters, just results.

---

## 🚀 What is Emper.ai?

**Emper.ai** is India’s first **GPT-powered job matching platform** for both skilled and unskilled workers.

The system is designed to be ultra-simple and fully automated:
- Recruiters fill out a **Google Form** describing their needs (with a free-form "custom requirement" field).
- Job seekers fill a **separate Google Form** with details like location, skill, expected pay, etc.
- Every weekend, Emper.ai matches the best candidates for each recruiter using **GPT-4 mini** — and sends the list via **Telegram Bot**.
- Payment reminders go via **Gmail**, and support is handled over **WhatsApp Business or phone**.

This platform was **built solo**, from scratch, and optimized for scale using prompt engineering, Python, and automated cloud workflows.

---

## 🧠 Key Highlights

✅ GPT-powered custom job matching  
✅ Weekly automation — no login, no dashboard needed  
✅ Telegram bot delivery (top 10–20 candidates based on plan)  
✅ Excel → AI → Telegram flow  
✅ Handles vague, free-form job requests (e.g., “maid who also cooks veg in Nagpur”)  
✅ Modular, scalable system with fallback logic and chunking  

---

## 🧩 Real-World Workflow

```text
Recruiter Form (Google Forms)    👷 Job Seeker Form (Google Forms)
            │                                  │
     Stored as Excel                    Stored as Excel
            │                                  │
            └─────▶  Python Matching Engine ◀────┘
                         (Runs every weekend)
                                │
                        GPT-4 Mini Prompt Engine
                                │
              🔄 Chunk → Compare → Filter → Rank
                                │
                📩 Send Top 10–20 via Telegram Bot
                                │
                 Gmail (payment reminders if needed)
                   WhatsApp (for subscription help)
```

## 🧠 Sample Use Cases
```
Recruiter Input                                                                 What Emper.ai Does
1 “Need a female tailor in Nagpur ₹5000/mo, must know blouse stitching”      	-Interprets gender, location, budget, and skill → filters                                                                                matching candidates
2 “Looking for a cook who also does dishes in Nagpur, ₹7000”                	-Understands dual-role requirement and budget → filters                                                                                  multi-skilled workers
3 “Need a part-time maid in the morning for 2 hours”	                        -Parses time-based need, schedule, and city → matches                                                                                    part-timers


⸻

## ⚙️ Architecture
```
Google Forms (Recruiters & Seekers)
          ↓
    Excel Exports (.xlsx)
          ↓
  🐍 Python Logic & Chunking
          ↓
   🧠 GPT-4 Mini Prompt Engine
          ↓
 Telegram API (Send Matched List)
          ↓
Gmail SMTP (For payment follow-ups)
          ↓
WhatsApp Business (Support & Upgrades)


⸻

🔧 Tech Stack

Layer	Tools / Services
Language Model	OpenAI GPT-4 Mini (via API)
Backend Logic	Python, Pandas, Prompt Engineering
Form Inputs	Google Forms (converted to Excel)
Data Processing	Excel (Pandas), CSV, Custom Chunking Logic
Messaging	Telegram Bot API (pyTelegramBotAPI)
Email Reminders	Gmail SMTP
Support Channel	WhatsApp Business
Hosting / Infra	Azure VM or Local Server (scheduled via CRON)


⸻

🧠 GPT Matching Logic (Simplified Pseudocode)

for recruiter in recruiter_list:
    job_description = format_job_prompt(recruiter)
    
    matches = []
    for chunk in chunkify(job_seekers, size=15):
        gpt_input = build_prompt(job_description, chunk)
        result = gpt_call(gpt_input)
        matches += parse_response(result)

    top_matches = rank_top_n(matches, recruiter.subscription_tier)
    send_to_telegram(recruiter.telegram_id, top_matches)


⸻

📁 Project Structure

emper-ai/
├── README.md                    ← Full documentation (this file)
├── ai-matching-logic.py        ← Main GPT loop & filtering engine
├── prompt_builder.py           ← Converts job post to GPT-compatible prompt
├── telegram_bot_sender.py      ← Sends results via Telegram
├── gpt_chunking.py             ← Handles long job seeker lists
├── email_reminder.py           ← Sends payment follow-up via Gmail
├── whatsapp-flow.md            ← Escalation & support logic
├── recruiters.xlsx             ← Sample recruiter Google Form export
├── job_seekers.xlsx            ← Sample job seeker form export
├── requirements.txt            ← Python dependencies
└── __init__.py                 ← (Optional) Python package initializer


⸻

🔥 Competitive Advantage

Feature	Legacy Platforms	Emper.ai
Free-form recruiter inputs	❌	✅
GPT-based AI matching	❌	✅
Works via Telegram	❌	✅
Handles low-tech job seekers	❌	✅
Zero login, no portal	❌	✅


⸻

💡 Future Plans
	•	Switch to PostgreSQL database for scale
	•	Add employer feedback loop for rating matches
	•	Enable resume generation for job seekers using GPT
	•	API-based recruiter onboarding (instead of forms)

⸻

👨‍💻 Built By

Om Vairagade
Founder – Emper.ai | AI Developer @ TCS
📍 Nagpur, Maharashtra
📧 omvairagade2001@gmail.com
🔗 LinkedIn
🔗 GitHub

⸻

🚀 “Emper.ai doesn’t just recommend — it understands your hiring needs.”

---

## ✅ Next Step

You're now ready to build the **repo files** listed in this README:

1. `ai-matching-logic.py`
2. `prompt_builder.py`
3. `telegram_bot_sender.py`
4. `gpt_chunking.py`
5. `email_reminder.py`
6. `whatsapp-flow.md`
7. `requirements.txt`
8. Sample: `recruiters.xlsx`, `job_seekers.xlsx`

Shall I begin generating each one, starting with `ai-matching-logic.py`?
