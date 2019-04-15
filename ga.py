import random
from itertools import groupby

amount = 127
scope =8

list_of_chroms=[]
list_of_dec=[]
scores=[]
percentes=[]

chromosoms=[]
def truncate(n):
    return int(n * 10000) / 10000

def percentage(part, whole):
    return (part / whole) * 100.00

def func(arg):
    fun =2*(arg**2 + 1)
    return fun

def count_ocs(lista):
    sum=[]
    for s in range(scope):
        sum.append(lista.count(s))
    return sum    

def chose_best(lista):
    best_pair=[]
    indexes=[]
    tmp = lista
    tmp = sorted(tmp)
    tmp = list(reversed(tmp))
    best_pair.append(tmp[0])
    best_pair.append(tmp[1])

    indexes.append(lista.index(tmp[0]))
    indexes.append(lista.index(tmp[1]))

    return best_pair, indexes


def to_binary(num):
    binar = bin(num)
    bin2 = binar[2:]
    while len(bin2) < 7:

        bin2 =str(0)+bin2
    return bin2

for x in range(0, scope):
    rand = random.randint(1,amount)
    chromosom = to_binary(rand)
    chromosoms.append(chromosom)

    list_of_chroms.append(chromosom)
    list_of_dec.append(rand)
    scores.append(func(rand))

    print(chromosom+' (' + str(rand) +')' +' - '+ str(func(rand)))

# print(list_of_chroms)
# print(scores) 
print()

for score in scores:
    percent = percentage(score, sum(scores) )
    percentes.append(percent)
    print(percent)

print()
tm=[]
for per in percentes:
    if not tm:
        tm.append(truncate(per))
    else:
        tm.append(truncate(per) + tm[-1])
print(tm)

pairs=[]  # to tak naprawde konkretne przedziały
lasts=[]
for part in tm:
    pair=[]
    if not pairs:
        pair.append(0)
        pair.append(part)
    else:
        pair.append(lasts[-1])
        pair.append(part)

    lasts.append(part)    
    pairs.append(pair)    

print(pairs)
    
losowe=[]    
for x in range(8):
    rnd = random.random()*100  ### yes, it is float
    for pair in pairs:
        if rnd >pair[0] and rnd <=pair[1]:
            losowe.append(pairs.index(pair))

print()
print(losowe)
ocurrences=count_ocs(losowe)
print(ocurrences)
print()
cb_best = chose_best(ocurrences)[0]
cb_indx = chose_best(ocurrences)[1]
print(cb_best)
print(cb_indx)

print(chromosoms[cb_indx[0]])
print(chromosoms[cb_indx[1]])

def crossing(chrom1, chrom2):
    wynik=""
    wynik2=""
    rnd = random.choice([1,2,3,4,5,6])  # picking locus
    for c in range(7):
        if c < rnd-1:
            wynik+= chrom1[c]
            wynik2+= chrom2[c]
        else:
            wynik+= chrom2[c]
            wynik2+= chrom1[c]       
    return  [wynik,wynik2]

print('-- -- -- --')
c1 = crossing(chromosoms[cb_indx[0]], chromosoms[cb_indx[1]])[0]
c2 = crossing(chromosoms[cb_indx[0]], chromosoms[cb_indx[1]])[1]

print(c1 +" - "+str(int(c1,2)))
print(c2 +" - "+str(int(c2,2)))





