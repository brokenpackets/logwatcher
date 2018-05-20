# logwatcher
Simple script to watch Arista switch logs and send an outgoing webhook when a line matches against configured regex.
Updated 05/20/18 - Two versions out now - newer one uses the built-in event-handler 'on-logging' functionality, the other tails the log file directly. Old version grabs _every_ log message, New version only grabs the first one to be seen per batch (if multiple log files show up at same time, such as during a bgp flap, it will only output the first flap).


-------- New Version  
Usage:  
```
event-handler LOGWATCHER
   action bash ip netns exec ns-MGMT python /mnt/flash/webhook.py
   delay 0
   asynchronous
   !
   trigger on-logging
      regex .* switch-hostname-here .*\: .*\-[0-4]\-
```

Requirements:  
  webhook.py located under /mnt/flash.  
  Updated webhook target URL in /mnt/flash/webhook.py.  
  DNS to resolve webhook destination endpoint IP (if using fqdn).  
  TCP reachability to webhook destination endpoint IP.  
  Can be run from VRF or global table. Example above uses VRF - change to syntax below to run from global:  
```
action bash python /mnt/flash/webhook.py
```
  
-------- Old Version  
Usage:  
```
event-handler LOGWATCHER
 trigger on-boot
   action bash ip netns exec ns-MGMT python /mnt/flash/logscript.py
   delay 60
```
Requirements:  
  Both scripts (logscript.py and webhookfunction.py) should be stored in /mnt/flash/  
  Needs DNS to resolve webhook destination endpoint ip.  
  Needs tcp reachability to destination endpoint ip.  
  Can be run from VRF or global table. example above uses VRF change to syntax below to run from global:
```
action bash python /mnt/flash/logscript.py
```

