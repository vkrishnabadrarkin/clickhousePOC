def g(i,j):
    return [j*1, j*2, j*3]
print([g(i,j) for i in range(5) for j in range(2)])