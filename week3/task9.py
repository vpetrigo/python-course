#!/usr/bin/env python3
# coding=utf-8

import sys
import re

def main():
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        print(re.sub(r"\b[Aa]+\b", "argh", line, count=1))

if __name__ == "__main__":
    main()
