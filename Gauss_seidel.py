'''

Author-Pushkar Patel
Email-pushkar.umrao@gmail.com

Gauss-Seidel iteration calculator
instructions:
1. Input initial values of x y z seperated by a space
2. Enter precision you want after decimals
3. Enter x in terms of y and z in terms of computer expression
   ex: x=(2y-z)/2
        then enter (2*y-z)/2 as input
4. Enter y in terms of x and z
5. Enter z in terms of x and y
6. Press c for continue iteration and e for exit and press enter
suggestion: please rearrange and find expressions on paper for equation and then input

'''
x,y,z=map(float,input('Enter initial Values of x,y&z:').split())
prec=int(input('How many digits of precision are needed.'))
fx=input('Enter Expression for x:')
fy=input('Enter Expression for y:')
fz=input('Enter Expression for z:')
#p=10*prec

rnd=lambda v:round(v,prec)

def tc(x,y,z):
    return (rnd(x),rnd(y),rnd(z))
def iterate():
    global x
    global y
    global z
    x=eval(fx)
    y=eval(fy)
    z=eval(fz)


i=1
ctr=None
print('_'*30)
print('i |x      |y     |z     |')
print('_'*30)
while True :
    iterate()
    print(f'{i} |{round(x,prec)} |{round(y,prec)} |{round(z,prec)} |')
    print('_'*30,':c-Continue e-Exit:',end=' ')
    i+=1
    ctr=input()
    if ctr=='e' or ctr=='E':
        break
