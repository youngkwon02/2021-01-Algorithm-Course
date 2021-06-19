import copy


MIN_INDEX = 0
MAX_INDEX = 3
g = 0


# Puzzle = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9, 10, 12, 'N'],
#   [13, 14, 11, 15]
# ]

Puzzle = [
  [10, 7, 3, 4],
  [5, 9, 'N', 11],
  [6, 1, 2, 8],
  [13, 14, 15, 12]
]


GOAL = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 'N']
]


Puzzle_stack = [Puzzle]


def move_puzzle(di, dk):
  puzzle_dup = copy.deepcopy(Puzzle)
  i,k =get_index_of_N(puzzle_dup)
  target_i = i + di
  target_k = k + dk
  puzzle_dup[i][k], puzzle_dup[target_i][target_k] = puzzle_dup[target_i][target_k], puzzle_dup[i][k]
  return puzzle_dup


def get_index_of_N(puzzle):
  for i in range(MAX_INDEX+1):
    for k in range(MAX_INDEX+1):
      if puzzle[i][k] == 'N':
        return i,k


def branch():
  branched_list = []
  i,k = get_index_of_N(Puzzle)
  if i == MIN_INDEX:
    if k == MIN_INDEX:
      branched_list.append(move_puzzle(1,0))
      branched_list.append(move_puzzle(0,1))
    elif k == MAX_INDEX:
      branched_list.append(move_puzzle(1,0))
      branched_list.append(move_puzzle(0,-1))
    else:
      branched_list.append(move_puzzle(1,0))
      branched_list.append(move_puzzle(0,1))
      branched_list.append(move_puzzle(0,-1))
  elif i == MAX_INDEX:
    if k == MIN_INDEX:
      branched_list.append(move_puzzle(-1,0))
      branched_list.append(move_puzzle(0,1))
    elif k == MAX_INDEX:
      branched_list.append(move_puzzle(-1,0))
      branched_list.append(move_puzzle(0,-1))
    else:
      branched_list.append(move_puzzle(-1,0))
      branched_list.append(move_puzzle(0,1))
      branched_list.append(move_puzzle(0,-1))
  else:
    if k == MIN_INDEX:
      branched_list.append(move_puzzle(1,0))
      branched_list.append(move_puzzle(-1,0))
      branched_list.append(move_puzzle(0,1))
    elif k == MAX_INDEX:
      branched_list.append(move_puzzle(1,0))
      branched_list.append(move_puzzle(-1,0))
      branched_list.append(move_puzzle(0,-1))
    else:
      branched_list.append(move_puzzle(1,0))
      branched_list.append(move_puzzle(-1,0))
      branched_list.append(move_puzzle(0,1))
      branched_list.append(move_puzzle(0,-1))
  return branched_list
    
      
def get_h(puzzle):
  h = 0
  for i in range(MAX_INDEX + 1):
    for k in range(MAX_INDEX + 1):
      if puzzle[i][k] != GOAL[i][k] and puzzle[i][k] != 'N':
        h += 1
  return h


def main():
  global Puzzle, GOAL, g
  iii = 0
  while True:
    iii+=1
    if Puzzle == GOAL:
      break
    g += 1
    h_list = []
    cost = []
    branched_list = branch()
    for index in range(len(branched_list)):
      if branched_list[index] in Puzzle_stack:
        h_list.append(float('INF'))
        cost.append(float('INF'))
        continue
      h = get_h(branched_list[index])
      h_list.append(h)
      cost.append(g + h)
      
    print("cost", cost)
    selected_index = cost.index(min(cost))
    print("𝑔(𝑥)=", g, ", h(𝑥)=", h_list[selected_index], ", total-cost C^(𝑥)=", cost[selected_index])
    Puzzle = branched_list[selected_index]
    for row in Puzzle:
      print(row)
    Puzzle_stack.append(Puzzle)
    
      
    flag = False
    for index in range(len(cost)):
      if cost[index] != float('INF'):
        break
      elif index == len(cost) - 1:
        flag = True
      else:
        pass
    if flag:
      break
    
    
    if iii > 10000:
      break
    
    
if __name__ == "__main__":
  main()