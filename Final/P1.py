def LCS_Length(X, Y):
  m = len(X)
  n = len(Y)
  b = [['0' for col in range(n+1)] for row in range(m+1)]
  c = [[0 for col in range(n+1)] for row in range(m+1)]
  for i in range(1, m+1):
    c[i][0] = 0
  for j in range(0, n+1):
    c[0][j] = 0
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
        b[i][j] = "↖"
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        b[i][j] = "↑"
      else:
        c[i][j] = c[i][j-1]
        b[i][j] = "←"
  return c, b


def Print_LCS(b, X, i, j):
  if i == 0 or j == 0:
    return
  if b[i][j] == "↖":
    Print_LCS(b, X, i-1, j-1)
    print(X[i-1],end='')
  elif b[i][j] == "↑":
    Print_LCS(b, X, i-1, j)
  else:
    Print_LCS(b, X, i, j-1)


def main():
  X = ["A", "B", "C", "B", "D", "A", "B"]
  Y = ["B", "D", "C", "A", "B", "A"]
  c, b = LCS_Length(X, Y)
  print("LCS : ", end='')
  Print_LCS(b, X, len(X), len(Y))
  print("\nThe length of LCS: ", c[len(X)][len(Y)])


if __name__ == "__main__":
    main()