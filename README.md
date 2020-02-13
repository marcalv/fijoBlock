# fijoBlock
This is a small Python Selenium project that blocks or unblocks incoming calls via a home router web server. This web server already has a feature to enable or disable incoming calls based on an schedule table but it is not working, so I'm replicating the same functionality externally.

This python script is running on a Raspberry Pi 3 on buster.

## Dependencies
```
sudo apt install chromium-browser
sudo apt install chromium-chromedriver
sudo apt-get install xvfb
sudo pip3 install PyVirtualDisplay
sudo pip3 install xvfbwrapper 
```
## Installation
```
cd /home/pi
git clone https://github.com/marcalv/fijoBlock
cd fijoBlock
cp config_template.py config.py
nano config.py
```
## Single run
```
python3 -u /home/pi/fijoBlock/fijoBlock.py unblock
python3 -u /home/pi/fijoBlock/fijoBlock.py block
```
## Cron Job
Example cron jobs:
```
# Execute block and unblock commands logging std & err to fb.log, wich is monthly deleted.
30 17 * * * python3 -u /home/pi/fijoBlock/fijoBlock.py unblock >> /home/pi/fijoBlock/fb.log 2>&1 &
50 23 * * * python3 -u /home/pi/fijoBlock/fijoBlock.py block >> /home/pi/fijoBlock/fb.log 2>&1 &
00 3 1 * * rm /home/pi/fijoBlock/fb.log
```
