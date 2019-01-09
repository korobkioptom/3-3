
def histogram(*vhod):
    if len(vhod)==0:
        print ('no_data')
    if len(vhod)==1:
        print(vhod)
    if len(vhod)>1:
        d = dict()
        for c in vhod:
            if  type(c) not in d.keys():
                d[type(c)]=1
            else:
                d[type(c)]+=1
        print (d)
    return (vhod)
hist = histogram('how many times', 'sdds','dfgbc', 56, True,('sa',32,23>32))
print(hist)