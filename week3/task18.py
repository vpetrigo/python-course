#!/usr/bin/env python3
# coding=utf-8

import requests
import json

artsy_token_url = "https://api.artsy.net/api/tokens/xapp_token"
artsy_api_url = "https://api.artsy.net/api/artists/{}"

info = {
    "client_id": "c72ead62d8fb82ddd3ca",
    "client_secret": "eea6663ca58325d9d41fb8e48c3b3a59"
}

class NotFound(Exception):
    pass

class TokenFail(Exception):
    pass

def get_token():
    token_data = requests.post(artsy_token_url, data=info)

    if token_data.status_code == 400:
        raise NotFound

    json_token = token_data.json()

    return json_token["token"]

def main():
    headers = {"X-XAPP-Token": get_token()}

    with open("dataset_24476_4.txt", "r") as artists_inp, open("dataset_24476_4_out.txt", "w") as artist_info_out:
        reader = (art_id.rstrip() for art_id in artists_inp)
        artists_info = []

        for art_id in reader:
            resp = requests.get(artsy_api_url.format(art_id), headers=headers)
            json_resp = resp.json()
            artists_info.append((json_resp["birthday"], json_resp["sortable_name"]))

        artists_info.sort()

        for artist in artists_info:
            print(artist[1], file=artist_info_out)


if __name__ == "__main__":
    main()
