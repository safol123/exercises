def skipmultiples(a,b):
    for i in range (a,b):
        if i%3 ==0:
            print 'Reiterate until it works'
        else:
            print i
            
print skipmultiples(1,51)
