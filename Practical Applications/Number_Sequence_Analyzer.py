options = ["0. Generate a Fibonacci sequence","1. Check if a number is prime","2. Display all prime numbers in a range","3. Generate a multiplication table","4. Calculate a factorial","5. Run a Collatz sequence","6. Exit the program"]

for i in options:
    print(i)

choice_M = 0
choice_Fib = 0
first_Fib = 0
second_Fib = 1

while choice_M <= 6 or choice_M >= 0:
    choice_M = int(input("what would you like to choose? enter 0-6 "))
    if choice_M == 0:
        print("Let's do a Fibonacci!")
        break
    elif choice_M == 1:
        print("You really need to know if a number is prime or not?! Fine...")
        break
    elif choice_M == 2:
        print("You really are needy aren't you? Lets see them all!")
        break
    elif choice_M == 3:
        print("What if I dont want to multiply?!? HUH?!?!")
        break
    elif choice_M == 4:
        print("What even is a Tacforial?")
        break
    elif choice_M == 5:
        print("I'm pretty sure you just made that up just now")
        break
    else:
         print("THATS NOT IN THE LIST BOZO!!!")
    

if choice_M == 0:
    choice_Fib = int(input("how many loops? "))
    loops_Fib = choice_Fib
    choice_Fib = 0
    
    while choice_Fib < loops_Fib:

        print(first_Fib)

        first_Fib, second_Fib = second_Fib, first_Fib + second_Fib
        
        choice_Fib += 1

elif choice_M == 1:
    choice_Prim = int(input("What stupid number can you not check yourself? "))