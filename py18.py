def merge(dic1, dic2):
    return(dic2.update(dic1))
    
dic1 = {'b':1, 'n':7, 'm':9}
dic2 = {'a':6, 'r':10}
merge(dic1, dic2)
print(dic2)

