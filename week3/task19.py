#!/usr/bin/env python3
# coding=utf-8

import sys
import xml.etree.ElementTree as ET

def traverse_tree(xml_tree, cost_dict, cost=2):
    for child in xml_tree:
        cost_dict[child.attrib["color"]] += cost
        traverse_tree(child, cost_dict, cost + 1)

def main():
    cubics_cost = dict(red=0, blue=0, green=0)
    reader = (line.rstrip() for line in sys.stdin)
    xml_data = next(reader)
    root = ET.fromstring(xml_data)

    cubics_cost[root.attrib["color"]] += 1
    # traverse through the whole tree
    traverse_tree(root, cubics_cost)

    print("{0[red]} {0[green]} {0[blue]}".format(cubics_cost))


if __name__ == "__main__":
    main()
