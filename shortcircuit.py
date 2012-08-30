l=(1,2,3,4,5,6)
def even(x):
	return (x%2==0 and True or False)

def pr(s):
	print s
def printnumtype(x):
	(even(x) and pr('even') or pr('odd'))

even=lambda x: (x%2==0 and True or False)

l_even=filter(even,l)
