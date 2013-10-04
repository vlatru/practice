# -*- encoding: utf-8 -*-
f = open("rslv_dict.txt", "r")
d = dict([line.split() for line in f])
for k, v in d.items():
    print "'{0}' '{1}'".format(k, v)
ip = raw_input("type ip: ")
name = raw_input("type name: ")
f = open("dict.txt", "a")
f.write("{0} {1}\n".format(ip, name))
f.close()
