from ctypes.wintypes import PINT


def isYearLeap(year):
    #
# coloca tu código aquí
#
    if year >= 1582:
        if year % 4 ==0:
            if year % 100 ==0:
                if year % 400 ==0:
                    return True
                else:
                    return False
            else: return True
        else:
            return False
    else:
        return None 

def daysInMonth(year,month):
    if isYearLeap(year) != None:    
        if month > 0 and month < 13: 
            if month %2 ==0 :
                if month == 4 or month == 6:
                    return 30
                elif month ==2 and isYearLeap(year) :
                    return 29
                elif month ==2 and not isYearLeap(year):
                    return 28
                else:
                    31
            else:
                if month == 9 or month == 11:
                    return 30
                else:
                    return 31
        else: 
            return None
    else:
        return None





def dayOfYear(year, month, day):
    #
# pon tu código nuevo aquí
#
    normalyy=[0,3,3,6,1,4,6,2,5,0,3,5]
    leapyy=[0,3,4,0,2,5,0,3,6,1,4,6]
    Day=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
    
    
    if isYearLeap(year):
        M=leapyy[month-1]
    else:
        M=normalyy[month-1]
    

    dd=(year-1)%7
    a=((year-1)//4-(3*((year-1)//100+1)//4))%7
    b=day%7
    r=(dd+a+M+b)%7
    
    print("dia del año: ",end="")
    return Day[r]
    


        


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

print("year","month","resutl")





testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

print(daysInMonth(1560,1))
print("2007 es bisiesto?:",isYearLeap(2007))


print(dayOfYear(1994, 8, 26))
print(dayOfYear(2013, 7, 11))