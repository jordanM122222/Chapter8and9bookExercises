# 9.15.1

# The words “contrafibularities” and “anaspeptic” were invented for a 1987 episode of the British
# television show Blackadder the Third. They are not real English words

# 9.15.2

#!/usr/bin/evn python3

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2)

def run():
    print(is_anagram('tame', 'fame'))
    print(is_anagram('tops', 'stop'))

def main():
    count = 0
    with open('files/words.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if is_anagram(word, 'takes'):
                count += 1
                print(word)
    print(f'Found {count} anagrams for takes')

if __name__ == '__main__':
    # run()
    main()

# 9.15.3

#!/usr/bin/evn python3

def is_palindrome(word):
    return ''.join(reversed(word)) == word

def run():
    print(is_palindrome('civic'))
    print(is_palindrome('tops'))

def main():
    count = 0
    with open('files/words.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) >= 7 and is_palindrome(word):
                count += 1
                print(word)
    print(f'Found {count} anagrams for takes')

if __name__ == '__main__':
    # run()
    main()

# 9.15.4

#!/usr/bin/evn python3

def reverse_sentence(sentence):
    print(' '.join(
        reversed(
            sentence.split(' '))).lower().capitalize())

def main():
    reverse_sentence('Reverse this sentence')
    reverse_sentence('Unlearn what you have learned')
    reverse_sentence('Feel the Force')

if __name__ == '__main__':
    main()

# 9.15.5

#!/usr/bin/evn python3

def total_length(str_list):
    return sum(len(a.strip()) for a in str_list)

def run():
    print(total_length(['hello', 'world', 'I\'m', 'here']))

def main():
    with open('files/words.txt', 'r') as file:
        print(total_length(file.readlines()))

if __name__ == '__main__':
    #run()
    main()

