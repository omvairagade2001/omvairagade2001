# 🧠 Emper AI – Smart CCTV Alert System  
**World’s First Agentic AI Surveillance System**  
_Developed under the Emper.ai initiative by [Om Vairagade](https://www.linkedin.com/in/omvairagade2001)_

---

## 🚀 Overview

**Emper AI CCTV** is an autonomous, AI-powered surveillance system that analyzes **live RTSP camera feeds** in real time and generates **instant Telegram alerts** for critical on-ground events — all without manual supervision.

This system blends **Computer Vision**, **SLMs (Cannot Reveal)**, and **edge automation** to detect unusual or defined activities such as:
- 💤 **Sleeping or idle guards**  
- 🎒 **Unattended bags or objects**  
- 👨‍👩‍👧 **Lost children or missing persons**  
- 🧍‍♂️ **Crowd formation or congestion zones**  
- 🐕 **Animals entering restricted areas**

---

## 🧩 Core Concept

> _“Turn any normal CCTV system into an intelligent, self-operating security agent.”_

The model continuously captures camera snapshots, processes them on a cloud AI server, and sends structured real-time alerts (with images) to a **Telegram channel** or **security dashboard**.

Example output:
  1.	garden cam 3: person without uniform
	2.	temple gate cam 1: unattended bag detected
	3.	hall cam 2: child in yellow shirt seen near exit
---

## ⚙️ Technical Architecture

**Client (Edge Device – Android / Raspberry Pi):**
- Runs on **Termux** with periodic image capture using a shell script (`snapshot.sh`)
- Securely transmits snapshots via **Tailscale** to cloud backend

**Server (Azure VM):**
- Flask-based API for image ingestion
- Integrates AI model (SLM) for analysis  
- Detects events based on dynamic prompts (per camera or site)
- Compresses, encodes, and logs alerts to database
- Sends real-time **Telegram notifications** with annotated image evidence

**Performance Optimizations:**
- Frame compression to reduce latency  
- Parallel image analysis loop (≈10s cycle)  
- Caching and prompt mapping for multi-camera load  
- Secure heartbeat monitor for uptime tracking

---

## 💡 Real Deployment

📍 **Client Site:** _Koradi Mandir, Nagpur (India)_  
🗓️ **Duration:** 15-day live pilot test  
🎯 **Outcome:** Successfully detected on-ground incidents including:
- Lost child seen in yellow shirt  
- Animals roaming inside temple premises  
- Unattended tools/equipment left on floor  
- Overcrowding near entry zones  
- People sitting or sleeping in restricted areas  

🧾 Alerts were delivered instantly via Telegram, enabling faster staff response and real-time situational awareness.

---

## 🧠 AI Stack

| Layer | Technology |
|:------|:------------|
| **Large Language Models** | SLM |
| **Vision Models** | SLM |
| **Backend** | Flask, Python, Azure VM |
| **Automation & Networking** | Tailscale, Termux, Cron Jobs |
| **Notifications** | Telegram Bot API |
| **Data Handling** | Base64 Encoding, Image Compression, JSON Logging |

---

## 🔐 Features

- Real-time multi-camera analysis (supports 9+ feeds per grid)
- Custom prompts per camera (e.g., *“if anyone without uniform”*)
- Autonomous decision-making & numbered alert mapping
- Works on limited internet and low-end hardware
- End-to-end encrypted data transmission
- Fully modular and scalable for enterprise environments

---

## 🧰 Setup Overview (Simplified)

1. **Configure Camera IP (RTSP / Snapshot URL)**  
2. **Run `snapshot.sh`** on edge client (Android/Raspberry Pi)  
3. **Connect to Cloud VM** via Tailscale for secure upload  
4. **Start Flask Server** (`main.py`) on Azure VM  
5. **Receive Alerts** instantly on Telegram  

*(Detailed setup instructions available upon request — private repository)*

---

## 📸 Sample Results

> “These are example detections from the 15-day Koradi Mandir pilot.”

- 🟢 Equipment lying on floor  
- 🟢 People in white attire detected  
- 🟢 Lost child seen in yellow shirt  
- 🟢 Crowd congestion near entrance  
- 🟢 Unattended bag detected  

_All detections verified manually by on-site staff._

---

## 🧭 Vision Ahead

Emper AI is evolving into a **full-scale agentic surveillance platform**, integrating:  
- Autonomous voice alerts  
- Behavior prediction models  
- Centralized multi-location dashboards  
- Integration with local law enforcement & IoT sensors

---

## 👤 Author

**Om Vairagade**  
Agentic AI Developer & Architect  
📍 Nagpur, India  
📧 omvairagade2001@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/omvairagade2001) | [GitHub](https://github.com/omvairagade2001)

---

> ⚠️ _Note:_ Core model architecture and code are proprietary to **Emper.ai**. This repository is for **demonstration and documentation** purposes only. Full implementations are available upon request for enterprise or research collaboration.
