# -*- encoding: utf-8 -*-
f = open("rslv_dict.txt", "r")
d = dict([s.split() for s in f])
f.close()
s = raw_input("search for: ")
nf = 1
for k, v in d.items():
    if s in k or s in v:
        print "found: '{0}' '{1}'".format(k,v)
        nf = 0
if nf: print "not found"
