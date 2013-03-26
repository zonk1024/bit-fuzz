#!/usr/bin/env python

from binascii import hexlify, unhexlify
from sys import argv

try:
    target = argv[1]
except Exception as e:
    print e
    exit(1)

allowed = '0123456789abcdefghijklmnopqrstuvwxyz'


print 'Possibilities for {}:'.format(target)

for i in range(len(target)):
    b = bin(int(hexlify(target[i]), 16))
    for j in range(2, len(b)):
        newchar = unhexlify(hex(int(b[0:j] + ('0', '1')[b[j]=='0'] + b[j+1:], 2))[2:])
        newword = target[0:i] + newchar + target[i+1:]
        newword = newword.lower()
        if newword != target and (newchar in allowed or ((i>1 and i<len(target)-1) and newchar == '-')):
            print newword
#    print '"{}" "{}"'.format(bb, len(bb))
#    for c in str(bin(b))[2:]:
#        print c
#    for i in range(len(bb)):
#        if bb[i] == '0':
#            print bb[0:i] + '1' + bb[i+1:], unhexlify(str('0b' + bb[0:i] + '1' + bb[i+1:]))
#        else:
#            print bb[0:i] + '0' + bb[i+1:]
