import random
counter = 0
print("********Guess Game********")
print("Guess a number from the range of two numbers of your inputs")
name = str(input("Enter your name: "))
print(f"Welcome master {name}")
min = int(input("Enter first number: "))
max = int(input("Enter second number: "))
numbers = random.randint(min, max)
while (1):
    counter += 1
    guess = int(input("Guess a number: "))
    print(guess)
    if (guess == numbers):
        print(f"After {counter} times you won :))))) ")
        break
    elif (guess < numbers):
        print("no no no your number is smaller :()")
    elif (guess > numbers):
        print("shit your number is bigger ;( ")