import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
while 1:
    try:
        a=list(map(int, input().split()))
        matrix=[]
        for i in range(a[0]):
            matrix.append(list(map(int, input().split())))
        query=[]
        for i in range(a[2]):
            query.append(list(map(int, input().split())))
        flag, rUnknown, cUnknown=1, set([i for i in range(a[0])]), set([i for i in range(a[1])])
        while flag:
            flag=0
            for i in rUnknown.copy():
                r = [[0, 0], [0, 0]]
                for j in range(a[1]):
                    if matrix[i][j]!=0:
                        if r[0][1]==0:
                            r[0][0], r[0][1]=j, matrix[i][j]
                        elif r[1][1]==0:
                            r[1][0], r[1][1] = j, matrix[i][j]
                if r[0][1]!=0 and r[1][1]!=0:
                    flag=1
                    rUnknown.remove(i)
                    q=int((r[1][1]-r[0][1])/(r[1][0]-r[0][0]))
                    for j in range(a[1]):
                        matrix[i][j]=matrix[i][0]+q*(j)
            for j in cUnknown.copy():
                r = [[0, 0], [0, 0]]
                for i in range(a[0]):
                    if matrix[i][j]!=0:
                        if r[0][1]==0:
                            r[0][0], r[0][1]=i, matrix[i][j]
                        elif r[1][1]==0:
                            r[1][0], r[1][1] = i, matrix[i][j]
                if r[0][1]!=0 and r[1][1]!=0:
                    flag=1
                    cUnknown.remove(j)
                    q=int((r[1][1]-r[0][1])/(r[1][0]-r[0][0]))
                    for i in range(a[0]):
                        matrix[i][j]=matrix[0][j]+q*(i)
        for x in query:
            if (x[0]-1) in rUnknown and (x[1]-1) in cUnknown:
                print('UNKNOWN')
            else:
                print(matrix[x[0] - 1][x[1] - 1])
    except:
        break

import collections
while 1:
    try:
        a=input()
        b=input()
        if len(a)!=len(b) or collections.Counter(a)!=collections.Counter(b):
            print(-1)
            continue
        res, i=0, 0
        while a!=b:
            while a[i]==b[i]:
                i+=1
            a=a[:i]+a[i+1:]+a[i]
            res+=1
        print(res)
    except:
        break

while 1:
    try:
        n=int(input())
        l=list(map(int, input().split()))
        r=list(map(int, input().split()))
        res=[[]]
        for i in range(len(l)):
            for x in res:
                for y in range(l, r+1):
                    x.append(x+[y])
        print(res)
    except:
        break