#!/usr/bin/env python3
# coding=utf-8

import sys

class Impossible(Exception):
    pass

def count_ops(origin_str, s_from, s_to):
    if s_from not in origin_str:
        return 0
   
    if s_from in s_to:
        raise Impossible("Impossible")

    op_counter = 0 
    while s_from in origin_str:
        origin_str = origin_str.replace(s_from, s_to)
        op_counter += 1

    return op_counter

def main():
    reader = (line.rstrip() for line in sys.stdin)
    origin, s_from, s_to = list(reader)
    
    try:
        result = count_ops(origin, s_from, s_to)
        print(result)
    except Impossible as imp:
        print(imp)

if __name__ == "__main__":
    main()
