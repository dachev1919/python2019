from decimal import Decimal
from math import floor

def going(n):
	f = 1; s = 0
	for i in range(1, n+1):
		f *= i
		s += f
	print("f -> ", f)
	print("s -> ", s)
	return floor(float(Decimal(1/Decimal(f)*s))*1e6)/1e6

if __name__ == "__main__":
	print("finish->", going(2500))