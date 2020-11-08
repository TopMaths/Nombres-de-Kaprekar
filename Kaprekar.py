# Fichier fourni par Top Maths, sans aucune garantie
# pour illustrer la vidéo sur les nombres de Kaprekar
# à l'adresse https://youtu.be/7tAZukqSInk
# Merci de ma faire de la pub


import PGCD


def isKaprekar(n,b):
    """détermine si n est un nombre de Kaprekar en base b.
dans ce cas, retourne la  hauteur de nombre, sinon, renvoie -1

attention 1 a plusieurs hauteurs, une seule est renvoyée : 1.

Un nombre de Kaprekar de hauteur k en base b est un entier n,
tel qu'il existe deux entiers naturels u et v vérifiant 
n= u*b^k+v avec 0<v<b^n et n=u+v.
k  est la hauteur du nombre de Kaprekar 


exemple :
>>> Kaprekar(5292,10)
6
car 5292**2 = 28005264 et 5292= 005264 + 28  
"""

    if n==0: return -1
    if n==1: return 1
    import math
    N=n**2
    c=1+math.floor(math.log(N,b)) # nb de chiffres de N en base b
    for k in range(c+1,0,-1):
        p1=N//b**k
        p2=N-b**k*p1
        if p2>0 and p1+p2==n:
            return k
    return -1

def listeK(b,max):
    """renvoie la liste des nombres inférieurs strict à max lorsqu'ils sont de Kaprekar en base b, ils sont accompagnés de leur hauteur"""
    L=[ (x,y) for x in range(max) for y in [Kaprekar(x,b)] if y>0 ]
    return L

def DiviseursUnitaires(k,n):
    """renvoie la liste des diviseurs unitaires de $n^k-1$, rangés dans l'ordre croissant

exemple :
>>> DiviseursUnitaires(2,10)
[1,9,11,99]
"""

    # algorithme idiot, pas du tout efficace pour les grandes valeurs de k
    x=n**k-1
    L=[1,x]
    p=2
    while p**2<=x:
        if x%p==0 and PGCD.pgcd(p,x//p)==1:
            L.append(p)
            L.append(x//p)
        p+=1
    return sorted(L)

def Kaprekar(k,n):
    """construit la liste des k-nombres de Kaprekar en base b

Exemple
>>> Kaprekar(4,10)
[1, 2223, 2728, 4950, 5050, 7272, 7777, 9999]
"""
    L=[]
    DU=DiviseursUnitaires(k,n)
    while DU:
        p=DU.pop()
        q=DU.pop(0)
        a,b,_=PGCD.bezout(p,q)
        if a>0:
            L.append(a*p)
            L.append((b+p)*q)
        else:
            L.append(b*q)
            L.append((a+q)*p)
    return sorted(L)



