# reading from text files
# writing to text files

# lets see how this is done
# open a file by creating a variable and assign the open() function to it

def reading():
    # ./ means that this file is in the same folder as our program file
    my_file = open("info", 'r')  # r stands for read mode, there is also w for write and some other ones

    print(my_file.readline())
    print(my_file.read())  # reads the entire contents of the file
    text = my_file.readlines()  # readlines() returns a list of strings with each string being a line from the file

    print(text)


def writing():

    # if we want to add new text to the end of a file we use the 'a' mode
    my_file = open("new_file.txt", 'w')  # we also have the 'w+' which opens a file for reading and writing

    my_file.writelines("Hello World this is a new file \n", )

    my_file.close()


def appending(lst):
    # if we want to add new text to the end of a file we use the 'a' mode
    my_file = open("new_file.txt", 'a')

    my_file.writelines(lst)

    my_file.close()
    
    
# context manager 
with open("filename") as file:
    file.readline()
    


strings = ["Hello \n", "I\n", "love\n", "Python!\n"]

writing()
appending(strings)
print("Wrote to file successfully")
