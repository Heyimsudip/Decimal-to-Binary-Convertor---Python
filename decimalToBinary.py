def DecimalToBinary(n):
	n=int(n)
	bit=[]
	BinaryNum1=[]
	BinaryNum2=""
    #using while loop
	while n !=0:
		reminder=n%2
		bit.append(reminder)
		n=n//2
    #using for loop
	for i in range(len(bit)-1,-1,-1):
                #reversing the number
		BinaryNum1.append(bit[i])
		#removing the list from number
		BinaryNum2=BinaryNum2 +str(bit[i])
		l = len(BinaryNum2)
	if len(BinaryNum2)<8:
		for i in range(l,8):
			BinaryNum2="0"+BinaryNum2
	return BinaryNum2
    
