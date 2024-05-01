import random
choices=[1,2,3]
d={1:'ROCK',2:'PAPER',3:'SISSORS'}
t=1
while t:
    print('Choose 1 or 2 or 3\n1.ROCK\n2.PAPER\n3.SISSORS')
    a=int(input('Enter Your Choice: '))
    b=random.choice(choices)
    if a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
        print('you choosed: ',d[a],'AND Computer: ',d[b],'\n YOU WON\n')
    else:
        print('you choosed: ',d[a],'AND Computer: ',d[b],'\n YOU LOSS\n')
    k=input('Do You Want To Continue(Y/N):')
    if k=='Y' or k=='y' or k=='N' or k=='n':
        temp=0
    else:
        temp=1
    while temp:
        print('Enter Valid Input:')
        k=input('Do You Want To Continue(Y/N):')
        if k=='Y' or k=='y' or k=='N' or k=='n':
            temp=0
        else:
            temp=1
    if k=='N' or k=='n':
        t=False