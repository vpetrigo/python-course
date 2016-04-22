#!/usr/bin/env python3
# coding=utf-8

import shutil
import os

def main():
    ARCH_FILE = "main.zip"
    shutil.unpack_archive(ARCH_FILE)
    DIRNAME = ARCH_FILE.split(".")[0]

    dir_with_py = []
    for (dirpath, dirname, filenames) in os.walk(DIRNAME):
        for i in filenames:
            # if we have even one *.py file add the name of a directory
            # to the dir_with_py list and go into the next directory
            if i.lower().endswith(".py"):
                dir_with_py.append(dirpath)
                break

    with open("dir_output.txt", "w") as dout:
        for item in sorted(dir_with_py):
            print(item, file=dout)

if __name__ == "__main__":
    main()
