
def countOnes3(hdata, a, b, c):
    suma = 0
    if hdata[a-1] == '1':
        suma += 1
    if hdata[b-1] == '1':
        suma += 1
    if hdata[c-1] == '1':
        suma += 1
    return suma

def countOnes4(hdata, a, b, c, d):
    suma = 0
    if hdata[a-1] == '1':
        suma += 1
    if hdata[b-1] == '1':
        suma += 1
    if hdata[c-1] == '1':
        suma += 1
    if hdata[d-1] == '1':
        suma += 1    
    return suma

def generate(data):#(1,3,5,7), (2,3,6,7), (4,5,6,7)
    hdata = 'P' + 'P' + data[0] + 'P' + data[1] + data[2] + data[3]
    if countOnes3(hdata, 3, 5, 7) % 2 == 0:
        p1 = '0'
    else:
        p1 = '1'
    if countOnes3(hdata, 3, 6, 7) % 2 == 0:
        p2 = '0'
    else:
        p2 = '1'
    if countOnes3(hdata, 5, 6, 7) % 2 == 0:
        p3 = '0'
    else:
        p3 = '1'
        
    realData = p1 + p2 + data[0] + p3 + data[1] + data[2] + data[3]
    return realData

def correct(hdata):#(1,3,5,7), (2,3,6,7), (4,5,6,7)
    #find error
    if countOnes4(hdata, 1, 3, 5, 7) % 2 == 0:
        c1 = 0
    else:
        c1 = 1
    if countOnes4(hdata, 2, 3, 6, 7) % 2 == 0:
        c2 = 0
    else:
        c2 = 1
    if countOnes4(hdata, 4, 5, 6, 7) % 2 == 0:
        c3 = 0
    else:
        c3 = 1
    
    errorPosition = c3 * 2**2 + c2 * 2**1 + c1 * 2**0
    #correct data
    if hdata[errorPosition-1] == '1':
        correctedData = hdata[:errorPosition-1] + '0' + hdata[errorPosition:]
    else:
        correctedData = hdata[:errorPosition-1] + '1' + hdata[errorPosition:]  
    
    #intented message
    realMessage = correctedData[2] + correctedData[4] + correctedData[5] + correctedData[6]
    toReturn = str(errorPosition) + ',' + str(correctedData) + ',' + realMessage 

    return toReturn
    
    

    pass