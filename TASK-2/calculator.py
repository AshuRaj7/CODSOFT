t=True
temp=0
while t:
    a=int(input('Enter num-1 :'))
    b=int(input('Enter num-2 :'))
    o=input('Enter Operator :')
    match o:
        case '+':
            print('Result: ',a+b)
        case '-':
            print('Result: ',a-b)
        case '%':
            print('Result: ',a%b)
        case '/':
            print('Result: ',a/b)
        case '*':
            print('Result: ',a*b)
        case default :
            print('Enter Valid Input')
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
        
        