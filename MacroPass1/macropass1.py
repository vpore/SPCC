import re

file = open('macro.txt','r+')
content = file.read()
line = content.split('\n')
length = len(line)

MNT = []
MDT = []
ALA = []

mnt=0
mdt=0
ala=0
i=0

while(i<length):
    if(re.match(r'.*(MACRO).*', line[i])):
        i = i+1
        words = line[i].split()
        for w in words:
            if(re.match(r'.*&.*', w)):
                pass
            else:
                name = w
        MNT.append([mnt,name,mdt])
        mnt = mnt + 1
        MDT.append([mdt,line[i]])
        mdt = mdt + 1
        i = i+1

        while not re.match(r'.*(MEND).*', line[i]): 
            words = line[i].split()
            updated_line = ""
            for w in words:
                if(re.match(r'.*&.*', w)):
                    ALA.append([ala,w])
                    w = w.replace(w,"#"+str(ala))
                    ala = ala + 1
                updated_line += w + " "
            MDT.append([mdt, updated_line])
            mdt = mdt + 1
            i = i+1
        
        if(re.match(r'.*(MEND).*', line[i])):
            MDT.append([mdt,line[i]])
            mdt = mdt + 1

    i = i+1                
        
print('\n\nMDT\n')
print("Index", '\t', "Macro definition", '\t')
for i in MDT:
    print(i[0], '\t', i[1], '\t')
    
print('\n\nMNT\n')
print("Index", '\t', "Macro Name", '\t', "MDT Index")
for i in MNT:
    print(i[0], '\t', i[1], '\t\t', i[2])

print('\n\nDummy Arguments\n')
print("Index", '\t', "Dummy argument", '\t')
for i in ALA:
    print("#",i[0], '\t', i[1], '\t')

print('\n\nALA\n')
for i in ALA:
    print(i[0], '\t')
