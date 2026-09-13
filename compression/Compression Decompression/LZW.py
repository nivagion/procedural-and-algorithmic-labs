#Lempel-Ziv-Welch
def compress(input_data):
    dictionary = {chr(i): i for i in range(256)} #makes dict with 256 ascii chars
    output = [] #list of codes
    current_string = input_data[0]
    
    for char in input_data[1:]:
        next = current_string + char
        if next in dictionary:
            current_string = next #if it is in already go next
        else:
            output.append(dictionary[current_string])
            dictionary[next] = len(dictionary) #add new sequence
            current_string = char
            
    output.append(dictionary[current_string])
    
    return output
        
        
        

def decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)} 
    output = '' 
    previous = compressed_data[0]
    output += dictionary[previous] #add first element
    for code in compressed_data[1:]: #loop through compressed data
        if code in dictionary:
            string = dictionary[code]       
        else:
            string = dictionary[previous] + dictionary[previous][0]
        output += string
        dictionary[len(dictionary)] = dictionary[previous] + string[0]
        previous = code
            
    return output
    