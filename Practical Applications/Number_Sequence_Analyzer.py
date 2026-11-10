options = ["0. Generate a Fibonacci sequence","1. Check if a number is prime","2. Display all prime numbers in a range","3. Generate a multiplication table","4. Calculate a factorial","5. Run a Collatz sequence","6. Exit the program", "\n"]
choice_M = 0

while choice_M <= 6 or choice_M >= 0:
    choice_Fib = 0
    first_Fib = 0
    second_Fib = 1
    steps = 0
    for i in options:
        print(i)

    try:
        choice_M = int(input("what would you like to choose ONLY ENTER KEYPAD NUMBERS? enter 0-6 "))

    except ValueError:
        print("THATS NOT A NUMBER BOZO!!!","\n")
        continue

    if choice_M == 0:
        print("Let's do a Fibonacci!","\n")
        
    elif choice_M == 1:
        print("You really need to know if a number is prime or not?! Fine...","\n")
        
    elif choice_M == 2:
        print("You really are needy aren't you? Lets see them all!","\n")
        
    elif choice_M == 3:
        print("What if I dont want to multiply?!? HUH?!?!","\n")
        
    elif choice_M == 4:
        print("What even is a Tacforial?","\n")
        
    elif choice_M == 5:
        print("I'm pretty sure you just made that up just now","\n")
        
    elif choice_M == 6:
        print("I dont want to talk to YOU anyway!","\n")
        break
    else:
         print("THATS NOT IN THE LIST BOZO!!!","\n")

    if choice_M == 0:

        try:
            choice_Fib = int(input("how many loops? "))

        except ValueError:
            print("You really like to test my patience...","\n")
            continue

        loops_Fib = choice_Fib
        choice_Fib = 0
        Fib_list = []

        if loops_Fib < 0:
            print("How do you expect me to print that many loops?","\n")

        while choice_Fib < loops_Fib:

            Fib_list.append(first_Fib)

            first_Fib, second_Fib = second_Fib, first_Fib + second_Fib
        
            choice_Fib += 1

        print(Fib_list,"\n")

    elif choice_M == 1:

        try:
            choice_Prim = int(input("What stupid number can you not check yourself? "))

        except ValueError:
            print("Choose. a. NUMBER. ","\n")
            continue

        prime = True

        if choice_Prim <= 0: 
            print("im not doing that.","\n")
            continue

        elif choice_Prim == 1:
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
            
            print(prime,"\n")

    elif choice_M == 2:
        try:
            choice_PrimRS =  int(input("Geez Choose your first number?!?! "))
            choice_PrimRE = int(input("better not be that long.. whats the second? "))

        except ValueError:
            print("Are you joking with me? WHY DO YOU KEEP ENTERING WOR-","\n")
            continue

        choice_Range = range(choice_PrimRS,choice_PrimRE + 1)
        range_list = []
        prime = True

        if choice_PrimRE < choice_PrimRS:
            print("i h8te u...","\n")
            continue

        elif choice_PrimRE or choice_PrimRS < 0:
            print("get out with your NEGATIVE energy!","\n")
            continue

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

            print(range_list,"\n")

    elif choice_M == 3:

        try:
            choice_MT = int(input("What do you need to be multiplied idiot? "))
            choice_MTL = int(input("How long? if it's more than 10 ill get u. "))

        except ValueError:
            print("you know what the next time you enter a word i'm leaving...","\n")
            continue

        MTL_list = []

        if choice_MTL <= 0:
            print("are you stupid? you CANT HAVE NEGATIVE AMOUNTS!!","\n")
            continue

        for i in range(1,choice_MTL + 1):
            i *= choice_MT
            MTL_list.append(i)

        print(MTL_list,"\n")

    elif choice_M == 4:
        try:
            choice_Fact = int(input("What number do you need for the Tacforial? "))

        except ValueError:
            print("Im NOT joking don't test me!","\n")
            continue

        if choice_Fact < 0:
            print("NO NEGATIVES. I SAID NO NEGATIVES!!!","\n")

        for i in range (1, choice_Fact):
            choice_Fact *= i
        print(choice_Fact,"\n")

    elif choice_M == 5:

        try:
            choice_Coll = int(input("Lets run the Collapse! give me a POSITIVE number. "))

        except ValueError:
            print("DIEEEEEEE!!!","\n")
            continue

        if choice_Coll <= 0: 
            print("Nope...","\n")
            continue

        Coll_list = []
        steps = 0
        while choice_Coll != 1:
            steps += 1
            Coll_list.append(choice_Coll)

            if choice_Coll % 2 == 0:
                choice_Coll //= 2
            
            elif choice_Coll % 2 > 0:
                choice_Coll = (choice_Coll * 3) + 1

        Coll_list.append(1)
        print(Coll_list,"\n")
        print(f"it took {steps} steps...","\n")