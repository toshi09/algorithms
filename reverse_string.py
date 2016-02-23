# program to find reverse of a string

def reverse(inp_string):
    rev_string = ''
    max_length = len(inp_string) - 1
    for index in range(len(inp_string)):
        rev_string = rev_string + inp_string[max_length]
        max_length = max_length - 1
    return rev_string


print(reverse('vikhyati'))