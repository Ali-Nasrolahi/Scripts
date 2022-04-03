#!/usr/bin/python3.9

'''
This script is designed to format hpp and cpp files which
present in src and include directories.

Formating is done by clang-foramt with file args. So .clang-foramt file
must be present in project folder or its parants.

Give the script only project folder.

Output files associated with include and src subfolder called OUTPUTDIR.

DO NOT RUN THIS SCRIPT TWICE, or
WHEN OUTPUTDIR IS PRESENT.
'''

import subprocess  # to run clang-format
import time  # to sleep
import os  # to change directory
import glob  # to find all *.hpp and *.cpp files
import sys  # To get input from command line

OUTPUTDIR = "CLANG-CLEAN-OUT"


def FormatIt(name):
    Input = name + ".clangout"
    Output = name

    # This command will format the code by clang-format-- .clang-format must exist.
    p = subprocess.Popen(
        f"clang-format -style=file {name} > " + OUTPUTDIR + "/" + Input, stdout=subprocess.PIPE, shell=True)

    # This sleep added to give clang-format sometime to do his job.
    time.sleep(0.1)

    os.chdir(OUTPUTDIR)
    f1 = open(Input, "r")
    f2 = open(Output, "w")
    os.chdir("..")

# Removing whitespaces from right of each line
    s = ""
    for l in f1:
        s = l.replace("\n", "").rstrip()
        print(s, file=f2, flush=True)


if __name__ == "__main__":
    # project path
    path = sys.argv[1]

    os.chdir(path)

    # checking for hpp
    os.chdir("include")
    os.mkdir(OUTPUTDIR)

    for name in glob.glob("*.hpp"):
        FormatIt(name)

    # checking for cpp
    os.chdir("../src")
    os.mkdir(OUTPUTDIR)

    for name in glob.glob("*.cpp"):
        FormatIt(name)
