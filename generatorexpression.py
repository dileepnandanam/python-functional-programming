print 'square of even integers between 0-100'
l=(i*i for i in range(100) if i%2==0)
for i in l:
	print i
	

import re
l=['asdfffffafa','eww','ffff','asd']

print 'iterator for subset containing regExp f+ on list',l
it=(i for i in l if re.search(r'f+',i))
for i in it:
	print i

