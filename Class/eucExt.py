def eucExt(a,b):
    v = [a,b]
    x = [1,0] 
    y = [0,1]
    i = 1
    q = [[]]
    while (v[i] != 0): 
        q = q + [v[i-1] // v[i]]
        v = v + [v[i-1] % v[i]]
        x = x + [x[i-1] - q[i]*x[i]]
        y = y + [y[i-1] - q[i]*y[i]]
        i = i+1

    
    return (v[i-1], x[i-1], y[i-1])

a1=101
b1=13
print "MCD(", a1, ",", b1, ") =", eucExt(int(a1),int(b1))[0]
print "x=",eucExt(a1,b1)[1]
print "y=",eucExt(a1,b1)[2]