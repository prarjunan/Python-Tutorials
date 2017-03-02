#!/usr/bin/python
from collections import Counter
import time

fil1 = r'/home/tutorials/MyDrive/file1.txt'
fil2 = r'/home/tutorials/MyDrive/file2.txt'

def get_file_contents2( ifile ):
	d = {}
	for line in open( ifile ):
		if d.get( line , None ):
			d[line] += 1
		else:
			d[line] = 1
	return d

def get_file_contents3( ifile ):
	return Counter( open( ifile ).readlines() )


def get_file_contents( ifile ):
	return set( open( ifile ).readlines() )

st = time.time()

l = get_file_contents3( fil1 )
r = get_file_contents( fil2 )

c = 0

for line in r:
	if l.get( line, None ):
		c+= l[line]

print 'Count is {}'.format( c )
print 'Total time taken is {} Seconds.'.format( time.time() - st )