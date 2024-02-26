rows = int(input("Enter number of rows: "))

#reverse
for i in range(rows):
    for j in range(rows+i+1):
        print("", end=" ")
    for j in range(rows - i):
        print("*", end=" ")
    print()


#not reverse
for i in range(rows):
    for j in range(rows-i-1): #loop for spacing in rows
        print("", end=" ")
    for j in range(i + 1): #loop for printing stars 
        print("*", end=" ")
    print() 