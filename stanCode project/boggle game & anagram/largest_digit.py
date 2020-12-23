"""
File: largest_digit.py
Name: Jason Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9



def find_largest_digit(n):
	"""
	This function is to find the largest digit in the input number
	:param n: int, the input number
	:return: int, the largest digit number in the input number
	"""
	t = 0
	return find_largest_digit_helper(abs(n), t)


def find_largest_digit_helper(n, greater):
	"""
	This function is the helper of find_largest_digit(n)
	:param n: int, the input number
	:param greater: int, the greater number within n
	:return: return greater
	"""
	if n != 0:
		if n % 10 > greater:
			greater = n % 10
		return find_largest_digit_helper(n//10, greater)
	return greater


if __name__ == '__main__':
	main()
