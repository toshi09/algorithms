def unique(input_string):
    sort_input = sorted(input_string)
    unique_found = True

    for idx in range(len(sort_input)-1):
        if sort_input[idx] == sort_input[idx + 1]:
            unique_found = False
        else:
            continue
            
    return(unique_found)



unique('ashwani')
