from _inquirer import inquirer as inquirer
from _colorama import Fore, Style
from getpass import getpass
import time
import math
import time
import threading
import os
import sys
import tty
import termios
from _blessed import Terminal


def chooseList(question: str, choices) -> str:
    return inquirer.prompt([
        inquirer.List('',
                      message=question,
                      choices=choices,
                      carousel=True)
    ])[""]


def progressBar(label: str, stat: int, max: int, color_inner,):
    """
    label: the label of the statistic
    stat: The current value of the statistic being measured (e.g. Health).
    max: maximum value of that statistic
    color_inner: the internal color of the progressBar
    """

    percentage = stat/max
    bars = math.ceil(percentage * 20)
    print(
        # To make progress bars align
        label + (" " * (10 - len(label)) +
                 Style.RESET_ALL + "[" +
                 color_inner + ("|" * bars) +
                 Fore.BLACK + ("|" * (20 - bars)) +
                 Fore.WHITE + "] "
                 + Fore.BLUE +
                 str(int(stat)) + "/" + str(max)
                 ))


def say(*args):
    print(*args)
    time.sleep(0.5)

# Narrate


def narr(*args):
    print(Fore.GREEN + Style.BRIGHT + "~" +
          Style.RESET_ALL, *args, end="", flush=True)
    # Continue text on enter
    getpass("")

# Ask a question


def ask(question) -> str:
    answer = input(f"[{Fore.YELLOW}?{Style.RESET_ALL}] {question}: ")
    if bool(answer.strip()) == False:
        return ask(question)
    return answer

#Creature dialogue
def dialogue(name, *args, waitForInput=True):
    print(f"{Fore.CYAN}{name}> {Style.RESET_ALL}", *args, end="", flush=True)
    if waitForInput:
        getpass("")

term = Terminal()

def getcolor(position):
  global term
  if position >= 0 and position < 10:
    return term.red
  elif position >= 10 and position < 20:
    return term.gold
  elif position >= 20 and position < 25:
    return term.green
  elif position == 25:
    return term.blue
  elif position > 25 and position <= 30:
    return term.green
  elif position > 30 and position <= 40:
    return term.gold
  else:
    return term.red


def movebar(timeout, position):
  global term
  #Amongus
  sys.stderr.write(term.move_down(3)+term.move_up()+"█"+term.move_up()+term.move_left()+"█"+term.move_up()+term.move_left()+"█")
  sys.stderr.flush()
  v = term.inkey(timeout=timeout)
  if v == "\n":
    return True
  sys.stderr.write(term.move_left()+term.move_down(3)+term.move_up()+getcolor(position)+"█"+term.move_up()+term.move_left()+"█"+term.move_up()+term.move_left()+"█" + term.normal)
  sys.stderr.flush()
  return False

def slider(interval):
  global term

  print("".join([getcolor(x) + "█"  for x in range(51)]))
  print("".join([getcolor(x) + "█"  for x in range(51)]))
  print("".join([getcolor(x) + "█"  for x in range(51)]))

  accuracy = 26
  pos = 0
  
  with term.location():
    with term.cbreak():
      with term.hidden_cursor():
        for i in range(50): 
          if movebar(interval, i):
            pos = i
            accuracy = abs(i-25)
            break
  term.move_down(4)
  print(term.normal)

  increaser = 0
  if getcolor(pos) == term.red:
    increaser = 0.1
  elif getcolor(pos) == term.gold:
    increaser = 0.5
  elif getcolor(pos) == term.green:
    increaser = 1
  else:
    increaser = 3
    
  multiplier = max((26 - accuracy) * increaser, 0)/5
  return multiplier

def clear():
  global term
  print(term.clear)