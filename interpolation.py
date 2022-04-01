"""
Program to prove that polynomails are not very good for aproximating
Note: Sage is required to run the matrix part of this script
"""

matrix_values = matrix(QQ,11) #create 11x11 matrix


def f(x):
    return (1 / ( (25*x**2) +1))

#creating vector
function_values = vector(RR,11)
for k in range(0,11):
    entry = k*(0.2)-1
    function_values[k] = f(entry)
# Expected valuess: (0.0384615384615385, 0.0588235294117647, 0.100000000000000, 0.200000000000000, 0.500000000000000, 1.00000000000000, 0.500000000000000, 0.200000000000000, 0.100000000000000, 0.0588235294117647, 0.0384615384615385)


#inital values for computing function
count =0
power = 1
vector_count = 1
for i in range(-10,12,2):
    i = i/ 10
    function = 1 / (25* (i**2) +1)   #calculated (x,y) y part of function
    #print("This is i",i)
    #print(function)
    col=1
    power = 1


    for row in range(0,10,1):

        print("\n this is row: ",row)
        print(" \n this is col: ",col)

        matrix_values[count,col] = i**power #Raise x^ith power
        col = col + 1
        #print("\n")
        #print( matrix_values)
        power = power + 1
    count = count + 1

for k in range(0,11,1):
    matrix_values[k,0] = 1
    #change first col value to 1

print(matrix_values)
w = matrix_values \ function_values
#creates our 11th degree polynomail that we can use later plot with
def p(x):
    return(w[0]
           +w[1]*x
           +w[2]*x**2
           +w[3]*x**3
           +w[4]*x**4
           +w[5]*x**5
           +w[6]*x**6
           +w[7]*x**7
           +w[8]*x**8
           +w[9]*x**9
           +w[10]*x**10)


#ploting...
plot(p)
pl1 = plot(f,(-1,1),color='red')
pl2 = plot(p,(-1,1))
pl1 + pl2 #to overlap to the two grpahs 
