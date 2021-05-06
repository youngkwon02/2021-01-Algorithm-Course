input_word = input("Enter a word for check palindrome: ")
length = len(input_word)
check_result = "palindrome"

for i in range(0, length // 2):
    head = i
    tail = (length - 1) - i
    if(input_word[head] != input_word[tail]):
        check_result = "not palindrome"
        break
    
print("The input word is", check_result)