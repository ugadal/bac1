#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as rnd
import sys
import itertools as it
mxo=int(sys.argv[1]) #max object
pmx=int(sys.argv[2]) #poids max
seed=float(sys.argv[3]) #random seed

rnd.seed(seed)

LO=[] # L iste d' O bjets
for i in range(mxo):
	p=rnd.randrange(1,10)
	v=4*p+rnd.randrange(1,20)+1
	LO.append((p,v))
# ~ LO=sorted(LO,key= lambda t:t[1]/t[0])
# ~ LO=sorted(LO,key= lambda t:t[0])
	# ~ print(p,v,v/p)
for p,v in LO:
    print (p,v,f"({v/p})")
# ~ print("technique anthony")
# ~ csum=0
# ~ sac=[]
# ~ ALO=list(LO)
# ~ while True:
	# ~ while csum<=pmx:
		# ~ sac.append(ALO.pop(0))
		# ~ csum+=sac[-1][0]
	# ~ print(sac,sum([p for p,v in sac]),sum([v for p,v in sac]))
	# ~ debord=csum-pmx
	# ~ filtered=[(p,v) for p,v in sac if p>=debord]
	# ~ minv=min([v for p,v in filtered])
	# ~ torem=next((p,v) for p,v in filtered if v==minv)
	# ~ print("remove",torem)
	# ~ sac.remove(torem)
	# ~ csum-=torem[0]
	# ~ print(sac,sum([p for p,v in sac]),sum([v for p,v in sac]))
	# ~ input()

# ~ print ("technique brute force")
# ~ for nbo in range(1,mxo+1):
	# ~ for comb in it.combinations(LO,nbo):
		# ~ if sum([p for p,v in comb])>pmx:continue
		# ~ print (sum([v for p,v in comb]),comb)

input()
# ~ exit()
Sacs=[]
Nsacs=[]
for x in range(pmx+1):Sacs.append([])
L=[0]*(pmx+1)

for p,v in LO:
	NL=L[:p]
	Nsacs=[]
	for os in Sacs[:p]:Nsacs.append(list(os))
	for d,u,ds,ts in zip(L,L[p:],Sacs,Sacs[p:]):
		NL.append(max(d+v,u))
		if d+v>u:
			Nsacs.append(ds+[(p,v)])
		else:Nsacs.append(list(ts))
	for x in range(pmx+1):Sacs[x]=Nsacs[x]
	print (" ".join(["%3i"%x for x in [p,v]+NL]),end="\n")
	L=list(NL)
# ~ input()
print (L[-1])
input()
print (Sacs[-1])
