# BUFFALO Internet router reboot scropt

# Summary

This python script reboots the BUFFALO Internet Router.

Target model : WHR-1166DHP

## Require python library

* requests
* beautifulsoup4

# Execution

```
$ export RT_HOST=192.168.4.3
$ export RT_ADMIN_USER=admin
$ export RT_ADMIN_PASS=hogehoge
$ ./reboot_rt.py 
 2020-08-07 18:12:50,286 - INFO - start
 2020-08-07 18:12:50,424 - INFO - compleate
```