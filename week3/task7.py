#!/usr/bin/env python3
# coding=utf-8

import sys
import re

def find_tand_repeat(string):
    pattern = r"(\b\w+?)\1\b"

    return re.search(pattern, string)

def main():
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        if find_tand_repeat(line):
            print(line)

if __name__ == "__main__":
    main()
