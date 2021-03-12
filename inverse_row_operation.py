# Finding the inverse of a matrix
from fractions import Fraction

def finding_inverse():
        n = int(input("Enter the order of the matrix: "))
        print()
        # formation of the main list
        given_matrix = []
        print("Enter the elements of a row giving space: ")
        print("For example for row1 of 3X3 matrix type: 1 2 3 ")
        print()
        # to get the  matrix
        for y in range(n):
            while(True):
                print(f"For row{y+1}: ")
                x = list(map(int, input().split()))

                if len(x)==n:
                    given_matrix.append(x)
                    break
                else:
                    print(f"You have to enter {n} numbers.")
                    continue

        # to get the diagonal matrix
        diagonal_matrix = []
        for i in range(n):
            temp_lst = []
            for j in range(n):
                if i == j:
                    temp_lst.append(1)
                else:
                    temp_lst.append(0)
            diagonal_matrix.append(temp_lst)



        # a function to print the matrix
        def print_matrix():
            global max_length
            for i in range(len(given_matrix)):
                for j in range(len(str(i))):
                    if len(str(given_matrix[i][j]))>max_length:
                        max_length = len(str(given_matrix[i][j]))
                    if len(str(diagonal_matrix[i][j]))>max_length:
                        max_length = len(str(diagonal_matrix[i][j]))
            
            for u in range(n):
                for v in range(n):
                    given_matrix[u][v] = str(given_matrix[u][v])
                    print(format(given_matrix[u][v], f"<{max_length+4}"), end="")
                    given_matrix[u][v] = Fraction(given_matrix[u][v])
                print(format("|", f"<6"), end="")
                for z in range(n):
                    diagonal_matrix[u][z] = str(diagonal_matrix[u][z])
                    print(format(diagonal_matrix[u][z], f"<{max_length+4}"), end="")
                    diagonal_matrix[u][z] = Fraction(diagonal_matrix[u][z])
                print()
            print("-"*((max_length+4)*n-1),"*","-"*((max_length+4)*n))
            print()
        print()
        print_matrix()
        # making the matrix lower triangular
        for x in range(n-1):

            for i in range(x, n-1):
                if given_matrix[x][x] == 0:
                    print(" "*((max_length+4)*n-5),f"R{x+1} <---> R{x+2}")
                    given_matrix[x], given_matrix[x + 1] =  given_matrix[x + 1] ,given_matrix[x]
                    diagonal_matrix[x], diagonal_matrix[x + 1] =  diagonal_matrix[x + 1] ,diagonal_matrix[x]
                    print_matrix()
                l = given_matrix[i+1][x]/given_matrix[x][x]
                l = Fraction(l).limit_denominator()
                if l!=0:
                    print(" "*((max_length+4)*n-5),f"R{i+2} ---> R{i+2} - ({l})R{x+1}")
                for k in range(n):
                    given_matrix[i+1][k] -= l*given_matrix[x][k]
                    diagonal_matrix[i+1][k] -= l*diagonal_matrix[x][k]
                    given_matrix[i+1][k] = Fraction(given_matrix[i+1][k]).limit_denominator()
                    diagonal_matrix[i+1][k] = Fraction(diagonal_matrix[i+1][k]).limit_denominator()
                if l!=0:
                   print_matrix()


        for i in given_matrix[0]:
            i = Fraction(i)
        for i in diagonal_matrix[0]:
            i = Fraction(i)

        # making the matrix identity
        for x in range(n-1,0,-1):
            for i in range(x-1, -1, -1):

                l = given_matrix[i][x]/given_matrix[x][x]
                l = Fraction(l).limit_denominator()

                if l!=0:
                    print(" "*((max_length+4)*n-5),f"R{i+1} ---> R{i+1} - ({l})R{x+1}")
                for k in range(n):
                    given_matrix[i][k] -= l*given_matrix[x][k]
                    diagonal_matrix[i][k] -= l*diagonal_matrix[x][k]
                    given_matrix[i][k] = Fraction(given_matrix[i][k]).limit_denominator()
                    diagonal_matrix[i][k] = Fraction(diagonal_matrix[i][k]).limit_denominator()
                if l!=0:
                   print_matrix()

        # making diagonal elements of given matrix to 1
        for i in range(n):
            if given_matrix[i][i] != 1:
                print(" "*((max_length+4)*n-5), f"R{i + 1} ---> R{i + 1}/{given_matrix[i][i]}")
                for j in range(n):
                    diagonal_matrix[i][j] = diagonal_matrix[i][j] / given_matrix[i][i]
                given_matrix[i][i] = 1
                print_matrix()

        print("Hence the inverse of the following matrix is following: ")
        print()
        for u in range(n):

            print(" "*6,"|   ", end="")
            for v in range(n):

                diagonal_matrix[u][v] = str(diagonal_matrix[u][v])
                print(format(diagonal_matrix[u][v], f"<{max_length+4}"), end="")
                diagonal_matrix[u][v] = Fraction(diagonal_matrix[u][v])
            print("|",end="")
            print()

def usercall():
    x=input('do you want to continue?(y/n)')
    if x=='n' or x=='N':
        return False
    else:
        return True

max_length = 0
to_continue=True
while(to_continue):
    try:
        finding_inverse()
    except ZeroDivisionError:
        print('It is a Singular matrix')
    print()
    to_continue=usercall()
    