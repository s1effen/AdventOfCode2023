import workspace
import helper
from importlib import import_module

def run(day, test=False):
   run = getattr(import_module("day{:02d}.day{:02d}".format(day,day)), "run")
   run("{:02d}".format(day),test)

run(1,test=False)