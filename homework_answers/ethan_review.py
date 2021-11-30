def print_list(my_list):
    # print each item in my_list 
    for item in my_list: 
        print(item)
    
def product(a, b): 
    # return a x b 
    return a * b 
    
import random
 
def generate_random(a, b): 
    return random.randrange(a, b)
    
def say_hi():
    # ask user for their name 
    name = input("What is your name? ")
    #say hi <name> to that user 
    print(f"hello {name}")
    
     
lst = [1, 2, 3, 4, 5, "Hello"]

#print_list(lst)

x = generate_random(1, 100)

say_hi()