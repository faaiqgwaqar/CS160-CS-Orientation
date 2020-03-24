#You may be wondering as a TA, what this giant block of commentary is
#I Would just like to vent some of my frustrations with the assignment
#Number 1: Why are the function names so unreasonably long and complicated
#Number 2: Why are 4 and 5 the same (Basically)

def addOne(num1,num2,num3):
#takes a list of intergers under the function
	num1 = int(num1)
	num2 = int(num2)
	num3 = int(num3)
	myList =[num1,num2,num3]
	myList[0] = myList[0]+1
	myList[1] = myList[1]+1
	myList[2] = myList[2]+1
	# Defines that each value will be added to One
	return myList
	# Returns the list of integers, only now added by one

def rawGradeToLetter(perc):
#defines a function in which a percent can be recieved	
	score = float(perc)
	#stores the percent as a float value
	if score >= 90:
		agrade = str('A')
		return agrade
	elif 80 <= score <90:
		bgrade = str('B')
		return bgrade
	elif 70 <= score <80:
		cgrade = str('C')
		return cgrade
	elif 60 <= score < 70:
		dgrade = str('D')
		return dgrade
	else:
		fgrade = str('F')
		return fgrade
	#Prints the desired results

def convertRawsToLetters(perc1,perc2,perc3):
	perc1 = float(perc1)
	perc2 = float(perc2)
	perc3 = float(perc3)
	#defined percentages as floats to store decimals
	rawgr = [perc1,perc2,perc3]
	if rawgr[0] >= 90:
		agrade=str('A')
		rawgr[0]=agrade
	elif 80<=rawgr[0]<90:
		bgrade=str('B')
		rawgr[0]=bgrade
	elif 70<=rawgr[0]<80:
		cgrade=str('C')
		rawgr[0]=cgrade
	elif 60<=rawgr[0]<70:
		dgrade=str('D')
		rawgr[0]=dgrade
	else:
		fgrade=str('F')
		rawgr[0]=fgrade
	if rawgr[1] >= 90:
		agrade=str('A')
		rawgr[1]=agrade
	elif 80<=rawgr[1]<90:
		bgrade=str('B')
		rawgr[1]=bgrade
	elif 70<=rawgr[1]<80:
		cgrade=str('C')
		rawgr[1]=cgrade
	elif 60<=rawgr[1]<70:
		dgrade=str('D')
		rawgr[1]=dgrade
	else:
		fgrade=str('F')
		rawgr[1]=fgrade
	if rawgr[2] >= 90:
		agrade=str('A')
		rawgr[2]=agrade
	elif 80<=rawgr[2]<90:
		bgrade=str('B')
		rawgr[2]=bgrade
	elif 70<=rawgr[2]<80:
		cgrade=str('C')
		rawgr[2]=cgrade
	elif 60<=rawgr[2]<70:
		dgrade=str('D')
		rawgr[2]=dgrade
	else:
		fgrade=str('F')
		rawgr[2]=fgrade
	return rawgr

def ouncesToCups(oz1,oz2,oz3):
	oz1 = float(oz1)
	oz2 = float(oz2)
	oz3 = float(oz3)
	ozlis = [oz1,oz2,oz3]
	
	print("This Program will convert your Ounce values to Cups")
	ozlis[0] = ozlis[0]/8
	ozlis[1] = ozlis[1]/8
	ozlis[2] = ozlis[2]/8
	return ozlis

def glassOfWater(oz1,oz2,oz3):
	oz1 = float(oz1)
	oz2 = float(oz2)
	oz3 = float(oz3)
	cuplis = [oz1,oz2,oz3]

	print("This program will convert your Ounce Values to GLASSES OF WATER")
	#You may be wondering, why the prints? Well, the last two functions are the same, and it is REALLY bothering me. So, I need a differentiator
	cuplis[0] = cuplis[0]/8
	cuplis[1] = cuplis[1]/8
	cuplis[2] = cuplis[2]/8
	return cuplis

def hydrated(ozwa):
	hyde = float(ozwa)
	if hyde >= 8:
		unep = str('Hydrated')
		return unep
	else:
		inep = str('Not Hydrated')
		return inep

def waterNeeded(ozwa):
	hyde = float(ozwa)
	if hyde >= 8:
		unep =  str('Hydrated')
		return unep
	else:
		hyde = 8-hyde
		print("you need this many more cups to be hydrated:")
		return hyde
