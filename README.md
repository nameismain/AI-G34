<h1 align="center">💨 PureCare · AI-Driven Symptom-Responsive Air Purifier</h1>
<p align="center">
  <b>ITE351 – AI & Applications · Group 34</b><br>
  <i>Hanyang University, Fall 2025</i><br>
  <a href="https://nameismain.github.io/AI-G34/">🌐 Live Site</a> · 
  <a href="https://uumarina.notion.site/">🧠 Notion Workspace</a>
</p>

---

## 🌿 Overview
**PureCare** is an AI-powered air purification system that listens, learns, and adapts.  
Instead of merely reacting to air quality levels, it uses **audio-based symptom recognition** —  
detecting coughs and sneezes to provide **personalized, health-aware air management**.

> 🩺 Turning air purifiers into proactive wellness companions.

---

## 🎯 Objectives
- Develop an **AI model** capable of detecting coughs and sneezes in realistic indoor conditions.  
- Learn **user-specific patterns** and link sound cues to health context.  
- Automatically **adjust purification speed and mode** based on detected symptoms.  
- Build an **edge-deployed prototype** using Raspberry Pi 4 for local, privacy-preserving inference.

---

## 🧪 Planned Methodology

### 1️⃣ Audio Data Collection
Following *Acoustic Cues for Person Identification using Cough Sounds (Tran et al.)*  
each participant records **40 ten-second samples** (coughs/sneezes) across **5 sessions** on different days.

| Variable | Variations |
|-----------|-------------|
| **Physical State** | Rest · After walking · After running · After climbing stairs |
| **Distance & Angle** | 0 – 3 m, multiple room positions |
| **Body Orientation** | Facing / sideways / angled from mic |
| **Environment** | Quiet · TV/music · Appliances · Open windows |

> 🎙️ Recorded indoors using `hardware/tools/audio_capture.py`  
> Device remains fixed to simulate a purifier placement.

---

### 2️⃣ Metadata & Labeling
Each recording logged in **`notes.csv`** with:
user_id, file_name, day, sample_no, is_cough, physical_activity, bg_noise, distance, cough_type
Example:  
`M1US20-01, manual_save_time1761366192.csv, 0, 3, 1, rest, music+window, 2m, throat_clearing`

Dataset supports both **symptom detection** and **person-identification research**.

---

### 3️⃣ AI Model Development
| Module | Description |
|:--|:--|
| **Sound Recognition** | CNN trained on MFCC features to classify cough/sneeze/background |
| **Adaptive Control** | Regression / RL model to dynamically tune purifier speed and mode |
| **User Identification** | Embedding + clustering to associate new coughs with existing users |

---

### 4️⃣ Integration & Testing
- Deploy trained models to **Raspberry Pi 4**  
- Perform **local real-time inference** to ensure low latency and privacy  
- Evaluate with real indoor recordings and live user interaction  

---

### 5️⃣ Evaluation & Optimization
| Metric | Description |
|---------|-------------|
| Accuracy | Symptom classification performance |
| False Positives | Model reliability under background noise |
| Latency | On-device inference time |
| Energy Efficiency | Power use vs. baseline purifier |
| User Feedback | Comfort / perceived responsiveness |

---

## 🧠 Tech Stack

| Category | Tools & Frameworks |
|-----------|-------------------|
| **AI / ML** | Python · TensorFlow · PyTorch · Keras |
| **Signal Processing** | Librosa · NumPy · pandas |
| **Hardware** | Raspberry Pi 4 · USB mic sensors |
| **Frontend / Docs** | HTML · CSS (Dark Theme) · GitHub Pages · Figma |
| **Collaboration** | Notion · GitHub · Google Drive |

---

## 👥 Team 34

| Name | Department | Contact |
|------|-------------|---------|
| **Minjin Kim** | Information Systems | idid02@hanyang.ac.kr |
| **Taehyun Kim** | Computer Science | tanggu01@connect.hku.hk |
| **Lison Olympie** | Computer Science | lsn.olmp@gmail.com |
| **Tom Georgin** | Computer Science | tom@georgin.net |

---

<p align="center">
  <sub>📅 Last updated: 2025-10-30 · Dept. of Information Systems, Hanyang University</sub><br>
  <sub>💻 Repository Contents: <code>index.html</code> · <code>assets/</code> · <code>README.md</code></sub>
</p>
