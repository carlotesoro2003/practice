import cmath

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c= int(input("Enter c: "))

#discriminant (b2- 4ac)
d = (b**2) - (4*a*c)


#calculation of whole formula 
result1 = (-b + cmath.sqrt(d)) / (2*a)
result2 = (-b - cmath.sqrt(d)) / (2*a)

print("Solution: {} and {}".format(result1, result2))

