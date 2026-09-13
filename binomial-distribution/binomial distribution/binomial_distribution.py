import math

def povrh(n,k):#comb, combination primjenjena matematika prvi broj je onaj dolje
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    

successRate = float(input('Success rate (0 - 1.0): '))
successTimes = int(input('How many times did it succeed: '))
allTimes = int(input('How many times did it run: '))

chancesForThat = povrh(allTimes, successTimes) * (successRate**successTimes) * ((1 - successRate)**(allTimes - successTimes))
print(chancesForThat)
posto = chancesForThat * 100
posto = "{:.5f}".format(posto)
print(f'{posto}%')

