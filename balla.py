a={'id':'123\u0000456','name':'karthik\u0000mitta','office':'wi\u0000pro'}
b={}
for i,j in a.items():
    x=j.split('\u0000')
    a[i]=''.join(x)
print(a)
        
        
    
    

