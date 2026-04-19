# 📚 SETUP_GUIDE.md — Ubuntu YouTube Timer (From Scratch)

## 🧭 Overview
This guide documents the complete step-by-step process to build the Ubuntu YouTube Timer from scratch.

**Purpose:**
- Rebuild the project anytime
- Understand the full setup logic
- Avoid repeating trial-and-error

## 🧱 Prerequisites

Install required packages:<br>
```bash
  sudo apt update
  sudo apt install python3 python3-tk firefox imagemagick
```
Explanation:<br>
• python3 → run script<br>
• python3-tk → GUI (popup + timer)<br>
• firefox → browser<br>
• imagemagick → create custom icons<br>

## CREATE PROJECT FOLDER (ORGANIZE FILES)
```bash
  mkdir -p ~/apps/youtube-timer
  cd ~/apps/youtube-timer
```
Target structure:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~/apps/youtube-timer/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── YouTubeTimerFirefox.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── launch_youtube_timer.sh<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── launch_youtubekids_timer.sh<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── icons/<br>

## CREATE FIREFOX PROFILES (SETUP PHASE)
Run:
```bash
  firefox --ProfileManager
```

*(Create profiles via GUI)*<br>
Create:<br>
• mainYT → for YouTube<br>
• kidsYT → for YouTube Kids<br>

**NOTE:**<br>
• ⚠️ This step is done only once.<br>
• This creates isolated browser environments.<br>

## INITIALIZE & LOGIN EACH PROFILE
Run each profile once:<br>
**YouTube (mainYT)**
```bash
  firefox --no-remote -P mainYT https://www.youtube.com
```
• Login to your YouTube account.<br>
• Close Firefox.<br>
	
**YouTube Kids (kidsYT)**
```bash
  firefox --no-remote -P kidsYT https://www.youtubekids.com
```
• Setup / login kids account.<br>
• Close Firefox.<br>
	
**❗IMPORTANT:**<br>
• Profiles must be initialized once.<br>
• Script will reuse login automatically.<br>

## CREATE MAIN PYTHON SCRIPT
```bash
  nano ~/apps/youtube-timer/YouTubeTimerFirefox.py
```
Paste your FINAL working code (*YouTubeTimerFirefox.py*).<br>

Core logic:<br>
- Popup (Tkinter) → select time<br>
- Launch Firefox using selected profile<br>
- Timer countdown<br>
- End Now → terminate browser<br>
- Auto close when time ends<br>

Make executable:
```bash
  chmod +x ~/apps/youtube-timer/YouTubeTimerFirefox.py
```

## CREATE LAUNCHER SCRIPTS (STABILITY LAYER)
**YouTube launcher**
```bash
  nano ~/apps/youtube-timer/launch_youtube_timer.sh
```

Paste:
```bash
  #!/usr/bin/env bash
  cd "$HOME/apps/youtube-timer"
  python3 "$HOME/apps/youtube-timer/YouTubeTimerFirefox.py" youtube
```
**YouTube Kids launcher**
```bash
  nano ~/apps/youtube-timer/launch_youtubekids_timer.sh
```
Paste:
```bash
  #!/usr/bin/env bash
  cd "$HOME/apps/youtube-timer"
  python3 "$HOME/apps/youtube-timer/YouTubeTimerFirefox.py" kids
```
Make executable:<br>
```bash
  chmod +x ~/apps/youtube-timer/*.sh
```
## CREATE APPLICATION LAUNCHERS (SYSTEM APPS)
```bash
  mkdir -p ~/.local/share/applications
```	
**YouTube app**
```bash
  nano ~/.local/share/applications/youtube-timer.desktop
```
Paste:
```bash
  [Desktop Entry]
  Version=1.0
  Type=Application
  Name=YouTube Timer
  Exec=/home/yudhi/apps/youtube-timer/launch_youtube_timer.sh
  Icon=/home/yudhi/apps/youtube-timer/icons/youtube.png
  Terminal=false
  Categories=Utility;
```
**YouTube Kids app**
```bash
  nano ~/.local/share/applications/youtubekids-timer.desktop
```
Paste:
```bash
  [Desktop Entry]
  Version=1.0
  Type=Application
  Name=YouTube Kids Timer
  Exec=/home/yudhi/apps/youtube-timer/launch_youtubekids_timer.sh
  Icon=/home/yudhi/apps/youtube-timer/icons/youtubekids.png
  Terminal=false
  Categories=Utility;
```
Activate:
```bash
  chmod +x ~/.local/share/applications/*.desktop
  update-desktop-database ~/.local/share/applications 2>/dev/null
```

## CREATE CUSTOM ICONS (LOCAL)
```bash
  mkdir -p ~/apps/youtube-timer/icons
  cd ~/apps/youtube-timer/icons
```
**YouTube icon (Y)**
```bash
  convert -size 256x256 xc:red
  -gravity center
  -pointsize 140
  -fill white
  -font DejaVu-Sans-Bold
  -annotate 0 "Y" youtube.png
```
**YouTube Kids icon (Yt)**
```bash
  convert -size 256x256 xc:#ff4444
  -gravity center
  -pointsize 110
  -fill white
  -font DejaVu-Sans-Bold
  -annotate 0 "Yt" youtubekids.png
```
## ADD TO DASH (RECOMMENDED USAGE)
Press Super key → search:<br>
	• YouTube Timer<br>
	• YouTube Kids Timer<br>
	Right-click → Add to Favorites<br>
**❗IMPORTANT:**<br>
	• Use Dash (left dock)<br>
	• Avoid Desktop shortcuts (less stable)<br>

## FINAL USAGE FLOW
Click app → popup appears<br>
Select:<br>
• 5 min<br>
• 10 min<br>
• 15 min<br>
• 25 min<br>
Then:<br>
• Firefox opens (correct profile)<br>
• Timer runs<br>
• End Now → closes browser<br>
Timer ends → auto close<br>
