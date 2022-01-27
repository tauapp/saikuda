import inquirer
from colorama import Fore
import time
from inquirer.themes import GreenPassion

def chooseList(question: str, choices) -> str:
  return inquirer.prompt([
    inquirer.List('',
    message = question,
    choices = choices,
    carousel = True)
  ], theme=GreenPassion())[""]

def progressBar(label: str, stat: int, max: int, color_inner, color_outer, color_contrast):
  """
  label: the label of the statistic
  stat: The current value of the statistic being measured (e.g. Health).
  max: maximum value of that statistic
  color_inner: the internal color of the progressBar
  color_outer: The color of the outside of the bar
  color_contrast: The color used to represent bars not being filled
  """

  percentage = stat/max
  bars = round(percentage * 20)
  print(
    #To make progress bars align
    label + (" " * (10 - len(label)) + 
    color_outer + "[" +
    color_inner + ("|" * bars) +
    color_contrast + ("|" * (20 - bars)) +
    color_outer + "] "
    + Fore.BLUE +
    str(stat) + "/" + str(max)
  ))

def say(*args):
  print(*args)
  time.sleep(0.5)