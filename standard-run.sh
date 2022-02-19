#!/bin/bash

DATE=$(date +"%Y-%m-%d")
DAY=$(date +"%a")

if grep $DATE /home/nouser/Desktop/scripts/twitter/twitter_bot/db.txt; then
    clear
    exit
fi
echo "[x] Running the bash Twitter script..."
echo "[x] Please wait..."
echo $DATE >> /home/nouser/Desktop/scripts/twitter/twitter_bot/db.txt
case $DAY in
    Mon|Wed|Fri)
	echo "[x] Clearing and fishing..."
	python /home/nouser/Desktop/scripts/twitter/twitter_bot/UI.py -o 1
	python /home/nouser/Desktop/scripts/twitter/twitter_bot/UI.py -o 2;;
    Tue|Thu|Sat)
	echo "[x] Clearing and fishing..."
	python /home/nouser/Desktop/scripts/twitter/twitter_bot/UI.py -o 1
	python /home/nouser/Desktop/scripts/twitter/twitter_bot/UI.py -o 1;;
    *) 
        python /home/nouser/Desktop/scripts/twitter/twitter_bot/UI.py -o 1;;
esac

