#!/usr/bin/env python3
# coding=utf-8

import requests
import re
import sys

class NotFound(Exception):
  pass

def check_access(from_url, to_url, url_pattern):
  try:
    resp = search_url(from_url)
    return True if to_url in url_pattern.findall(resp) else False
  except NotFound:
    return False

def search_url(from_url):
  resp = requests.get(from_url)

  if resp.status_code == 404:
    raise NotFound
  
  return resp.text
  
def is_accessible(from_url, to_url):
  pattern = re.compile(r"<a\s.*?\s?href=\"([\w:\/.]+)\">")
  
  try:
    resp = search_url(from_url)
    links = pattern.findall(resp)
    
    for link in links:
      if check_access(link, to_url, pattern):
        return True
    else:
      return False
  except NotFound:
    return False

def test():
  assert is_accessible("https://stepic.org/media/attachments/lesson/24472/sample0.html", 
                       "https://stepic.org/media/attachments/lesson/24472/sample2.html") == True
  
  assert is_accessible("https://stepic.org/media/attachments/lesson/24472/sample0.html",
                       "https://stepic.org/media/attachments/lesson/24472/sample1.html") == False
  
  assert is_accessible("https://stepic.org/media/attachments/lesson/24472/sample1.html", 
                       "https://stepic.org/media/attachments/lesson/24472/sample2.html") == True

def main():
  reader = (line.rstrip() for line in sys.stdin)
  from_url = next(reader)
  to_url = next(reader)
  
  if (is_accessible(from_url, to_url)):
    print("Yes")
  else:
    print("No")
  
if __name__ == "__main__":
  main()