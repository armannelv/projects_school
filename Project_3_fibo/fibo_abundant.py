choice_input = input("Input f|a|b (fibonacci, abundant or both): ",)

fib_int_one = 0
fib_int_two = 1
fib_int_three = 0

if choice_input == "f":
    fib_input = int(input("Input the length of the sequence: ", ))
    print(fib_int_one)
    print(fib_int_two)
    for i in range(0, fib_input - 2):
        fib_int_three = fib_int_one + fib_int_two
        print(fib_int_three)
        fib_int_one = fib_int_two
        fib_int_two = fib_int_three

#elif choice_input == "a":

#elif choice_input == "b":

