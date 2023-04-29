## An RPI-CM4 based pocket development server

I don't want to wear a lot of gear when I'm out and about, but I do want to be able to do some development work. This is a small, portable, battery powered, RPI-CM4 based development server. It's designed to be used with a phone or tablet as a display and keyboard.

I use [Piunora](https://www.diodes-delight.com/products/piunora/) as a main board and CM4 with WiFi and 8Gb of RAM. Storage is 240Gb Toshiba RC100 NVMe SSD.
Battery is 2000mAh LiIon. I use a 3D printed case to hold everything together.
To charge the battery I use a [chinese module](https://www.aliexpress.com/item/1005004616088520.html) with unknown chip.

Battery connected to MCP3008 ADC via voltage divider to measure voltage. When battery runs low, the LED will blink red every 15 seconds.


