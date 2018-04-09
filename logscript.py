#!/usr/bin/env python
########
# Logwatcher with webhook function by Tyler Conrad, conrad@arista.com
# based on work by Richard, https://eos.arista.com/syslog-triggered-event-scripts/
# Usage -
# event-handler LOGWATCHER
#   trigger on-boot
#   action bash ip netns exec ns-MGMT python /mnt/flash/logscript.py
#   delay 60
# Requirements:
#  Needs DNS to resolve webhook destination endpoint
#  Needs tcp reachability to destination endpoint IP
#  Can be run from VRF or global table. example above uses VRF change to syntax below to run from global:
#  action bash python /mnt/flash/logscript.py
########

import re, time, sys, Logging
from os import stat
from os.path import abspath
from stat import ST_SIZE
import webhookfunction
import socket

#Enter your webhook URL here.
webhook_url = ''
username = socket.gethostname()
text = ''

# What log file to watch
file = "/var/log/messages"

# What expression in the log to match on - needs work.
expression = '(.*RIB:.*|.*OSPF:.*|.*BGP:.*)'

# Define Log
Logging.logD( id="ANY_EVENT",
              severity=Logging.logInfo,
              format="%s",
              explanation="Message to indicate that the any-event script has caught an event",
              recommendedAction=Logging.NO_ACTION_REQUIRED
)

class LogTail:
    def __init__(self, logfile, expression):
        self.expression = expression
        self.logfile = abspath(logfile)
        self.f = open(self.logfile,"r")
        file_len = stat(self.logfile)[ST_SIZE]
        self.f.seek(file_len)
        self.pos = self.f.tell()
    def _reset(self):
        self.f.close()
        self.f = open(self.logfile, "r")
        self.pos = self.f.tell()

# Look for new entries in the log file

    def tail(self):
        while 1:
            self.pos = self.f.tell()
            line = self.f.readline()
            if not line:
                if stat(self.logfile)[ST_SIZE] < self.pos:
                    self._reset()
                else:
                    time.sleep(1)
                    self.f.seek(self.pos)
            else:

# Look for a matching line
                if re.match(self.expression, line, re.M|re.I):
                  text = line
                  response = webhookfunction.webhook(webhook_url, username, text)

# Run this thing
tail = LogTail(file, expression)
tail.tail()
