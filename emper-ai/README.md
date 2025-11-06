# 🧠 Emper.ai (NAUKRIZZ) – AI-Powered Hiring Platform

> The future of hiring — fully automated, form-based GPT matchmaking that delivers top candidates over Telegram, every weekend. No apps, no filters, just results.

---

## 🚀 What is NAUKRIZZ?

**NAUKRIZZ** is India’s first **AI-powered job matching platform** for both skilled and unskilled workers.

The system is designed to be ultra-simple and fully automated:
- Recruiters fill out a ** Form** describing their needs (with a free-form "custom requirement" field).
- Job seekers fill a **separate Form** with details like location, skill, expected pay, etc.
- NAUKRIZZ matches the best candidates for each recruiter using my **Fine tuned  & Trained SLM** — and Shows the list in **NAUKRIZZ results portal**.

This platform was **built solo**, from scratch, and optimized for scale using prompt engineering, Python, and automated cloud workflows.

---

## 🧠 Key Highlights

✅ AI-powered custom job matching    
✅ Accurate Matches delivery (top 10–20 candidates based on plan)  
✅ Handles vague, free-form job requests (e.g., “maid who also cooks veg in Nagpur”)  
✅ Modular, scalable system with fallback logic and chunking  

---

## 🧩 Real-World Workflow

```text
    Recruiter Form                       👷 Job Seeker Form 
            │                                  │
     Stored as Excel                    Stored as Excel
            │                                  │
            └─────▶  Python Matching Engine ◀────┘
                         (Runs on a single click)
                                │
                        AI Prompt Engine
                                │
              🔄 Chunk → Compare → Filter → Rank
                                │
                📩 Show Top 10–20 on RESULTS page
                                
```

## 🧠 Sample Use Cases
```
Recruiter Input                                                                 What Emper.ai Does
1 “Need a female tailor in Nagpur ₹5000/mo, must know blouse stitching”      	-Interprets gender, location, budget, and skill → filters                                                                                matching candidates
2 “Looking for a cook who also does dishes in Nagpur, ₹7000”                	-Understands dual-role requirement and budget → filters                                                                                  multi-skilled workers
3 “Need a part-time maid in the morning for 2 hours”	                        -Parses time-based need, schedule, and city → matches                                                                                    part-timers

```
⸻

## ⚙️ Architecture
```
 Forms (Recruiters & Seekers)
          ↓
  🐍 Python Logic & Chunking
          ↓
   🧠 AI Prompt Engine
          ↓
   (Show Matched List)


⸻
```
🔧 Tech Stack
```
Layer										Tools / Services
Language Model									SLM
Backend Logic									Python, Pandas, Prompt Engineering
Form Inputs									    Databse (Postgre SQL)
Data Processing									Custom Chunking Logic
Hosting / Infra									Azure VM or Local Server (scheduled via CRON)

```



📁 Project Structure
```
emper-ai/
├── README.md                    ← Full documentation (this file)
├── ai-matching-logic.py        ← Main ai loop & filtering engine
├── prompt_builder.py           ← Converts job post to ai-compatible prompt
├── bot_sender.py               ← Sends results on portal
├── ai_chunking.py              ← Handles long job seeker lists
├── requirements.txt            ← Python dependencies
└── __init__.py                 ← (Optional) Python package initializer
```

⸻

⸻

#💡 Future Plans
```
	•	Add employer feedback loop for rating matches
	•	Enable resume generation for job seekers using ai
	•	API-based recruiter onboarding 

⸻
```
👨‍💻 Built By
```
Om Vairagade
Founder – Emper.ai | AI Developer @ TCS
📍 Nagpur, Maharashtra
📧 omvairagade2001@gmail.com
```
⸻

🚀 “Emper.ai doesn’t just recommend — it understands your hiring needs.”

---

