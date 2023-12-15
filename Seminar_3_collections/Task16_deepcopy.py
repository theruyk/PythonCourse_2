import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy () # создаст новый список с сылками на вложенные списки и 
#при изменении одного списка изменится и второй 
print (matrix, new_m, sep='\n')
matrix[0][1] = 555
print (matrix, new_m, sep= '\n')

print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix) # copy.deepcopy копирует все элементы вложенности 
#(Это будут два совершенно не связаных объекта)
print (matrix, new_m, sep='\n')
matrix[0][1] = 555
print (matrix, new_m, sep= '\n')