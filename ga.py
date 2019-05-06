import random
from itertools import groupby

amount = 127
scope =8
bits=7

list_of_dec=[]
scores=[]
percentes=[]


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


def chose_best(lista, list_of_chroms):
    results=[]
    for x in lista:
        results.append(list_of_chroms[x])
    return results

def to_binary(num):
    binar = bin(num)
    bin2 = binar[2:]
    while len(bin2) < bits:
        bin2 =str(0)+bin2
    return bin2

# generating start poulation of 'scope' chromosoms
def generate_init():
    chromosoms=[]
    for x in range(scope):
        rand = random.randint(1,amount)
        chromosom = to_binary(rand)
        chromosoms.append(chromosom)
    return chromosoms

def init(chroms):
    scrs=[]
    for x in chroms:
        ran = int(x, 2)
        list_of_dec.append(ran)
        scrs.append(func(ran))

        print(x+' (' + str(ran) +')' +' - '+ str(func(ran)))
    print()
    return scrs
#krzyzowanie

def crossing(chrom1, chrom2):
    wynik = ""
    wynik2 = ""
    rnd = random.choice([1, 2, 3, 4, 5, 6, 7])  # picking locus
    for c in range(bits):
        if c <= rnd-1:
            wynik += chrom1[c]
            wynik2 += chrom2[c]
        else:
            wynik += chrom2[c]
            wynik2 += chrom1[c]
    return [wynik, wynik2]

def mutate(chroms):
    res=[]
    for chrom in chroms:
        x = random.choice([0,1,2,3,4,5])
        if x == 5:
            replace = random.choice([0,1,2,3,4,5,6])
            teem = list(chrom)
            if teem[replace]=='0':
                teem[replace] = '1'
            else:
                teem[replace] = '0'
            chrom= ''.join(teem)
        res.append(chrom)
    return res


def perform():

    list_of_chroms = generate_init()
    init(list_of_chroms)
    for iii in range(200):
        scores = init(list_of_chroms)
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
        # print(tm)

        # przedzialy
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

        # print(pairs)

        #losowanie   
        losowe=[]    
        for x in range(8):
            rnd = random.uniform(0,100)  ### yes, it is float
            for pair in pairs:
                if rnd >pair[0] and rnd <=pair[1]:
                    losowe.append(pairs.index(pair))

        print()
        # print(losowe)
        # print(count_ocs(losowe))
        print()
        cb_best = chose_best(losowe, list_of_chroms)
        print('przed tasowaniem: '+str(cb_best))
        print('przed tasowaniem: '+str(losowe))
        for i in range(15):
            random.shuffle(cb_best)
        
        print('po tasowaniu: '+str(cb_best))

        print('-- -- -- --')


        # # for i in range(len(cb_best)):
        # c1 = crossing(cb_best[0], cb_best[1])[0]
        # c2 = crossing(cb_best[0], cb_best[1])[1]
        # print(c1 + " - "+str(int(c1, 2)))
        # print(c2 + " - "+str(int(c2, 2)))
        new_gen=[]
        for x in [0, 2, 4, 6]:
            c1 = crossing(cb_best[x], cb_best[x+1])[0]
            c2 = crossing(cb_best[x], cb_best[x+1])[1]
            # print(c1 + " - "+str(int(c1, 2)))
            # print(c2 + " - "+str(int(c2, 2)))
            new_gen.append(c1)
            new_gen.append(c2)
        print(new_gen)
        print('mutatio n!!!')
        new_gen=mutate(new_gen)
        print(new_gen)
        list_of_chroms = new_gen
        init(list_of_chroms)
        print("-----------  ----------- end of gen "+str(iii+1)+' ----------- ----------')


perform()

def print_example():
    for a in range(10):
        for x in range(8):
                    print(random.uniform(0,100))
        print()           

# print_example()
    
    
