def converter(INPUT):
	SUM = 0
	for i in range(len(INPUT)):
		DIGIT = int(INPUT[i])
		if DIGIT not in (0, 1):
			print("Not a binary digit")
			return -1
		else:
			SUM = SUM * 2 + DIGIT
	return SUM

while True:
    try:
    	INPUT = input("Input a binary number: ")
    	SUM = converter(INPUT)

    	if SUM != -1:
    		print(SUM)
    		
    except ValueError:
    	print("Try again.")
