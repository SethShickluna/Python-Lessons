# lesson 2

completed = True # set to false to use the calculator

while not completed: # while completed == False

    # get string from user input
    user_input = input("Please input 2 numbers and an operation or type done to quit: ")

    if user_input.lower() == "done":
        completed = True
        break
        
    # operators[number_1, operation, number_2]
    operators = user_input.split(' ')

    # do we all know whats going on here  # and
    number_1 = 0
    number_2 = 0

    calculated = True

    if operators[0].isdigit() and operators[2].isdigit():
        number_1 = int(operators[0])
        number_2 = int(operators[2])
    else:
        print("Invalid number inputs!")
        calculated = False

    operation = operators[1]

    result = 0

    if operation == "+":
        result = number_1 + number_2
    elif operation == "-":
        result = number_1 - number_2
    elif operation == "*":
        result = number_1 * number_2
    elif operation == "/":
        result = number_1 / number_2
    else:
        print("Invalid operator, we cannot do math with this")
        calculated = False

    if calculated:
        print(result)


number = 1

while number < 5:
    print(number)
    number += 1

print("all done")


for number in range(10):  #starts at 0, 1, ...
    print(number)





















