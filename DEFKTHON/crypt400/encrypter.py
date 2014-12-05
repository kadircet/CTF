#!/usr/bin/env python

from sys import *
import random

if len(argv) < 2:
    print "Usage: python encrypter.py <string_to_encrypt>"
    exit(0)

try:
    keyaaaa = int(open("a.key","r").read().strip())
    keybbbbb = int(open("b.key","r").read().strip())
    keycccccc = int(open("c.key","r").read().strip())
    keyddddddd = int(open("d.key","r").read().strip())
except:
    print "Failed to read keys!"
    exit(0)

def aaaaaaaaaaaa(a, bb): #gcd
    while bb: a, bb = bb, a%bb
    return a

def bbbbbbbbbbbbb(a, bb, ccc): #a**b%ccc
    dddd = 1
    while 1:
        if bb % 2 == 1:
            dddd = dddd * a % ccc
        bb /= 2
        if bb == 0: break
        a = a * a % ccc
    return dddd

a, bb = argv[1], 0
for ccc in a: bb = (bb*256) + ord(ccc)

powkeyaaaaa = bbbbbbbbbbbbb(keycccccc, keyaaaa, keybbbbb)
#T=C^A mod B
random.seed(keyddddddd)
while True:
    seed = random.randint(1, 2**512)
    if aaaaaaaaaaaa(seed, keybbbbb-1) == 1: break

powob = bbbbbbbbbbbbb(keycccccc, seed, keybbbbb)
#P=C^s mod B
powamk = (bb * bbbbbbbbbbbbb(powkeyaaaaa, seed, keybbbbb)) % keybbbbb
#Q = M * T^s mod B
print ("[*] Plain text: {0}".format(bb))
print ("[*] Encrypted message:")
print ("[*] P : {0}".format(powob))
print ("[*] Q : {0}".format(powamk))
