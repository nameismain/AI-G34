# ITE351 – AI & Applications · Group 34
Course project for **Hanyang University (Fall 2025)**  
Instructor: Prof. YoungjoonWon 
Team 34 — *PureCare: AI-Driven Symptom-Responsive Air Purifier*

---

## 🌐 Live Site
➡️ [https://nameismain.github.io/AI-G34/](https://nameismain.github.io/AI-G34/)

---

## 🧠 Project Overview
**PureCare Air Purifier** is an AI-powered system designed to recognize **user health conditions** through **audio-based symptom detection**.  
Unlike conventional purifiers that only react to air quality levels, PureCare *learns from real-world cough and sneeze sounds* and adapts its behavior intelligently — adjusting fan speed, purification mode, and scheduling to provide a **personalized, health-aware home environment**.

> Goal: Transform air purifiers from passive devices into **proactive health companions**.

---

## 📊 Project Proposal (Summary)

### Objective
Develop a smart air purifier that:
- Detects coughs/sneezes via AI-based sound recognition  
- Learns user-specific patterns and health cues  
- Automatically adjusts operation based on real-time context  
- Supports multi-user personalization within shared environments  

---

## 🧩 Planned Methodology

### 1. **Audio Data Collection**
Following the paper *Acoustic Cues for Person Identification using Cough Sounds* (Tran et al.):
- Each participant records **40 ten-second audio samples** (cough/sneeze)  
- **5 recording sessions** on different days  
- Conditions vary by:
  - Physical activity before recording (rest, after walking/running/stairs)  
  - Distance & position from microphone (0–3 m, various angles)  
  - Body orientation relative to the device  
  - Indoor background noise (quiet, TV, appliances, open windows)  
- Recording tool: `hardware/tools/audio_capture.py` (fixed device position)

### 2. **Metadata & Labeling**
Each sample logged in `notes.csv`:
user_id, file_name, day, sample_no, is_cough, physical_activity, bg_noise, distance, cough_type
Example:
M1US20-01, manual_save_time1761366192.csv, 0, 3, 1, rest, music+window, 2m, throat_clearing
Dataset supports both **symptom detection** and **user identification**.

### 3. **AI Model Development**
- **Sound Recognition** – CNN trained on MFCC features to classify cough/sneeze vs noise  
- **Adaptive Control** – Regression or reinforcement model to auto-adjust purifier behavior  
- **User Identification** – Embedding & clustering to map new cough samples to known users  

### 4. **Integration & Testing**
- Deploy models on **Raspberry Pi 4**  
- Local inference for privacy & low latency  
- Evaluate in realistic indoor environments  

### 5. **Evaluation & Optimization**
- Metrics: detection accuracy, latency, false positives, energy efficiency  
- Iterative retraining with new user data and feedback  

---

## 🧑‍💻 Tech Stack
| Category | Tools |
|-----------|-------|
| Frontend | HTML, CSS (Dark Theme, Responsive), React |
| Backend / AI | Python, TensorFlow, PyTorch, Keras |
| Embedded | Raspberry Pi 4, audio sensors |
| Data | NumPy, pandas, MFCC feature extraction |
| Design & Docs | Figma, GitHub Pages, Notion |

---

## 👥 Team
| Name | Department | Email |
|------|-------------|-------|
| **Minjin Kim** | Information Systems | idid02@hanyang.ac.kr |
| **Taehyun Kim** | Computer Science | tanggu01@connect.hku.hk |
| **Lison Olympie** | Computer Science | lsn.olmp@gmail.com |
| **Tom Georgin** | Computer Science | tom@georgin.net |

---

📅 **Last updated:** 2025-10-30  
🧾 **Repository Contents:**  
- `index.html` — Website homepage (dark theme, navigation)  
- `assets/` — Images and static files  
- `README.md` — Project documentation overview  

---
