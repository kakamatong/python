import os

with open("txt/test.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line)