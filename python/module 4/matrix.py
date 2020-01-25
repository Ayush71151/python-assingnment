#matrix
matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print (matrix)

#matrix in 1 line
matrix1=[[j for j in range(5)]for i in range(5)]
print(matrix1)

#flatter list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix=[]
for sub_list in matrix:
    for var in sub_list:
       flatten_matrix.append(var)
print(flatten_matrix)

#flatten matrix in 1 line
flatten_matrix=[var for sub_list in matrix for var in sub_list]

#flatter in 2d
planets=[['mercury','venus','earth'],['mars','jupiter','saturn'],['uranus','neptune','pluto']]
faltten_planets=[planet for sublist in planets for planet in sublist if len(planet)<6]
print(faltten_planets)