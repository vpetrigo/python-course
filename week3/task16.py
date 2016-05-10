#!/usr/bin/env python3
# coding=utf-8

import json
import sys
import collections

def dfs_inc_parent_counter(tree, from_n, to_n, class_counter, path=None):
  if not path:
      path = []

  class_counter[from_n] += 1
  path.append(from_n)

  if from_n not in tree:
    return None
  if from_n == to_n:
    return path

  for node in tree[from_n]:
    if node not in path:
      newpath = dfs_inc_parent_counter(tree, node, to_n, class_counter, path)

      if newpath:
        return newpath

  return None

def main():
  reader = (line.rstrip() for line in sys.stdin)
  classes_inh_count = collections.defaultdict(lambda: 0)
  # read json input
  data = next(reader)
  # parse it to the dictionary
  classes_relations = {_class["name"] : _class["parents"] for _class in json.loads(data)}

  for cl in classes_relations:
      dfs_inc_parent_counter(classes_relations, cl, None, classes_inh_count)

  for k in sorted(classes_inh_count):
      print("{} : {}".format(k, classes_inh_count[k]))

if __name__ == "__main__":
  main()
