matrix1 = []
matrix2 = []

row1 = int(input("Enter number of rows: "))
col1 = int(input("Enter number of columns: "))


for i in range(row1):  
    row = []
    for j  in range(col1):
        values = int(input("Enter element: "))
        row.append(values)
    
    matrix1.append(row)


for i in matrix1:
    print(i)


row2 = int(input("Enter number of rows: "))
col2 = int(input("Enter number of columns: "))


for i in range(row2):
    row = []
    for j  in range(col2):
        values = int(input("Enter element: "))
        row.append(values)
    
    matrix2.append(row)


for i in matrix2:
    print(i)


def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def subtract_matrices(matrix1, matrix2):   
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result

def multiply_matrices(matrix1, matrix2):    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
        result.append(row)
    
    return result

operations = input("Add(1), Subtract(2) or Multiply(3) Matrices??")

if(operations == "1"):
    total = add_matrices(matrix1, matrix2)
elif(operations == "2"):
    total = subtract_matrices(matrix1, matrix2)
elif(operations == "3"):
    total = multiply_matrices(matrix1, matrix2)

for i in total:
    print(i) 
