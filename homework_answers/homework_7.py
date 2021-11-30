########################################################################################
# todo app                                                                             #
# user can select add, delete or view                                                  #
# add, prompts the user for input, which then gets appended to the file                #
# delete prints out each item with a number beside it, then gets deleted from the file #
# view, prints out each item in the list to the user                                   #
########################################################################################

def append_but_better(): 
    with open("list.txt") as file: 
        pass 


def append(): 
    file = open('list.txt','a')
    item = input('add an item: ') +'\n'
    file.write(item)
    file.close()

def delete(): 
    file = open('list.txt','r')
    lines = file.readlines()
    file.close()
    
    for line_num, line in enumerate(lines): 
        print(f"{line_num + 1}. {line}")
    
    choice = input("Which item would you like to delete? (type nvm to stop) \n")
    
    delete = 0
    
    if choice != 'nvm': 
        delete = int(choice) - 1
        
    with open('list.txt', 'w') as file: 
        for line_num, line in enumerate(lines): 
            if line_num != delete: 
                file.write(line)
        
    
def view():
    file = open('list.txt','r')
    print(file.read())

def main():
    while True:
        choice = input('[add] [view] [delete] [quit] \n')
        
        if choice == 'quit': 
            break
        elif choice == 'add':
            append()
        elif choice == 'view':
            view()
        elif choice == 'delete':
            delete()
        else: 
            print('Sorry, please try another command!')
        
        
main() 
