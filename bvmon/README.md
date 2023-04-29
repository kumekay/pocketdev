Service tracking battery voltage.

On button press, the battery voltage is measured and displayed with the LED.

When battery runs low, the LED will blink red every 15 seconds.

To install this service:
-  copy the `bvmon.service` to `/etc/systemd/system/`
-  copy the `bvmon.py` to `/opt/bvmon/`
-  run `sudo systemctl enable bvmon.service`.
