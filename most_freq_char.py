def max(inp_string):
    sort_string = sorted(inp_string)
    count = 0
    max_freq = 0
    last_freq_char = ''
    for index in range(len(sort_string)-1):
        if sort_string[index] == sort_string[index+1]:
            count = count + 1


        else:
            if count > max_freq:
                max_freq = count + 1
                last_freq_char = sort_string[index]
                count = 0
    return last_freq_char,max_freq

print(max('vikhyati'))

