def reduceFour(n):
    if n == 4:
        return str(n -1) 
    else:
        return str(n)
    

t = int(input())

for i in range(0, t):
    numStr = input()
    num = int(numStr)
    numList = []
    newNumStr = ''
    for digit in numStr:
        numList.append(int(digit))
    
    numList = map(reduceFour, numList)
    
    newNumStr = newNumStr.join(numList)
    #print(newNumStr)
    newNumInt = int(newNumStr)
    print('Case #'+ str(i+1) + ':', newNumInt, num - newNumInt)