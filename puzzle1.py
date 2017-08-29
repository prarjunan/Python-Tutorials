#!/usr/bin/python

# e = 10
# h = 1
# c = 0.125

# ne + nh + nc = 100

# ne*e + nh*h + nc*c = 100

# ne*10 + nh + nc/8 = 100

for e in xrange(1,99):
    for h in xrange(1,99):
        for c in xrange(1,99):
            if sum( [e,h,c] ) == 100 and sum( [ e*10,h,c*0.125] ) == 100:
            	print 'E : {}, H : {}, C : {}'.format( e,h,c )
