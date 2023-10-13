x = float(input("enter a number : "))
y = float(input("enter another one : "))
if ( x >= 0 and y >= 0 ) or ( x <= 0 and y <= 0) :
    z = x
    x = y
    y = z
    print("the first number is : " , x)
    print("the second number is : " , y)
else :
    print ("the sum is : " , x + y)
    print ("and the multiplication is : ", x * y)