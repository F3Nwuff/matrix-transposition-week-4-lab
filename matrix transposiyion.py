x = eval(input("please enter a list here in [] form and sepperated by coma:"))
result =[]
for r in range(len(x[0])):
    matrix = []
    for c in range(len(x)):
        matrix.append(x[c][r])
    result.append(matrix)
print(result)