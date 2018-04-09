# logwatcher
Simple script to watch Arista switch logs and send an outgoing webhook when a line matches against configured regex.

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

