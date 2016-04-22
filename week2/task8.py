#!/usr/bin/env python3
# coding=utf-8

def main():
    lines = []
    with open("dataset_24465_4.txt", "r") as inp:
        lines = [line for line in inp]

    with open("output.txt", "w") as out:
        out.writelines(reversed(lines))

if __name__ == "__main__":
    main()
