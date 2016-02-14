# kfs_lds
Raspberry pi based video streaming

#Necessary software
- Mplayer
- netcat

#Usage
1. Change stream_cam.py target ip to target computer
2. Open port 8889 port with netcat (netcat -l -p 8889)
3. Start script receive_cam.sh on target computer
4. Start stream_cam.py on source raspberry pi
-> Mplayer should pop up
