def FirstReverse(str): 
    string_length = len(str)
    reversed_string = ""
    while (string_length > 0):
        reversed_string = reversed_string + str[string_length - 1]
        string_length = string_length - 1
    return reversed_string
    
# keep this function call here  
print FirstReverse(raw_input())
