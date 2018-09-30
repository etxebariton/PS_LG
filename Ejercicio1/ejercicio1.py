#
# Given a list of numbers, the function returns
# for each number, if it's perfecto, abundante or defectivo
#
def myFunction(myList):
    i=0
    myMap={}
    while i<len(myList):
        n = myList[i]
        if n>0 and type(n)==int:
            auxList = []
            for j in range(1,n):
                if (n%j == 0):
                    auxList.append(j)    
            v=0
            k=0
            while k<len(auxList):   
                v = auxList[k]+v
                k=k+1
            if (v == n):
                myMap[n] = 'perfecto'
            elif (v>n):
                myMap[n] = 'abundante'                
            else:
                myMap[n] = 'defectivo'            
        i=i+1
    return myMap
	
