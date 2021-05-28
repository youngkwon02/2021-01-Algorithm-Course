items = [
  {"item": 1, "weight": 6, "value":60},
  {"item": 2, "weight": 10, "value":20},
  {"item": 3, "weight": 3, "value":12},
  {"item": 4, "weight": 5, "value":80},
  {"item": 5, "weight": 1, "value":30},
  {"item": 6, "weight": 3, "value":60},
]


def get_vpw(item):
  return item.get("value")/item.get("weight")


def sort_by_vpw():
  for i in range(0, len(items)):
    for k in range(i + 1, len(items)):
      if get_vpw(items[i]) < get_vpw(items[k]):
        items[i], items[k] = items[k], items[i]
        
        
def fill_knapsack(capacity):
  knapsack = []
  for item in items:
    if capacity == 0:
      break
    if item.get("weight") > capacity:
      fraction = capacity / item.get("weight")
      item["fraction"] = fraction
      knapsack.append(item)
      capacity -= item.get("weight") / fraction
      break
    item["fraction"] = 1
    knapsack.append(item)
    capacity -= item.get("weight")
  return knapsack
        
        
def print_total_value(knapsack):
  total_value = 0
  for item in knapsack:
    total_value += item.get("value") * item.get("fraction")
  print("\n* Maximum value: ", int(total_value))


def print_knapsack(knapsack):
  print("\n<Associated Items>")
  for item in knapsack:
    print(item)

        
def main():
  sort_by_vpw()
  knapsack = fill_knapsack(capacity=16)
  print_knapsack(knapsack)
  print_total_value(knapsack)
  
  
if __name__ == "__main__":
    main()