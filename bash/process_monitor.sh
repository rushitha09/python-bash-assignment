#!/bin/bash

PROCESS="notepad.exe"
LOGFILE="logs/process.log"

mkdir -p logs

DATE=$(date "+%Y-%m-%d %H:%M:%S")

if tasklist.exe | grep -i "$PROCESS" > /dev/null
then
    echo "$DATE : $PROCESS is running." >> "$LOGFILE"
    echo "$PROCESS is already running."
else
    echo "$DATE : $PROCESS is NOT running." >> "$LOGFILE"

    echo "Starting $PROCESS..."

    cmd.exe /c start notepad

    sleep 2

    if tasklist.exe | grep -i "$PROCESS" > /dev/null
    then
        echo "$DATE : $PROCESS started successfully." >> "$LOGFILE"
        echo "Restart successful."
    else
        echo "$DATE : Failed to start $PROCESS." >> "$LOGFILE"
        echo "Restart failed."
    fi
fi