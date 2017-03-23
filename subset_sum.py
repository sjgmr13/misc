from itertools import product

def nulla_egy(arr,num):
    n=len(arr)
    szum=[0]*pow(2,n)
    lista=[]
    a = -1
    for i in [list(elem) for elem in product([1, 0], repeat =n)]:
        a +=1
        lista.append(i)
        for j in range(len(i)):
            szum[a] +=arr[j]*i[j]
    

    eredmeny_lista=[]
    for i in range(len(szum)):
        if szum[i]==num:
            eredmeny_lista.append(lista[i])
    
    eredmeny = []
    for i in range(len(eredmeny_lista)):
        eredmeny.append([a*b for a,b in zip(eredmeny_lista[i],arr)])
    
    return eredmeny
