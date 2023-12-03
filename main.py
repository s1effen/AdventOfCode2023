from importlib import import_module
from datetime import date


def run(day=date.today().day, test=False):
    print("\n######################################################")
    print("#".ljust(24) + "Day {:02d}".format(day) + "#".rjust(24))
    print("######################################################")
    run = getattr(import_module("day{:02d}.day{:02d}".format(day, day)), "run")
    run("{:02d}".format(day), test)

run(test=True)
