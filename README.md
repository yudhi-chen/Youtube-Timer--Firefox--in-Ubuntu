# 📺Ubuntu YouTube Timer (Parental Control Tool)
A lightweight Python-based timer tool for Ubuntu Linux that helps parents control screen time when children watch YouTube or YouTube Kids using Firefox. <br>
This tool launches YouTube with a predefined timer (5 / 10 / 15 / 25 minutes) and automatically closes the session when time is up.

## 📌 Features
- ⏱️ One-click timer selection (5, 10, 15, 25 minutes)<br>
- 🌐 Opens YouTube / YouTube Kids in Firefox<br>
- 👨‍👩‍👧 Designed for parental control<br>
- 🔒 Uses separate Firefox profiles (parent vs child)<br>
- 🖥️ Simple GUI interface (Python-based)<br>
- 🔊 Optional sound feedback on button click<br>

## 🧠 Concept
This project is designed as a controlled access system:<br>
- Parent selects a timer duration<br>
- App launches YouTube (or YouTube Kids)<br>
- Child watches within the allowed time<br>
- Session automatically ends after timer expires<br>

## ▶️ Requirements & How to Run
Refer to the [Setup Guide](./SETUP_GUIDE.md) for full instructions.

## 📁 Project Structure
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~/apps/youtube-timer/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── YouTubeTimerFirefox.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── launch_youtube_timer.sh<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── launch_youtubekids_timer.sh<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── icons/<br>

## 🎮 Usage
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

## 👨‍💻 Author
Developed as a personal project to support structured digital learning for children.

## 🎥 Demo
▶️ Watch how the YouTube Timer works in action:  
[Click here to view demo](2026-04-19-ubuntu_youtube_demo.mp4)

## 💡 Blocking YouTube Ads
This app does not include an ad blocker directly in the Python file.<br>
The ad blocker is handled by Firefox, not by the Python script.<br>
This keeps the Python file simple and avoids needing to modify the app code.<br>

The timer app only launches Firefox using separate Firefox profiles:<br>
&nbsp;&nbsp;&nbsp;&nbsp;*mainYT* for normal YouTube<br>
&nbsp;&nbsp;&nbsp;&nbsp;*kidsYT* for YouTube Kids<br>

⚠️ To block ads, install *uBlock Origin* inside each Firefox profile.<br>

**Setup**<br>
&nbsp;&nbsp;&nbsp;&nbsp;Run YouTube mode first:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*python3 YouTubeTimerFirefox.py youtube*<br>
&nbsp;&nbsp;&nbsp;&nbsp;When Firefox opens, install *uBlock Origin* from Firefox Add-ons.<br>

&nbsp;&nbsp;&nbsp;&nbsp;Then run Kids mode:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*python3 YouTubeTimerFirefox.py kids*<br>
&nbsp;&nbsp;&nbsp;&nbsp;Install *uBlock Origin* again inside this profile.<br>

After that, the timer app will continue working normally, but Firefox will open with ad blocking enabled.
