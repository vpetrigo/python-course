#!/usr/bin/env python3
# coding=utf-8

import sys
import re

def find_slash(string):
    pattern = r"\\"
    return re.search(pattern, string)

def main():
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        if find_slash(line):
            print(line)

if __name__ == "__main__":
    main()
