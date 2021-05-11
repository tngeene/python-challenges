#  this program checks the no.s divisible by 7 but not multiples of 5 between 200
#  and 3200 
l= []
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print (','.join(l))