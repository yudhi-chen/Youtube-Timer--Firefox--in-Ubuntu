# 📺Ubuntu YouTube Timer (Parental Control Tool)<br>
A lightweight Python-based timer tool for Ubuntu Linux that helps parents control screen time when children watch YouTube or YouTube Kids using Firefox. <br>
This tool launches YouTube with a predefined timer (5 / 10 / 15 / 25 minutes) and automatically closes the session when time is up.

## 📌 **Features**<br>
- ⏱️ One-click timer selection (5, 10, 15, 25 minutes)<br>
- 🌐 Opens YouTube / YouTube Kids in Firefox<br>
- 👨‍👩‍👧 Designed for parental control<br>
- 🔒 Uses separate Firefox profiles (parent vs child)<br>
- 🖥️ Simple GUI interface (Python-based)<br>
- 🔊 Optional sound feedback on button click<br>

## 🧠 **Concept**<br>
This project is designed as a controlled access system:<br>
- Parent selects a timer duration<br>
- App launches YouTube (or YouTube Kids)<br>
- Child watches within the allowed time<br>
- Session automatically ends after timer expires<br>

## 🛠️ **Requirements**<br>
Make sure the following are installed:<br>
`sudo apt update`<br>
`sudo apt install python3 python3-tk firefox`<br>

## 📁 **Project Structure**<br>
youtube-timer/<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── main.py      # Main application script<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── icons/       # App icons (YouTube / YouTube Kids)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── sounds/      # Optional click sound<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── README.md<br>

## 🔧 **Setup Guide**<br>
**1. Clone Repository**<br>
`git clone https://github.com/YOUR_USERNAME/youtube-timer.git`<br>
`cd youtube-timer`<br>

**2. Create Firefox Profiles**<br>
Run:<br>
`firefox --ProfileManager`<br>
Create:<br>
youtube → for normal YouTube<br>
youtube-kids → for kids content<br>
(Optional: log in with separate Google accounts)<br>

**3. Update Python Script**<br>
Inside `main.py`, configure:<br>
`YOUTUBE_URL = "https://www.youtube.com"`<br>
`YOUTUBE_KIDS_URL = "https://www.youtube.com/kids"`<br>
`FIREFOX_PROFILE_YT = "youtube"`<br>
`FIREFOX_PROFILE_KIDS = "youtube-kids"`<br>

## ▶️ **How to Run**<br>
`python3 main.py`<br>

## 🎮 **Usage**<br>
- Launch the app<br>
- Select icon:<br>
&nbsp;&nbsp;&nbsp;&nbsp;YouTube<br>
&nbsp;&nbsp;&nbsp;&nbsp;YouTube Kids<br>
- Choose timer:<br>
&nbsp;&nbsp;&nbsp;&nbsp;5 min<br>
&nbsp;&nbsp;&nbsp;&nbsp;10 min<br>
&nbsp;&nbsp;&nbsp;&nbsp;15 min<br>
&nbsp;&nbsp;&nbsp;&nbsp;25 min<br>
- Browser opens automatically<br>
- Timer starts counting<br>
- Browser closes when time ends<br>

## 👨‍💻 Author<br>
Developed as a personal project to support structured digital learning for children.
