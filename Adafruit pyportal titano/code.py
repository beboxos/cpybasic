try:
    i2c.deinit()
except:
    pass

"""This class implements a BASIC interpreter that
presents a prompt to the user. The user may input
program statements, list them and run the program.
The program may also be saved to disk and loaded
again.
orginal port : https://github.com/richpl/PyBasic

Modified by BeBoX. 2021 for Adafruit titano
"""

from basictoken import BASICToken as Token
from lexer import Lexer
from program import Program
from sys import stderr

#addon BeBoX 09.10.2021 special version for Adafruit Pyportal
i2ckeyboard=True

import os, microcontroller
import busio, board
i2c = busio.I2C(board.SCL, board.SDA)
while not i2c.try_lock():
    pass
cardkb = i2c.scan()[0]  # should return 95
if cardkb != 95:
    print("!!! Check I2C config: " + str(i2c))
    print("!!! CardKB not found. I2C device", cardkb,
          "found instead.")
    exit(1)
 
ESC = chr(27)
NUL = '\x00'
CR = "\r"
LF = "\n"

buffer=[]
bufidx=0

b = bytearray(1)


def ReadKey():
    c = ''
    i2c.readfrom_into(cardkb, b)    
    try:
        c = b.decode()
    except:
        c = b
           
    if c == CR:
        # convert CR return key to LF
        c = LF
    return c

def InputFromKB(prompt):
    global bufidx
    global buffer
    key=''
    keyRead=''
    datainput=''
    print(prompt, end='')
    while key!="\n":
            key=ReadKey()
            #key = keyRead[0]    
            #key = key[1]
            if key!=NUL:
                if key!="\n":
                    if key==b'\xb5':
                        #key up
                        if len(buffer)!=0:
                            if bufidx>0:
                                bufidx=bufidx-1
                            else:
                                bufidx=0
                            tmp=len(datainput)
                            datainput=buffer[bufidx]
                            print(chr(27)+"[2K", end="")
                            print(chr(27)+"["+str(tmp)+"D", end="")
                            print(" "*20, end="")
                            print(chr(27)+"[2K", end="")
                            print(chr(27)+"[20D", end="")                            
                            print(datainput, end="")
                    elif key==b'\xb6':
                        #key down
                        if len(buffer)!=0:
                            if bufidx<len(buffer)-1:
                                bufidx=bufidx+1
                            else:
                                bufidx=len(buffer)-1
                            tmp=len(datainput)
                            datainput=buffer[bufidx]
                            print(chr(27)+"[2K", end="")
                            print(chr(27)+"["+str(tmp)+"D", end="")
                            print(" "*20, end="")
                            print(chr(27)+"[2K", end="")
                            print(chr(27)+"[20D", end="")                            
                            print(datainput, end="")
                    elif key == b'\xb7':
                        #right
                        pass
                    elif key == b'\xb4':
                        #left
                        pass
                    else:                            
                        print(key, end='')
                        if key!='\x08':
                            datainput+=key
                        else:
                            datainput=datainput[:-1]
                            #print(key, end="")
                            print(" ", end="")
                            print(key, end="")
    
    buffer.append(datainput)
    bufidx = len(buffer)
    print()
    return datainput

#---------------------------------------------------

def main():

    banner = (
    """
  ___  _                 _  _    _ __  _  _  _    _               
 / __|(_) _ _  __  _  _ (_)| |_ | '_ \| || || |_ | |_   ___  _ _  
| (__ | || '_|/ _|| || || ||  _|| .__/ \_. ||  _||   \ / _ \| ' \ 
 \___||_||_|  \__| \_._||_| \__||_|    |__/  \__||_||_|\___/|_||_|
         ___  _  _  ___            _                  
        | _ \| || || _ ) __ _  ___(_) __              
        |  _/ \_. || _ \/ _` |(_-/| |/ _|        _    
        |_|   |__/ |___/\__/_|/__/|_|\__|       (_)   
_________________________________________________________________ 
\____\____\____\____\____\____\____\____\____\____\____\____\____\ 
                                                                  
""")
    for n in range(20):
        print()
    print(banner)
    print("        Adafruit PyPortal Titano Edition by BeBoX (c)2021\r\n")
    lexer = Lexer()
    program = Program()
    
    # check if system is Read only
    RO=False
    
    
    # Continuously accept user input and act on it until
    # the user enters 'EXIT'
    while True:
        if i2ckeyboard==True:
            stmt = InputFromKB(chr(187)+' ')
        else:
            stmt = input(chr(187)+' ')
        #if no i2c keyboard take input from PC

        try:
            tokenlist = lexer.tokenize(stmt)

            # Execute commands directly, otherwise
            # add program statements to the stored
            # BASIC program

            if len(tokenlist) > 0:

                # Exit the interpreter
                if tokenlist[0].category == Token.EXIT:
                    break

                # Add a new program statement, beginning
                # a line number
                elif tokenlist[0].category == Token.UNSIGNEDINT\
                     and len(tokenlist) > 1:
                    program.add_stmt(tokenlist)

                # Delete a statement from the program
                elif tokenlist[0].category == Token.UNSIGNEDINT \
                        and len(tokenlist) == 1:
                    program.delete_statement(int(tokenlist[0].lexeme))

                # Execute the program
                elif tokenlist[0].category == Token.RUN:
                    try:
                        program.execute()

                    except KeyboardInterrupt:
                        print("Program terminated")

                # List the program
                elif tokenlist[0].category == Token.LIST:
                     if len(tokenlist) == 2:
                         program.list(int(tokenlist[1].lexeme),int(tokenlist[1].lexeme))
                     elif len(tokenlist) == 3:
                         # if we have 3 tokens, it might be LIST x y for a range
                         # or LIST -y or list x- for a start to y, or x to end
                         if tokenlist[1].lexeme == "-":
                             program.list(None, int(tokenlist[2].lexeme))
                         elif tokenlist[2].lexeme == "-":
                             program.list(int(tokenlist[1].lexeme), None)
                         else:
                             program.list(int(tokenlist[1].lexeme),int(tokenlist[2].lexeme))
                     elif len(tokenlist) == 4:
                         # if we have 4, assume LIST x-y or some other
                         # delimiter for a range
                         program.list(int(tokenlist[1].lexeme),int(tokenlist[3].lexeme))
                     else:
                         program.list()

                # Save the program to disk
                elif tokenlist[0].category == Token.SAVE:
                    program.save(tokenlist[1].lexeme)
                    print("Program written to file")

                # Load the program from disk
                elif tokenlist[0].category == Token.LOAD:
                    program.load(tokenlist[1].lexeme)
                    print("Program read from file")

                # Delete the program from memory
                elif tokenlist[0].category == Token.NEW:
                    program.delete()
                    
                elif tokenlist[0].category == Token.DIR:
                    print("directory of ",end="")
                    path="/"                    
                    try:
                        path+=tokenlist[1].lexeme
                    except:
                        pass
                    files=os.listdir(path)
                    print(path + " *.bas")
                    count=0
                    for n in files:
                        if n[-4:]==".bas":
                            count+=1
                            print(n)
                    print("Found " + str(count) + " files.")
                    

                # Unrecognised input
                else:
                    print("Unrecognised input", file=stderr)


        # Trap all exceptions so that interpreter
        # keeps running
        except Exception as e:
            print("Error : ", end="")
            print(e, file=stderr, flush=False)
            


if __name__ == "__main__":
    main()