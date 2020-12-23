"""
File: anagram.py
Name: Jason Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

result_list = []
dictionary = []


def main():
    # This is the program to find the anagram in dictionary
    global result_list
    while True:
        result_list = []
        print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
        s = input(str('Find anagrams for:'))
        if s == EXIT:
            break
        else:
            read_dictionary()
            find_anagrams(s)


def read_dictionary():
    # This function is to add the raw material of dictionary in the list.
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            dictionary.append(line)


def find_anagrams(s):
    """
    :param s: the word which is the word user want to find the anagram in the dictionary using this program
    :return: list, all of the anagrams
    """
    word = []
    find_anagrams_helper(s, word)
    print(f'{len(result_list)} anagrams: {result_list}')


def find_anagrams_helper(s, word):
    """
    this is the helper program to support find_anagrams(s).
    :param s: the word which is the word user want to find the anagram in the dictionary using this program
    :param word: the list which will collect the index of the letter in s
    :return: list, anagrams, the anagrams of s.
    """
    if len(word) == len(s):
        result = ''
        for index in word:
            result += s[index]
        if result in dictionary:
            if result not in result_list:
                print('Searching...')
                print(f'Found: \'{result}\' in dictionary..')
                result_list.append(result)
    else:
        for i in range(len(s)):
            if i not in word:
                # choose
                word.append(i)
                # explore
                find_anagrams_helper(s, word)
                # un-choose
                word.pop()


def has_prefix(sub_s):
    """
    This program is to pre-check whether the word prefix is in the dictionary
    :param sub_s: the prefix of string formulated by the word index.
    :return: boolean, True or False
    """
    read_dictionary()
    bool_list = []
    for word in dictionary:
        if word.startswith(sub_s):
            bool_list.append(1)
        else:
            bool_list.append(0)
    if 1 in bool_list:
        return True
    return False


if __name__ == '__main__':
    main()
