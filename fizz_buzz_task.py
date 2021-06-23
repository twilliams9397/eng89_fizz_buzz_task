a = int(input("What number would you like to substitute for Fizz?  "))
b = int(input("What number would you like to substitute for Buzz?  "))

for i in range (100):
    if i % a == 0 and i % b == 0:
        i = "FizzBuzz"
        print(i)
    elif i % a == 0:
        i = "Fizz"
        print(i)
    elif i % b == 0:
        i = "Buzz"
        print(i)
    else:
        print(i)