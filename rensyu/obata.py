#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import csv
from copy import deepcopy
 
in_file = 't.csv'
f = open(in_file, "r")
data = csv.reader(f)
# header = next(reader)
 
#for row in tmp:i

data_c = deepcopy([ v for v in data])
f.close()

print "input file data:"
for row in data_c:
        print row

data2 = list(map(list, zip(*data_c)))
#data2 = list(map(list, zip(*data)))
#data2 = zip(*data)

print "transpose data2:"
for row2 in data2:
        print row2
print data_c

fw = open('t-out.csv', 'w')
writer = csv.writer(fw, lineterminator='\n')
# writer.writerow(list)
writer.writerows(data2)
fw.close()

