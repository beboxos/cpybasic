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

New commands added : 

 - DIR : in main window list .bas files can't be used in programs
 - NEOPIXEL : usage NEOPIXEL R G B (values 0 - 255)
 - LIGHT : return value of light sensor
 - PAUSE : make a pose in sec ex. PAUSE 0.5 for 30 seconds
 - GETTTOUCH : wait for touch screen press and return coords x,y in string ex: 10 LET A$=GETTOUCH
 - TOUCHX : non blocking, return x coord of touch screen -1 if no value
 - TOUCHY : non blocking, return y coord of touch screen -1 if no value
 - CLS : Clear screen #reworked 19.10.2021
 - BEEP : beep a sound BEEP Feq_in_hz Duration_in_Sec ex: BEEP 440 1 => 440 Hz for 1 sec
 - PLAY : make a note ex. 10 PLAY C#2 1, play do # 2nd octave during 1 sec
 - PRINTAT : print a string at coordinate ex: 10 PRINTAT 5 10 "Hello World" #add on 19.10.2021
 - WAV : play a wav file usage WAVE "filename"

BEEP & PLAY are experimental and buggy for now

- todo list : 
- fix all bugs :) 
- Play Wav files from disk (in progress)
- SD card support
- graphics 
- network support
- and all we can imagine 

Change Log:
19.10.2021 : new functions PRINTAT, CLS 
21.10.2021 : m5stack CardKB management improvement (keystroke history by pressing up/down + inline editing by using left/right key)
22.10.2021 : WAV function let you play a wave sound file
