def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list = []
        matrix.append(list)
        for k in range(m):
            list.append(value)
    return matrix

result = get_matrix(5, 2, 15)

print(result)