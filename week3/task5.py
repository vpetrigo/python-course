#!/usr/bin/env python3
# coding=utf-8

import sys
import re

def find_zz(string):
    pattern = r'z.{3}z'

    return re.search(pattern, string)

def main():
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        if find_zz(line):
            print(line)

if __name__ == "__main__":
    main()
