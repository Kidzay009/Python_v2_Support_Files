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
    prime = True

    if choice_Prim == 1:
        prime = False
        print(prime)

    elif choice_Prim == 2:
        prime = True
        print(prime)
    
    else:
        for i in range(2,choice_Prim):

            if choice_Prim % i == 0:
                prime = False
                break

            else:
                prime = True
            
        print(prime)

if choice_M == 2:
    choice_PrimRS =  int(input("Geez Choose your first number?!?!"))
    choice_PrimRE = int(input("better not be that long.. whats the second?"))
    choice_Range = range(choice_PrimRS,choice_PrimRE + 1)
    range_list = []
    prime = True
    for i in choice_Range:
        if i == 1:
            prime = False
    
        elif i == 2:
            prime = True

        elif i < 0:
            prime = False
        
        else:
            for divisor in range(2, i):
    
                if i % divisor == 0:
                    prime = False
                    break
    
                else:
                    prime = True

        if prime == True:
            range_list.append(i)

print(range_list)