WHATSAPP FLOW - EMPER.AI

🔹 Entry Point:
Recruiters or job seekers message the Emper.ai WhatsApp Business number.

🔹 Auto-Reply Options:
1. For Recruiters
   - "Hire talent" → Sends Google Form for recruiter job details
   - "Pricing" → Sends pricing tiers (e.g., ₹499/month for 10 matches/week)
   - "Support" → Connects to a human assistant via WhatsApp or call

2. For Job Seekers
   - "Find job" → Sends Google Form for uploading resume and details
   - "Track application" → Auto-replies that status updates come via email or Telegram
   - "Support" → Same support flow as recruiters

🔹 Human Escalation:
- After 3 invalid attempts or if user types "Talk to human", forward to support person on call/WhatsApp.

🔹 Weekend Reminder:
- Recruiters receive WhatsApp message every Saturday: 
  "Hi [Name], your Emper.ai matches are ready! Check Telegram or upgrade plan to get more candidates."






📦 EMPER.AI - COMPLETE FLOW & USAGE OVERVIEW

👤 USER FLOW:
1. Recruiter visits Emper.ai and clicks "Hire Talent"
2. Fills a Google Form (e.g., Company Name, Job Title, Required Skills, Custom Requirements, etc.)
3. Job Seekers fill a similar form with skills, resume summary, and expected salary

🧠 MATCHING LOGIC (ai-matching-logic.py):
- Every weekend, the system:
  a. Loads job_seekers.xlsx and recruiters.xlsx
  b. Filters based on skills/experience/location
  c. Sends each recruiter 10–20 matched candidates using GPT-generated descriptions

🔍 SAMPLE GPT PROMPT:
Prompt sent to GPT for matching:

You are a recruitment AI. Given the following recruiter requirement and a list of job seekers, choose the top 10 best matches.

Recruiter Job:
- Job Title: Data Analyst
- Skills: SQL, Excel, Tableau
- Experience: 3–5 years
- Custom Requirement: Must have worked on financial datasets

Job Seekers:
1. Vikram Singh: SQL, Excel, Tableau | 3 yrs | B.Sc | Worked in finance domain
2. Anjali Rao: Python, Django | 4 yrs | B.Tech
3. Suman Joshi: AWS, Docker | 6 yrs | DevOps role

Return: Top 10 matches with short reason.

🎯 GPT RESPONSE:

Top Matches:
1. Vikram Singh – Matches all required skills and finance background.
2. Neha Sharma – Skilled in testing, but may fit if analytics role requires QA input.
