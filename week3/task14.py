#!/usr/bin/env python3
# coding=utf-8

import requests
import re
import sys

class NotFound(Exception):
  pass

def get_urls(content):
  pattern = re.compile(r"<a\s.*?\s?href=[\"\']{1}([\w:\/.?&=\-]+)[\"\']{1}.*?>")
  
  return pattern.findall(content)

def get_abs_link(url):
  if url[:2] == "..":
    return []
    
  pattern = re.compile(r"\b(https|http|ftp)?(:\/\/)?([\w.\-]+)\/?(.*)")
  return pattern.match(url)

def main():
  reader = (line.rstrip() for line in sys.stdin)
  html_url = next(reader)
  resp = requests.get(html_url)
  
  if resp.status_code != 200:
    raise NotFound
  
  urls = get_urls(resp.text)
  res = [get_abs_link(main_dom) for main_dom in urls]
  abs_link = set(link.group(3) for link in res if link)
  abs_link = list(abs_link)
  abs_link.sort()

  for l in abs_link:
    print(l)
  
def test():
  resp = requests.get("mail.ru")
  
  if resp.status_code != 200:
    raise NotFound
  
  res = [get_abs_link(main_dom) for main_dom in get_urls(resp.text)]
  abs_link = set(link.group(3) for link in res if link)
  abs_link = list(abs_link)
  abs_link.sort()
  
  print(abs_link)
  

if __name__ == "__main__":
  test()
  main()