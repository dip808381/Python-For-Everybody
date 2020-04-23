fname = input('Enter file name: ')
if len(fname) < 1 : name = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        di[w] = di.get(w, 0) + 1
print(di)

temp = list()
for k,v in di.items():
    print(k,v)
    newt = (v, k)
    temp.append(newt)
print(temp)
temp = sorted(temp, reverse = True)
print('Sorted', temp)

for v, k in temp[:5]:
    print(k, v)