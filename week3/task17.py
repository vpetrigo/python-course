#!/usr/bin/env python3
# coding=utf-8

import sys
import requests
import json

number_url = "http://numbersapi.com/{}/math"

parameters = {"default": "Boring", "json": True}

def main():
    out = open("dataset_24476_3_output.txt", "w")

    with open("dataset_24476_3.txt") as dataset:
        for num in dataset:
            resp = requests.get(number_url.format(int(num)), params=parameters)
            json_data = resp.json()

            if json_data["text"] == parameters["default"]:
                print(json_data["text"], file=out)
            else:
                print("Interesting", file=out)

    out.close()

if __name__ == "__main__":
    main()
