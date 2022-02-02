import _inquirer as inquirer
from colorama import Fore
import time
import math

def chooseList(question: str, choices) -> str:
  return inquirer.prompt([
    inquirer.List('',
    message = question,
    choices = choices,
    carousel = True)
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
    #To make progress bars align
    label + (" " * (10 - len(label)) + 
    Fore.WHITE + "[" +
    color_inner + ("|" * bars) +
    Fore.BLACK + ("|" * (20 - bars)) +
    Fore.WHITE + "] "
    + Fore.BLUE +
    str(stat) + "/" + str(max)
  ))

def say(*args):
  print(*args)
  time.sleep(0.5)

#Narrate
def narr(*args):
  print(*args)
  letters = len(" ".join(args))
  time.sleep(letters/25)
