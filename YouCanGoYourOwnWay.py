t = int(input())
for i in range(0,t):
    nx = 0
    ny = 0

    lx = 0
    ly = 0
    n = int(input())
    lPath = input()
    nPath = ''
    direcIndex = 0
    removedPath = ''
    #print('nx: '+ str(nx)  , 'ny: '+ str(ny))
    while direcIndex < len(lPath):
        # during cross over change path  otherwise follow same path   but cross over shoudn't be happening at dead end
        if nx == lx and ny == ly and (nx != n-1 and ny != n-1) : 
            if lPath[direcIndex] == 'E':
                nPath += 'S'
                lx+=1
                ny+=1
            else :
                nPath += 'E' 
                ly+=1
                nx+=1
            direcIndex+=1 
        elif nx == lx and ny == ly and(nx == n-1 or ny == n-1) :
            if nPath[direcIndex-1] == 'E':
                nx -=1
            else :
                ny -=1
            removedPath += nPath[-1]
            nPath  = nPath[:-1]
            
        else:
            # calutate coordinate for nadeem's Path and follow lydia's previous
            if lPath[direcIndex - 1 ] == 'E':
                nPath += 'E'
                nx+=1
            else :
                nPath += 'S'
                ny+=1 
            # calutate coordinate for Lydia's Path
            if lPath[direcIndex] == 'E':
                lx+=1
            else :
                ly+=1
            direcIndex+=1
        #print('nx: '+ str(nx)  , 'ny: '+ str(ny))
        #print('nPath: ', nPath, 'lPath: '+ lPath, 'removedPath: ' + removedPath)   
    print('Case #'+str(i+1)+ ':',nPath + removedPath, len(nPath + removedPath))
    #print("Case #{}: {}".format(i+1, nPath + removedPath))