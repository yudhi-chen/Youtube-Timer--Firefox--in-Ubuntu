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

## ▶️ **Requirements & How to Run**<br>
Refer to the [Setup Guide](./SETUP_GUIDE.md) for full instructions.

## 📁 **Project Structure**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~/apps/youtube-timer/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── YouTubeTimerFirefox.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── launch_youtube_timer.sh<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── launch_youtubekids_timer.sh<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── icons/<br>

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
