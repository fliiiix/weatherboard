Weatherboard
============

This is a copy from https://github.com/andrewgodwin/weatherboard.
Rebuilt as something which runs on the PI with cron.

The crontab looks like this:

```
0 * * * * /home/pi/run.sh
```

And the script used here:

```
cat /home/pi/run.sh
#!/bin/sh

export API_KEY=""
export latitude=""
export longitude=""
export timezone="Europe/Zurich"

rm /home/pi/weather.png || echo "nothing to remove"

python3 /home/pi/weatherboard-cron/server/app.py
python3 /home/pi/clear.py
python3 /home/pi/image.py /home/pi/weather.png
```

Get the software:
```
cd ~
git clone https://github.com/fliiiix/weatherboard.git weatherboard-cron

wget https://raw.githubusercontent.com/pimoroni/inky/master/examples/7color/clear.py
wget https://raw.githubusercontent.com/pimoroni/inky/master/examples/7color/image.py 
```
