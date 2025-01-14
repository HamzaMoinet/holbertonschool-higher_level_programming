#!/usr/bin/python3
print("".join("{:c}".format(i) for i in range(97, 123) if i != ord('q') and i != ord('e')), end="")
