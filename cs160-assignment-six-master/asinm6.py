def add (fnum,lnum):
#Function for an addition of two integers
	sumnum=fnum+lnum
	return sumnum
	#The integers will add together

def sub (fnum2,lnum2):
#Function for a subtraction of two [integers]
	difnum=fnum2-lnum2
	return difnum
	#The integers will subtract one another

def mult (fnum3,lnum3):
#Function for a multiplication function
	pronum=fnum3*lnum3
	return pronum
	#the integers should be multiplied

def square (fnum4):
#Function for a square of an integer
	sqnum=fnum4**2
	return sqnum
	#the  integer will be squared

def f1 (fnum1, fnum2):
#function org minus 5
	return sub(add(fnum1,fnum2), 5)
	#Return Func	

def f2 (fnum1,fnum2):
#Func for a negative versh of the sub func	
	return mult(sub(fnum1,fnum2), -1)
	#Return Func

def f3 (fnum1):
#Func for neg version of the square func
	return mult(square(fnum1), -1)
	#Return Func

def f4 (fnum1,fnum2):
#Func for polynomial w vars
	return add(f3(fnum1),fnum2)
	#Return Func

def f5 (fnum1):
#Func for polynomial complex
	return add((mult((square(fnum1)), 2)),(add((mult(fnum1, 3)), 5)))
	#Return Func

def f6 (fnum1):
#Func for quad exp poly
	return square(square(fnum1))
	#return Func
