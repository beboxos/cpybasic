# cPyBasic
## Circuitpython version of PyBasic for microcontrollers
![img](https://github.com/beboxos/circuitpython/blob/main/images/pybasic1.jpeg)

Current version work only for Adafruit titano & CardKB for now.
The [origninal PyBasic](https://github.com/richpl/PyBasic) was designed to work on "Normal Python".
But microcontrollers avec spécific things like neopixels, touchscreens etc.

The current version is made and developped around the [Adafruit PyPortal Titano](https://learn.adafruit.com/adafruit-pyportal-titano).
Why ? 
Because I have it and because this device is enough complete : network, touchscreen, 480x320 color lcd, sound, light sensor, microSD 
if a [m5stack i2c CardKB](https://shop.m5stack.com/products/cardkb-mini-keyboard) is attached to the Pyportal titano, it will be used 
for input keystroke and that make the device fully usable "On the Road". If there is no keyboard attached, input come from computer
over REPL serial interface.
![img](https://github.com/beboxos/circuitpython/blob/main/images/pybasic2.jpeg)

Later, will be ported to other devices like WIO terminal, regular PyPortal etc... 

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
 - GSCREEN "on" / GSCREEN "OFF" : show or hide graphic screen 
 - GCLS [color] : clear graphic screen , with optional color or black if blank
 - GLINE x,y,x2,y2,color : draw a line from x,y to x1,y1
 - GRECT x,y,width,height,fill color,outline color, outline width: draw a rectangle shape. use none for transparent color
 - GRRECT x,y,width,height,radius, fill color,outline color, ouline width: draw a round rectangle shape use none for transparent color
 - GTRIANGLE x0,y0,x1,y1,x2,y2,fill color, outline color : draw a triangle shape, use none for transparent color
 - GPRINT x,y,"TEXT"[,size,color,bgcolor] : print a text at x,y optional multiplier size, font color, background color
 - GCIRCLE x,y,radius,fill color, outline color, outline width : draw a circle shape at x,y 

BEEP & PLAY are experimental and buggy for now

- todo list : 
- fix all bugs :) 
- SD card support
- graphics image load , sprites ?
- network support
- and all we can imagine 

Change Log:
- 19.10.2021 : new functions PRINTAT, CLS 
- 21.10.2021 : m5stack CardKB management improvement (keystroke history by pressing up/down + inline editing by using left/right key)
- 22.10.2021 : WAV function let you play a wave sound file
- 24.10.2021 : Graphic news feature , gscreen, gcls, gline, grect, gtriangle,gprint ...
- 24.10.2021 : fixed val() function to match Circuitpython. added example.bas to help you manage all new functions
