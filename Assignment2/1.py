input_n = int(input("Enter a number n: "))
k = 1 # Because K is positive

while True:
    if pow(2, k) <= input_n:
        k = k + 1
    else:
        if k > 1:
            k = k - 1
            print("The largest K is", k)
        else:
            print("There is no positive integer K which is satisfying the equation.")
        break



    