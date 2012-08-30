print 'square of even integers in range 100'
l=[i*i for i in range(100) if i%2==0]


m=[[1,2,3],[4,5,6],[7,8,9]]
print 'matrix:',m
t=[[m[i][j] for i in range(3)] for j in range(3)]
print 'transpos:',t
