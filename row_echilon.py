
# input your values in the below 4 lines   use the constants in front of each equation
# if a constant is not mentioned ( that is it is zero for a variable mention zero and don't skip it)
# if the values obtained are in fraction truncate the values to the required decimal places on your own.
x1,y1,z1 = map(float,input("enter the first row elements").split())
x2,y2,z2 = map(float,input("enter the second rew elements").split())
x3,y3,z3 = map(float,input("enter the third row elements").split())

a1,a2,a3 =  map(float,input("enter the values of answer column").split())
if x1==0:#checking whether the first row has the first element zero or not.
    x1, x2 = x2, x1# swapping the first row with the second row.
    z1, z2 = z2, z1
    z1, z2 = z2, z1
    a1, a2 = a2, a1
    if x1==0:
        x1, x3 = x3, x1# swapping the first row with the third row if second row also has zero as first element.
        z1, z3 = z3, z1
        z1, z3 = z3, z1
        a1, a3 = a3, a1

if x1!=0:
    k1 = x2/x1
    k2 = x3/x1

    y2 = y2-k1 *y1
    z2=z2-k1*z1
    a2=a2-k1*a1
    y3=y3-k2 *y1
    z3= z3-k2*z1
    a3=a3-k2*a1
    print(x1,' ',y1,' ',z1, "|", a1)
    print(0 ,' ',y2,' ',z2, "|", a2)
    print(0 ,' ',y3,' ',z3, "|", a3)
    print()

if y2==0:
    y2,y3=y3,y2#swapping second row with the third row if the second element of the second row is zero.
    z2, z3 = z3, z2
    a2, a3 = a3, a2

if y2!=0:
    k3 = y3/y2
    z3= z3-k3*z2
    a3= a3-k3*a2
    print(x1,' ',y1,' ',z1, "|", a1)
    print(0 ,' ',y2,' ',z2, "|", a2)
    print(0 ,' ',0 ,' ',z3, "|", a3)
    print()

if z3!=0:# checking whether the last element of the third row is zero or not to use it for making other elements zero.
    k4 = z2/z3
    k5 = z1/z3
    a1=a1-k5*a3
    a2 = a2-k4*a3
    print(x1,' ',y1,' ',0,"|", a1)
    print(0 ,' ',y2,' ',0, "|", a2)
    print(0 ,' ',0 ,' ',z3, "|", a3)
    print()

if y2!=0: # checking whether subtraction is possible or not.
    k6=y1/y2
    a1=a1-k6*a2
    print(x1,' ',0,' ',0,"|", a1)
    print(0 ,' ',y2,' ',0, "|", a2)
    print(0 ,' ',0 ,' ',z3, "|", a3)
    print()


a1 = a1/x1
a2 = a2/y2
a3 = a3/z3
# printing the final required matrix and the values
# do not that final matrix printed may be consistent or inconsistent do check it properly.
print(1, ' ', 0, ' ', 0, "|", a1)
print(0, ' ', 1, ' ', 0, "|", a2)
print(0, ' ', 0, ' ', 1, "|", a3)
print()

#printing the final values of x ,y and z
print("x=",a1)
print("y=",a2)
print("z=",a3)

