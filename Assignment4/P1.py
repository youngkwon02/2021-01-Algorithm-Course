def fibonacci(input, holder):
    if input == 1 or input == 2:
      return 1
    
    if input in holder:
      return holder[input]
    holder[input] = fibonacci(input-1, holder) + fibonacci(input-2, holder)
    return holder[input]


def main():
  holder = {}
  output = fibonacci(input=5, holder=holder)
  print("n = 5 -> Output : ", output)
  holder = {}
  output = fibonacci(input=10, holder=holder)
  print("n = 10 -> Output : ", output)
  

if __name__ == "__main__":
    main()