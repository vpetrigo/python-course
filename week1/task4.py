#!/usr/bin/env python3

import sys

namespaces = {"global": ["global"]}
namespace_vars = {"global": list()}

def add_value(namespace, val):
  if namespace not in namespace_vars:
    namespace_vars[namespace] = list()
  
  namespace_vars[namespace].append(val)
   
def create_namespace(namespace, parent):
    namespaces[namespace] = namespaces[parent] + [namespace]
    namespace_vars[namespace] = list()

def get_value(namespace, val):
  for ns in reversed(namespaces[namespace]):
      if val in namespace_vars[ns]:
        return ns
  else:
    return None

def main():
  n = int(sys.stdin.buffer.readline())
  reader = (tuple(map(str, line.split())) for line in sys.stdin)
  commands = list(reader)
  for command, *args in commands:
    if command == "add":
      add_value(*args)
    elif command == "get":
      print(get_value(*args))
    elif command == "create":
      create_namespace(*args)
    else:
      raise Exception("error")
      
if __name__ == '__main__':
  main()