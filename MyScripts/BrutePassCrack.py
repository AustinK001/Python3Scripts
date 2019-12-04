import random

    letters = [str(i) for i in range('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p')]
    s = [''.join([a,b,c,d,e,f,g,h]) for a in letters for b in letters for c   in letters for d in letters for e in letters for f in letters for g in letters  for h in letters]
    random.shuffle(s)
    real_password = 'aaaaaaaa'
    i = 0

    for code in s:
        if code == real_password:
            print()
            print('The password is: ', code)
             break
        else:
            i += 1
            print(i, ' failures', end='\r')import random
