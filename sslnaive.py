import sys
try:ll=int(sys.argv[1])
except:ll=30
from random import randrange as rn
from random import choice
def pf():return choice((True,False))
L=[rn(1,6) if pf() else -rn(1,7) for x in range(ll)]
print(L)
def futee(L):
	t=r=0
	for v in L:
		t=max(0,t+v)
		r=max(r,t)
	return r
print(f"methode futee {futee(L)}")
print("methode naive : ......")
record=0
for lg in range(0,ll):
	for ld in range(lg+1,ll):
		tt=sum(L[lg:ld+1])
		if tt>record:
			record=tt
print(record)
