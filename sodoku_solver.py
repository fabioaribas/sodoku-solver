M = [
[0,0,3, 0,0,0, 5,0,0],
[0,0,0, 1,2,8, 0,0,0],
[2,0,0, 0,0,0, 0,0,6],
[0,3,0, 5,0,9, 0,1,0],
[0,6,0, 0,8,0, 0,4,0],
[0,9,0, 3,0,7, 0,2,0],
[4,0,0, 0,0,0, 0,0,9],
[0,0,0, 9,1,6, 0,0,0],
[0,0,6, 0,0,0, 2,0,0]
]


def startPos(numBlock):
	#9x9 matrix is divided into 9 blocks (3x3) from 0 to 8
	iPos = (numBlock // 3)*3
	jPos = (numBlock * 3) % 6
	vector = [iPos,jPos]
	return(vector)

def retInitValues(numBlock):
	initValues = []
	startp = startPos(numBlock)
	for i in range(startp[0], startp[0]+3):
		for j in range(startp[1], startp[1]+3):
			if (M[i][j] != 0):
				initValues = initValues + [M[i][j]]
	return initValues

def retValues(numBlock):
	vinit = retInitValues(numBlock)
	vret = []
	for k in range(1,10):
		if not(k in vinit):
			vret = vret + [k]
	return vret

def retLineValues(numLine):
	vRes = [1,2,3,4,5,6,7,8,9]
	for j in range(0,9):
		if (M[numLine][j] != 0):
			vRes.remove(M[numLine][j])
	return vRes

def retColValues(numCol):
	vRes = [1,2,3,4,5,6,7,8,9]
	for i in range(0,9):
		if (M[i][numCol] != 0):
			vRes.remove(M[i][numCol])
	return vRes

def listsIntersect(a,b):
	return list(set(a).intersection(b))

def lists3Intersect(a,b,c):
	return listsIntersect( listsIntersect(a,b), listsIntersect(b,c) )

def simpleSolveBlock(numBlock):
        startp = startPos(numBlock)
        si = startp[0]
        sj = startp[1]
        updated = False
        blockv = retValues(numBlock)
        for i in range(si, si+3):
                reti = retLineValues(i)
                for j in range(sj, sj+3):

                        if (M[i][j] == 0):
                                retj = retColValues(j)
                                values = lists3Intersect(reti,retj,blockv)
                                if (len(values)==1):
                                        #print("i:%d j:%d %s (UPDATED)" % (i,j,str(values)))
                                        M[i][j] = values[0]
                                        updated = True
                                #else:
                                        #print("i:%d j:%d %s" % (i,j,str(values)))
        return updated

def solveBlocks():
	updated = False
	for k in range(0,9):
		if (simpleSolveBlock(k) == True):
			updated = True
	return updated

def printMatrix():
        for i in range(0,9):
                for j in range(0,9):
                        if (j!=8):
                                print("%d" % M[i][j], end = ' ')
                        else:
                                print("%d" % M[i][j])

#start
print('---')
printMatrix()
print('---')
retUpdated = solveBlocks()
while (retUpdated):
        retUpdated = solveBlocks()

print('---')
printMatrix()
print('---')

