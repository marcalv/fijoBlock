# fijoBlock
This is a small Python Selenium project that blocks or unblocks incoming calls via a home router web server. This web server already has a feature to enable or disable incoming calls based on an schedule table but it is not working, so I'm replicating the same functionality externally.

This python script is running on a Raspberry Pi 3 on buster.

## Dependencies
```
sudo apt install git chromium-browser chromium-chromedriver xvfb python3 python3-pip
pip3 install pipenv 
```
## Installation
Clone from repo, install dependencies with pipenv, create config.py and customize it.
```
cd /home/pi
git clone https://github.com/marcalv/fijoBlock
cd fijoBlock
pipenv install
cp config_template.py config.py
nano config.py
```
## Single run
```
pipenv run python -u /home/pi/fijoBlock/fijoBlock.py unblock
pipenv run python -u /home/pi/fijoBlock/fijoBlock.py block
```
## Cron Jobs
Example cron jobs:
```
# Execute block and unblock commands logging std & err to fb.log, wich is monthly deleted.
30 17 * * * PATH_TO_VIRUALENV/bin/python -u /home/pi/fijoBlock/fijoBlock.py unblock >> /home/pi/fijoBlock/log.log 2>&1 &
50 23 * * * PATH_TO_VIRUALENV/bin/python -u /home/pi/fijoBlock/fijoBlock.py block >> /home/pi/fijoBlock/log.log 2>&1 &
00 3 1 * * rm /home/pi/fijoBlock/log.log
```
Replace `PATH_TO_VIRUALENV` with virtualenv path. You can find it with the following command:
```
pipenv --venv
```
