#tupleiterator

l=(1,2,3)
print 'tuple:',l
it=iter(l)
print it.next()
print it.next()
print it.next()
print it.next()

l=[1,2,3]
print 'list:',l
it=iter(l)
print it.next()
print it.next()
print it.next()
print it.next()
it=iter(l)
for i in it:
	print i

l={'a':1,'b':2,'c':3}
print 'dict:',l
it=iter(l)
for i in it:
	print i,l[i]
