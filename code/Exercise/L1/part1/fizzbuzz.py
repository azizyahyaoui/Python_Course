# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz


num: int = 50

for num in range(1,num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz",num)
    elif num % 3 == 0:
        print("Fizz",num)
    elif num % 5 == 0:
        print("Buzz",num)
    else:
        print(num)
