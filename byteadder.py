#This module calculates the addition of two binary numbers

#and gate
def and_gate(a,b):
	if a==1 and b==1:
		return 1
	else:
		return 0

#or gate
def or_gate(a,b):
	if a==0 and b==0:
		return 0
	else:
		return 1
        
#xor gate
def xor_gate(a,b):
	if (a==0 and b==0) or (a==1 and b==1):
		return 0
	else:
		return 1

def halfAdder(a,b):
	x = xor_gate(a,b)
	y = and_gate(a,b)
	return (x,y)

def fullAdder(a,b,c=0):
	sum1, c1 = halfAdder(a,b)
	sum2,c2 = halfAdder(sum1,c)
	return (sum2,or_gate(c1, c2))

def binaryAdder(a,b):

	
	c=0
	result=""
	for i in range(len(a)-1,-1,-1):
		summ,c= fullAdder(int(a[i]),int(b[i]),c)
		result+=str(summ)
		
	# Reversing a list using slicing technique 		
	result= result[::-1]
	return result
	
