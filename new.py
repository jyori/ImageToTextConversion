

f = open('qwe.txt',"r")
q = open('qwer.txt',"r")

def space_remover(line):
    x=[]
    for i in line:
        if i == ' ' or i == '\n':
            pass
        else:
            x.append(i)
    for i in x:
        if i ==':':
            x.remove(':')

    return x




line = f.read()
#print(line)
line = line.split()
#print(line)
line= space_remover(line)
#print('*'*100)
#print(line)



line2 = q.read()
#print(line2)
line2 = line2.split()
#print(line2)
line2= space_remover(line2)
#print('*'*100)
#print(line2)


for i,j in zip(line,line2):
    ##print(i , j)
    #print(i ,'<<>>',j)

    if i == j:
        pass

    else:
        print(i)
        for p,q in zip(list(i),list(j)):
            #print('>>>>>>>>>>>>>',p,q)
            if p==q:
                print(p,end='')
            else:
                print(q,'<',end='')
        print('\n','-'*20)



