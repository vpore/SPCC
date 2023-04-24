
grammar = open('prod.txt', 'r')
productions = {}
nt = []

for prod in grammar:
    elem = []
    
    for i in prod:
        if(i=='-' or i=='>' or i=='\n'):
            continue
        else:
            elem.append(i)
            
    left_prod = elem.pop(0)
    right_prod = []
    temp_right_prod = []
    
    for j in elem:
        if(j != '|'):
            temp_right_prod.append(j)
            if (not j.isupper() and j!='*' and j not in nt):
                nt.append(j)
        else:
            right_prod.append(temp_right_prod)
            temp_right_prod = []
    
    right_prod.append(temp_right_prod)
    productions[left_prod] = right_prod

print('\nProductions :')
for key, value in productions.items():
    print(key, ' --> ', value)

print('\nNon-Terminals : ', nt, end='\n\n')

first = {}
follow = {}

first_file = open('first.txt', 'r')
follow_file = open('follow.txt', 'r')

for i in first_file:
    first[i[0]] = set()
    for j in i:
        if j==' ' or j==i[0] or j==',' or j=='\n':
            pass
        else:
            first[i[0]].add(j)

for i in follow_file:
    follow[i[0]] = set()
    for j in i:
        if j==' ' or j==i[0] or j==',' or j=='\n':
            pass
        else:
            follow[i[0]].add(j)
print('First : ', first, end='\n\n')
print('Follow : ', follow, end='\n\n')

LL1 = {}

def foo(s, p):
    prod = s+'->'
    rhs = ''
    for i in p:
        rhs += i
    prod += rhs
    return prod

for s in productions:
    for p in productions[s]:
        if p[0].isupper():
            for f in first[p[0]]:
                key = s+'\t'+f
                LL1[key] = foo(s, p)
        
        else:
            if(p[0]!='*'):
                key = s+'\t'+p[0]
                LL1[key] = foo(s, p)
            else:
                for f in follow[s]:
                    key = s+'\t'+f
                    LL1[key] = foo(s, p)

print('Row\tColumn\tProduction')
for key, value in LL1.items():
    print(key, '\t', value)