"""
Cleaner for removing ._. files created by Mac

Examples
--------
$ python3 cleaner.py /path/to/target
"""
from typing import List
import os
import sys
import time


UNWANTED = ["lib", ".idea", "Archive"]


def remove(unwanted: List[str], target: List[str]):
    """
    Removes unwanted in target in place

    Parameters
    ----------
    unwanted: List[str]
        A list of strings containing the dir to skip
    target: List[str]
        The target list
    """
    for x in unwanted:
        if x in target:
            target.remove(x)

def clean(target: str):
    for root, dirname, files in os.walk(target):
        remove(UNWANTED, dirname)
        for f in files:
            if f.startswith("._"):
                os.remove(os.path.join(root, f))


if __name__ == '__main__':
    print("Cleaning")
    while True:
        clean(sys.argv[1])
        time.sleep(30)