from math import gcd

def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)

import sys

up1, down1 = tuple(map(int, sys.stdin.readline().split()))
up2, down2 = tuple(map(int, sys.stdin.readline().split()))
up = (up1 * (lcm(down1, down2)) // down1) + (up2 * (lcm(down1, down2) // down2))
down = lcm(down1, down2)
print(up // gcd(up, down), down // gcd(up, down))