#!/usr/bin/env python3
# coding=utf-8

import sys
import re

def main():
    pattern = r"^(1(01*0)*1|0)+$"
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        if re.match(pattern, line):
            print(line)

if __name__ == "__main__":
    main()
