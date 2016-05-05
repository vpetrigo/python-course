#!/usr/bin/env python3
# coding=utf-8

import sys
import re

def main():
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        print(re.sub(r"(\w)\1+", r"\1", line))

if __name__ == "__main__":
    main()
