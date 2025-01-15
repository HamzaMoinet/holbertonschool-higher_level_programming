#!/usr/bin/python3
def uppercase(str):
    upper_char = ""
    for c in str:
        if 'a' <= c <= 'z':
            upper_char += chr(ord(c) - 32)
        else:
            upper_char += c
    print(upper_char)
