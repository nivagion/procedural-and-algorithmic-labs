import hamming74 as h74

whatMethod = input('hamming 7 4 - h74: ')

whatToDo = input('generate or correct - g/c: ')

if whatMethod == 'h74':
    if(whatToDo == 'g'):
        data = input('input 4 bits of data: ') 
        hdata = h74.generate(data)
        print(f'Generated hamming 7 4 data is: {hdata}') 
    else:
        data = input('input 7 bits of data: ')
        Correction = h74.correct(data)
        errorLoc, corrected, real4bits = Correction.split(',')
        print(f'Error is at position: {errorLoc}')
        print(f'Corrected h message is: {corrected}')
        print(f'Original message is: {real4bits}')
elif whatMethod == 'PLACEHOLDER': #reed solomon?
    pass
    