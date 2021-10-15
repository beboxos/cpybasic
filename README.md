# cPyBasic
## Circuitpython version of PyBasic for microcontrollers
![img](https://github.com/beboxos/circuitpython/blob/main/images/pybasic1.jpeg)

Current version work only for Adafruit titano & CardKB for now.
The [origninal PyBasic](https://github.com/richpl/PyBasic) was designed to work on "Normal Python".
But microcontrollers avec spécific things like neopixels, touchscreens etc.

The current version is made and developped around the[Adafruit PyPortal Titano](https://learn.adafruit.com/adafruit-pyportal-titano).
Why ? 
Because i have it and because this deveice is enough complete : network, touchscreen, 480x320 color lcd, sound, light sensor, microSD 
if a [m5stack i2c CardKB](https://shop.m5stack.com/products/cardkb-mini-keyboard) is attached to the Pyportal titano, it will be used 
for input keystroke and that make the device fully usable "On the Road". If there is no keyboard attached, input comme from computer
over REPL serial interface.
![img](https://github.com/beboxos/circuitpython/blob/main/images/pybasic2.jpeg)

Later, will be ported to other devices like WIO terminal, regular pyportal etc... 
