"""
pydiceroller init
"""

from random import random
from colorama import Back
from columnar import columnar
from columnar import exceptions
from click import style
from pydiceroller.args import compute_args
import os
import copy
import random
import time
import subprocess
from shutil import which
import re
from termcolor import colored
import colorama

DICE_EMOJI = "\U0001f3b2"

def pydiceroller():
    """
    pydiceroller entry point
    """
    #fix potential windows bug
    colorama.init()
    os.sys.stdin.reconfigure(encoding='utf-8')
    os.sys.stdout.reconfigure(encoding='utf-8')
    if compute_args().update:
        update()
        exit()
    if not compute_args().dices:
        print("no dice given")    
        exit(1)

    for dice in compute_args().dices:
        if not re.match("^[1-9][0-9]*d[1-9][0-9]*$",dice.lower() ) and not re.match("^d?[1-9][0-9]*$",dice.lower() ) and not re.match("^s[1-9][0-9]*d[1-9][0-9]*$",dice.lower() ):
            print("bad param") 
            exit(1)

    for dice in compute_args().dices:
        if re.match("^[1-9][0-9]*d[1-9][0-9]*$",dice.lower() ):
            number=dice.lower().split('d')[0]
            diceone=dice.lower().split('d')[1]
            for r in range(int(number)):
                print(((DICE_EMOJI + diceone + " : ") if not compute_args().silent else "") + str(random.randint(1, int(diceone))))
        elif re.match("^d[1-9][0-9]*$",dice.lower() ):
            number=1
            diceone=dice[1:]
            for r in range(int(number)):
                print(((DICE_EMOJI + diceone + " : ") if not compute_args().silent else "") + str(random.randint(1, int(diceone))))              
        elif re.match("^[1-9][0-9]*$",dice.lower() ):
            number=1
            diceone=dice
            for r in range(int(number)):
                print(((DICE_EMOJI + diceone + " : ") if not compute_args().silent else "") + str(random.randint(1, int(diceone))))              

        elif re.match("^s[1-9][0-9]*d[1-9][0-9]*$",dice.lower() ):
            number=dice[1:].lower().split('d')[0]
            diceone=dice[1:].lower().split('d')[1]
            result=0
            for r in range(int(number)):
                result=result+random.randint(1, int(diceone))
            print(((number + DICE_EMOJI + diceone + " : ") if not compute_args().silent else "")  + str(result))                  
def update():
    """
    entry point for --update
    """
    prog = "pip3"
    if (which("pip3")) is None:
        prog = "pip"
    params = [
        prog,
        "install",
        "--upgrade",
        "pydiceroller",
    ]
    subprocess.check_call(params)

def printwarning(txt):
    print(colored(txt,"yellow"))    