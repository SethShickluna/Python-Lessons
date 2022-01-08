    """
    Write a function which tells us if we should 
    sleep in. 
    
    We only sleep in, if we are on vacation or it is a weekend: 
    - vacation is a boolean value which indicates whether we are on vacation or not. 
    - day is the name of the day represented by a string
    
    Example sleep_in(False, "sunday") -> True
    """
def sleep_in(vacation: bool, day: str) -> bool:
    pass 


    """
    Write a function which returns the number of times that
    a character, c,  appears in a string, s.
    
    Example:
        count_chars('a', 'abracadabra') -> 5 
        count_chars('x', 'abracadabra') -> 0  
    """
def count_chars(c: str, s: str) -> int: 
    pass 


if __name__ == "__main__":
    print(sleep_in(False, "sunday"))
    print(sleep_in(True, "monday"))
    print(sleep_in(False, "friday"))