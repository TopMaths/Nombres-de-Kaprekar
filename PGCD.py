# Fichier PGCD.py fourni par Top Maths sans aucune garantie
# Merci de faire de la pub pour ma chaine Youtube !




def pgcd(a,b):
    """calcule le pgcd de deux entiers a et b.

 Ce programme fonctionne également si a et b sont des éléments d'un anneau représentés par des objets dont l'opérateur % a été défini et qui calcule un reste de division euclidienne


exemple 
>>> pgcd(138,114)
6
 """


    
    while b!=0:
        a,b=b,a%b
    return a


def bezout(a,b):
    """Ce programme calcule le pgcd de deux entiers a et b et fournit aussi un couple de coeffcients de Bézout.

exemple : 
>>> bezout(138,114)
(5, -6, 6)

car pgcd(138,114) =6 et   5 * 138 - 6 * 114=6
"""
    u1,v1=1,0
    u2,v2=0,1
    while(b!=0):
        q=a//b
        u1,v1,a,u2,v2,b=u2,v2,b,u1-q*u2,v1-q*v2,a-q*b
    return (u1,v1,a)



