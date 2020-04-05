import numpy as np
n = int(input("Size of the Matrix:"))  
original_matrix = []
for i in range(n):
    original_matrix.append(list(map(int, input().rstrip().split())))
original_matrix_plus_identity = np.add(original_matrix, np.identity(n))
multiplier = np.copy(original_matrix_plus_identity)
while not np.array_equal(multiplier.dot(original_matrix_plus_identity) > 0,  multiplier):
    multiplier = multiplier.dot(original_matrix_plus_identity) > 0
next=[]
parent=[]
maprow=[]
for i in range(n):
    maprow.append(i)
while 1 :
    flag = 0
    for i in range(n):
        for j in range(n):
            if (i < j and np.array_equal(multiplier[i],multiplier[j]) and np.array_equal(multiplier[ : , i], multiplier[ : , j])):
                multiplier = np.delete(multiplier, j, 0)
                multiplier = np.delete(multiplier, j, 1)
                for k in range(j, n):
                    maprow[k] += 1
                n = n - 1
                flag = 1
                break
        if(flag):
            break
    if (not flag):
        break
for i in range(n):
    parent.append([])
    next.append([])
for i in range(n):
    for j in range(n):
        if (multiplier[i][j]):
            next[i].append(j)
            parent[j].append(i)
B= set([])
C= [set() for _ in range(n)]
E= set([])
for i in range(n):
    C[i] = (set(parent[i]) & set(next[i]))
    if(C[i] == set(parent[i])):
        B.add(i)
    if(C[i]  == set(next[i])):
        E.add(i)
blocks = []
alreadyin_flag=[]
for i in range(n):
    alreadyin_flag.append(0)
restlist=[]
for i in B:
    tempflag = 0
    for j in B:
        if(i != j):
            if (bool(set(next[i]) & set(next[j])) == 1):
                tempflag = 1
                break
    if(not tempflag):
        if (alreadyin_flag[i] == 0):
            blocks.append(next[i])
            alreadyin_flag[i] = 1
    else:
        for j in next[i]:
            if (not (j in restlist)):
                restlist.append(j)
row = []
blocks.append(restlist)
for _blocks in blocks:
    num = len(_blocks)
    while(num != 0):
        for i in _blocks:
                if(not(i in row) and set(next[i]) == C[i]):
                   row.append(i)
                   for j in _blocks:
                      if (i in next[j]):
                         next[j].remove(i)
                      if (i in parent[j]):
                         parent[j].remove(i)
                      C[j] = (set(parent[j]) & set(next[j]))
                      
                   num = num - 1
                   break
skeleton = np.copy(multiplier).astype(int)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if(i != j and i != k and j != k and multiplier[i][j] and multiplier[i][k] and multiplier[j][k]):
                skeleton[i][k] = 0
skeleton-=np.identity(n).astype(int)
ans = np.zeros((n,n))
for i in range(n):
    for j in range(n):
       ans[i][j] = skeleton[row[i]][row[j]]
for i in range(n):
    row[i] = maprow[row[i]] + 1
print("The rows and columns are printed in the following order corresponding to the original matrix:",row[:n])
print(ans)
