"""
File: boggle.py
Name: Jason Huang
----------------------------------------
TODO: This program is to create the boggle game as per user input
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = []
result_list = []


def main():
	"""
	TODO: This main function is the main body of the boggle game
	"""
	scale = int(input('length of board:'))
	row_1_list = []

	row_1 = str(input('1 row of letters: '))
	for letter in row_1:
		letter.strip()
		if letter != ' ':
			row_1_list.append(letter.lower())
	if len(row_1_list) != scale:
		print('illegal format')
		return
	row_2 = str(input('2 row of letters: '))
	for letter in row_2:
		letter.strip()
		if letter != ' ':
			row_1_list.append(letter.lower())
	if len(row_1_list) != 2 * scale:
		print('illegal format')
		return
	row_3 = str(input('3 row of letters: '))
	for letter in row_3:
		letter.strip()
		if letter != ' ':
			row_1_list.append(letter.lower())
	if len(row_1_list) != 3 * scale:
		print('illegal format')
		return
	row_4 = str(input('4 row of letters: '))
	for letter in row_4:
		letter.strip()
		if letter != ' ':
			row_1_list.append(letter.lower())
	if len(row_1_list) != 4 * scale:
		print('illegal format')
		return
	read_dictionary()
	board = row_1_list
	location = []
	for i in range(int(len(row_1_list)**0.5)):
		for j in range(int(len(row_1_list)**0.5)):
			location.append((i, j))

	word = ''
	word_index = []
	current_list = []

	boggle_game(board, location, word, word_index, current_list)
	print(f'There are {len(result_list)} words in total.')


def boggle_game(board, location, word, word_index, current_list):
	"""
	This function is the algorithm of how to find the possible word to check whether it is
	in the dictionary
	:param board: list, the boggle game board, including all the letters info.
	:param location: list, number the possible location of the board
	:param word: str, the possible word as per the index in word_index list corresponding letter in board
	:param word_index: list, the list containing the word index info.
	:param current_list: list, the current list carrying the location of the word_index
	:return: the word find in dictionary
	"""
	if not has_prefix(word):
		return
	else:
		if len(word) >= 4 and word in dictionary:
			if word not in result_list:
				print(f'Found:{word}..')
				result_list.append(word)

		for i in range(len(board)):
			if i in word_index:
				continue

			elif len(current_list) > 0:
				if location[i][0] + 1 < current_list[-1][0] or location[i][0] - 1 > current_list[-1][0]:
					continue
				if location[i][1] + 1 < current_list[-1][1] or location[i][1] - 1 > current_list[-1][1]:
					continue
			# choose
			current_list.append(location[i])
			word_index.append(i)

			# explore
			boggle_game(board, location, word+board[i], word_index, current_list)
			# un-choose
			current_list.pop()
			word_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			dictionary.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
