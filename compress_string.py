'''program to perform basing string compresion using the counts of repeated characters ex- aaabbbaaa would become a3b3a3'''
def compress(inp_string):
    count = 1
    compressed_string = ''
    for index in range(len(inp_string)-1):
        if inp_string[index] == inp_string[index+1]:
            count = count + 1
        else:
            compressed_string = compressed_string + inp_string[index] + str(count)
            count = 1
    else:
        if len(compressed_string) >= len(inp_string):
            compressed_string = inp_string

    return compressed_string




print(compress('vvvvvvvvvvvvviikkhhyati'))




