#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ~ demander le nb d'equipes
n=int(input("entrez le nb d equipes : "))
d=1
p=2
H=list(range(3,(n+4)//2))
B=list(range((n+4)//2,n+1))
for j in range(1,n):
	J=[]
	J.append( (1,p) )
	for  h,b in zip(H,B) : 
		x=[h,b]
		x.sort()
		J.append( tuple(x)  )
	B.insert(0,p)
	H.append(B.pop())
	p=H.pop(0)
	print(J)
	
