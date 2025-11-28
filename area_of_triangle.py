"""Find the area of a triangle when all sides are known"""
a=float(input("enter side 1"))
b=float(input("enter side 2"))
c=float(input("enter side 3"))
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area of triangle is ", round(area,2))