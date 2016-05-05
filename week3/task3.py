#!/usr/bin/env python3
# coding=utf-8

import re
import sys

def find_substr(string, pattern):
    res = re.findall(pattern, string)

    return res

def main():
    pattern = r'cat'
    reader = (line.rstrip() for line in sys.stdin)

    for line in reader:
        r = find_substr(line, pattern)

        if len(r) >= 2:
            print(line)


if __name__ == "__main__":
    main()
