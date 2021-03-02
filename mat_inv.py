#import numpy as np
print('___________Matrix Inverse Calculator(3x3)________')
#N=input('Enter size of matrix(AxA):')
A=[[],[],[]]

for i in range(3):
    for j in range(3):
        ele=input(f'Enter {i+1},{j+1} :')
        A[i].append(int(ele))

print('A:')

for i in range(3):
    for j in range(3):
        print(A[i][j],end='  ')
    print()

cof=[[0,0,0],[0,0,0],[0,0,0]]
#i=-1

cof[0][0]=(1)*(A[1][1]*A[2][2]-A[2][1]*A[2][2])
cof[0][1]=(-1)*(A[1][0]*A[2][2]-A[2][0]*A[2][2])
cof[0][2]=(1)*(A[1][0]*A[2][1]-A[2][0]*A[1][1])
cof[1][0]=(-1)*(A[0][1]*A[2][2]-A[2][1]*A[0][2])
cof[1][1]=(1)*(A[0][0]*A[2][2]-A[2][0]*A[0][2])
cof[1][2]=(-1)*(A[0][0]*A[2][1]-A[2][0]*A[0][1])
cof[2][0]=(1)*(A[0][1]*A[1][2]-A[1][1]*A[0][2])
cof[2][1]=(-1)*(A[0][0]*A[1][2]-A[1][0]*A[0][2])
cof[2][2]=(1)*(A[0][0]*A[1][1]-A[1][0]*A[1][1])

for i in range(3):
    for j in range(3):
        print(f'Cofactor {i+1},{j+1} :{cof[i][j]}')

#transposing
print('Cof:')

for i in range(3):
    for j in range(3):
        print(cof[i][j],end='  ')
    print()

Adj=[[0,0,0],[0,0,0],[0,0,0]]

det=A[0][0]*cof[0][0]+A[0][1]*cof[0][1]+A[0][2]*cof[0][2]

for i in range(3):
    for j in range(3):
        Adj[i][j]=cof[j][i] #Transposing

print('Adj:')

for i in range(3):
    for j in range(3):
        print(Adj[i][j],end='  ')
    print()

print(f'Det={det}')

input('Press Enter key to End...')