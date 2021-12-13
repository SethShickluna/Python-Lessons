#files!!!!

# reading from text files 
# writing to text files 


def make_words(): 
    result = [] 
    with open("C:/Users/seths/Documents/tutoring/Python-Lessons/code/ethan/list.txt") as file: 
        
        for word in file.readlines(): 
            result.append(word.strip("\n"))
            
    return result 
        
    
# words = make_words() 

def write_words(text): 
    with open("C:/Users/seths/Documents/tutoring/Python-Lessons/code/ethan/list.txt", "a") as file: 
        file.write(text)


file_name = input("Please enter a file name: ")
      
try:
    with open("C:/Users/seths/Documents/tutoring/Python-Lessons/code/ethan/" + file_name + ".txt") as file:
        file.read() 
except FileNotFoundError:
    print("No file with this name found")


def main(): 
    while True: 
        text = input("Enter a word: ")
        
        if text != "stop":
            write_words(text + "\n")
        else: 
            break 
        
        
