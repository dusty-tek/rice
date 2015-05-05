#!/bin/sh
export TOP=`date '+%A %B %d - %R'`
export BOT=`python /home/yuno/bin/np.py`
echo "$TOP;$BOT"
