import math

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

def d2bconverter(INPUT):
	SUM = 0
	COUNTER = 0
	for i in range(len(INPUT)):
		DIGIT = int(INPUT[i])
		if DIGIT not in (0, 1):
			print("Not a binary digit")
			return -1
		else:
			SUM = SUM + DIGIT
			COUNTER += 1
	SUM = COUNTER + SUM
	SUM = SUM / 2
	return SUM

def friction():
	try:
		A = float(input("GIVE (p=u/s): "))
		B = input("MASS(KG) OR N: ")
		if B == "MASS" or B == "1":
			NUM = float(input("input: "))
			N = 9.81 * NUM
		elif B == "N" or B == "2":
			N = float(input("input: "))
			NUM = N / 9.81
		F2 = N * A
		C = input("NEED ACCELERATION? ").upper()
		if C == "YES" or C == "1":
			E = float(input("GIVE (p=u/k): "))
			K2 = 0
			F = E * N
			K2 = A - F
			print("formula: F=ma")
			print("Using: a=F/A")
			ACCEL = N / NUM
			print("F(S): ", ACCEL, "N")
		else:
			print("Accleration not calculated")
		print("F(F): ", F2, "N")
	except TypeError or ValueError:
		print("try again")
	except SyntaxError:
		print("Syntax error (program fault)")
	
def notequal():
	if SUM != -1:
		print(SUM)

def Fun():
	try:
		print("nothing is selected")		
	except ValueError or TypeError:
		print("try again")
	except SyntaxError:
		print("Error system quitting")
	
while True:		
	try:
		b = input("Computer Science, Physics or Math: ").upper()
		if b in ("COMPUTER SCIENCE", "CP","1","COMPUTER"):
			a = input("binary or denary: ").upper()
			if a == "BINARY" or a == "1":	
				INPUT = input("Input binary number: ")
				SUM = converter(INPUT)
				notequal()
			elif a == "DENARY" or a == "2":
				INPUT = input("Input denary: ")
				SUM = d2bconverter(INPUT)
				notequal()
		elif b in ("PHYSICS","2","P","PHYSIC"):
			a = input("FRICTION or idk: ").upper()
			if a == "FRICTION" or a == "1": 
				friction()
		elif b in ("MATH", "3", "M"):
			a = input("Calculate Geometric seq and series or Statistic: ").upper()
			if a == "1" or a == "GEOMETRIC" or a == "G" or a=="GEOMETRIC SEQ":
				print("Function required, not done yet")
				exit()
				Geometric()
			elif a=="2" or a=="STATISTIC" or a =="S":
				print("Function required, not done yet")
				exit()
				Statistic()
		else:
			print("try again")
	except ValueError or TypeError:
		print("Try again.")
		
	except KeyboardInterrupt:
		print("ancelled")
		break
