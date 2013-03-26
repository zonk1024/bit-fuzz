#!/usr/bin/env python

from binascii import hexlify, unhexlify
from sys import argv

allowed = '0123456789abcdefghijklmnopqrstuvwxyz'
allowedmid = allowed + '-'
debug = False

def valid(url):
    url = str(url)
    if url[0] not in allowed or url[-1] not in allowed:
        if debug: print 'returning false b/c of an end'
        return False
    for c in url[1:-1]:
        if c not in allowedmid:
             if debug: print 'returning false b/c of a mid: {}'.format(c)
             return False
    return True

try:
    target = argv[1].lower()
except Exception as e:
    print e
    exit(1)

if not valid(target):
    print 'Invalid domain name'
    exit(1)

print 'Possibilities for {}:'.format(target)

for i in range(len(target)):
    b = bin(int(hexlify(target[i]), 16))
    for j in range(2, len(b)):
        newchar = unhexlify(hex(int(b[0:j] + ('0', '1')[b[j]=='0'] + b[j+1:], 2))[2:])
#        oldchar = b[j]
        newword = target[0:i] + newchar + target[i+1:]
        newword = newword.lower()
        if valid(newword):
            print newword
#    print '"{}" "{}"'.format(bb, len(bb))
#    for c in str(bin(b))[2:]:
#        print c
#    for i in range(len(bb)):
#        if bb[i] == '0':
#            print bb[0:i] + '1' + bb[i+1:], unhexlify(str('0b' + bb[0:i] + '1' + bb[i+1:]))
#        else:
#            print bb[0:i] + '0' + bb[i+1:]


