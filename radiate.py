"""Adin Vashi's Radiate coding challenge - 11/24/20 """

import requests
from PIL import Image

def test_api():
    query_params = {
        "num": 9,
        "min": 0,
        "max": 9,
        "col": 3,
        "format": "plain",
        "base": 10,
        "rnd": "new",
    }
    res = requests.get("https://www.random.org/integers/", params=query_params)
    if not res.ok:
        print("There was an error with the API")
        print(res.status_code)
    print(res.text)

def get_bytes(size):
    rgb_value_count = size * size * 3
    query_params = {
        "num": rgb_value_count,
        "min": 0,
        "max": 255,
        "col": 3,
        "format": "plain",
        "base": 16,
        "rnd": "new",
    }
    res = requests.get("https://www.random.org/integers/", params=query_params)
    if not res.ok:
        print("There was an error with the API")
        print(res.status_code)
    print(res.text)
    pixels = res.content.split(b'\n')
    rgb = []
    #TODO: this is no longer required
    for triplet in pixels:
        for value in triplet.split(b'\t'):
            rgb.append(value)
    rgb = rgb[0:-1]
    rgb = b"".join(rgb)
    return rgb

def generate_random(filename: str, size: int):
    rgb = b""
    request_count = (size / 40) * 3
    for _ in range(int(request_count)):
        rgb = rgb + get_bytes(40)
    image = Image.frombytes("RGB", (size, size), rgb)
    image.save(filename, "JPEG")


if __name__ == "__main__":
    generate_random("./generated_image.jpeg", 120)
