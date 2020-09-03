# In this program the user chooses if he wants to know the fibonacci sequence, abundant number or both given
# how many rounds he wants the program to run(fibonacci) or a max number(abundant).

choice_input = input("Input f|a|b (fibonacci, abundant or both): ", )

# Variables

fib_int_one = 0
fib_int_two = 1
fib_int_three = 0
ab_counter = 0

# Fibonacci sequence

if choice_input == "f":
    fib_input = int(input("Input the length of the sequence: ", ))

    print("Fibonacci Sequence:")
    print("-------------------")
    print(fib_int_one)
    print(fib_int_two)

    for i in range(0, fib_input - 2):
        fib_int_three = fib_int_one + fib_int_two
        print(fib_int_three)
        fib_int_one = fib_int_two
        fib_int_two = fib_int_three

# Abundant numbers

elif choice_input == "a":
    ab_input = int(input("Input the max number to check: ", ))

    print("Fibonacci Sequence:")
    print("-------------------")

    for i in range(1, ab_input + 1):
        for x in range(1, i):
            if i % x == 0:
                ab_counter = ab_counter + x
        if ab_counter > i:
            print(i)
        ab_counter = 0

# Both Fibonacci and Abundant numbers

elif choice_input == "b":

    # Fibonacci sequence

    fib_input = int(input("Input the length of the sequence: ", ))

    print("Fibonacci Sequence:")
    print("-------------------")
    print(fib_int_one)
    print(fib_int_two)

    for i in range(0, fib_input - 2):
        fib_int_three = fib_int_one + fib_int_two
        print(fib_int_three)
        fib_int_one = fib_int_two
        fib_int_two = fib_int_three

    # Abundant number

    ab_input = int(input("Input the max number to check: ", ))

    print("Fibonacci Sequence:")
    print("-------------------")

    for i in range(1, ab_input + 1):
        for x in range(1, i):
            if i % x == 0:
                ab_counter = ab_counter + x
        if ab_counter > i:
            print(i)
        ab_counter = 0
