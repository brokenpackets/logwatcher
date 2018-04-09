# logwatcher
Simple script to watch Arista switch logs and send an outgoing webhook when a line matches against configured regex.
 Usage -
```
event-handler LOGWATCHER
 trigger on-boot
   action bash ip netns exec ns-MGMT python /mnt/flash/logscript.py
   delay 60
```
Requirements:
  Needs DNS to resolve webhook destination endpoint
  Needs tcp reachability to destination endpoint IP
  Can be run from VRF or global table. example above uses VRF change to syntax below to run from global:
```
action bash python /mnt/flash/logscript.py
```

