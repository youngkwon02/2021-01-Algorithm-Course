import random


def print_matrix(matrix):
  for row in matrix:
    print(row)


def matrix_multiplication(a, b):
  a_row = len(a)
  a_col = len(a[0])
  b_row = len(b)
  b_col = len(b[0])
  
  if a_col != b_row:
    print("incompatible dimensions")
    return -1
  
  c = [[0 for i in range(b_col)] for i in range(a_row)]
  
  for i in range(a_row):
    for k in range(b_col):
      for j in range(0, a_col):
        c[i][k] += a[i][j]*b[j][k]
        
  return c


def print_optimal_chain_order(div_k, num):
  order = ""
  
  for index in range(1, div_k+1):
    if index == 1:
      order+= "( "
    order+=("A" + str(index) + " ")
    if index == div_k:
      order+= ")"
      
  for index in range(div_k+1, num):
    if index == div_k+1:
      order+= "( "
    order += ("A"+ str(index) + " ")
    if index == num-1:
      order+= ")"
  
  print("\nOptimal chain order : ", order)
  

def get_min_computation(dimensions):
  div_k = 0
  num = len(dimensions)
  m = [[0 for i in range(num)] for i in range(num)]
  for index in range(2, num):
    for i in range(1, (num+1)-index):
      j = i + index - 1
      m[i][j] = float('inf')
      for k in range(i, j):
        val = m[i][k] + m[k+1][j] + (dimensions[i-1]*dimensions[k]*dimensions[j])
        if val < m[i][j]:
          m[i][j] = val
          if i == 1 and j == num-1:
            div_k = k
  return div_k, m[1][num-1]


def main():
  dimensions=[5,3,7,10]
  print("\nDimensions: ", dimensions)
  num = len(dimensions)
  matricis = []
  for i in range(num - 1):
    matrix = [[random.randint(1, 6) for index in range(dimensions[i+1])] for index in range(dimensions[i])]
    matricis.append(matrix)
    print("\nA"+str(i+1),"=", end="")
    for row in matrix:
      print("\t",row)
  
  div_k, min_computation = get_min_computation(dimensions)
  
  if div_k == 1:
    result = matrix_multiplication(matricis[1], matricis[2])
    result = matrix_multiplication(matricis[0], result)
  
  if div_k == 2:
    result = matrix_multiplication(matricis[0], matricis[1])
    result = matrix_multiplication(result, matricis[2])
  print("\nOutput matrix : ")
  print_matrix(result)
  print_optimal_chain_order(div_k, num)
  print("\nThe minimum number of computations : ", min_computation)\

  
if __name__ == "__main__":
    main()