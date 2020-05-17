import argparse
import json
from random import choice, random, randrange

VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
CONSONANT_PAIRS = [ ['B', 'V'], ['V', 'W'], ['W', 'R'],
        ['M', 'N'], ['B', 'M'], ['C', 'K'], ['C', 'G'],
        ['C', 'S'], ['S', 'Sh'], ['Ch', 'Sh'], ['Tt', 'Th'] ]
OTHER_CONSONANTS = ['D', 'F', 'H', 'J', 'L', 'P', 'Q', 'T', 'X', 'Y', 'Z']

user_vowels = []
user_consonants = []

def generate_word():
    length = randrange(2,10)
    word = []
    curr = 0
    first_letter = choice(user_alphabet)
    prev_letter = first_letter
    word.append(first_letter)
    while curr <= length:
        repeat_chance = random()
        if prev_letter in VOWELS:
            repeat_type = repeat_chance > 0.9
            if repeat_type:
                next_letter = choice(user_vowels)
            else:
                next_letter = choice(user_consonants)
        else:
            repeat_type = repeat_chance > 0.75
            if repeat_type:
                next_letter = choice(user_consonants)
            else:
                next_letter = choice(user_vowels)
        word.append(next_letter)
        prev_letter = next_letter
        curr = len(word)
    print(''.join(word).lower(), end=' ')

parser = argparse.ArgumentParser(description="Generate fantasy names and words.")
parser.add_argument('-f', '--file', nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()

if args.file is None:
    favored = ''
    while favored not in VOWELS and favored != 'QUIT':
        favored = input("Please choose a vowel (AEIOUY) to favor: ").upper()
    excluded = ''
    while excluded not in VOWELS and excluded != 'QUIT' and excluded != favored:
        excluded = input(f"Please choose a vowel ({'AEIOUY'.replace(favored, '')}) to exclude: ").upper()
    for vowel in VOWELS:
        if vowel != excluded:
            user_vowels.append(vowel)
    user_vowels.append(favored)

    for pair in CONSONANT_PAIRS:
        included = ''
        while included not in pair and included != 'QUIT':
            included = input(f"Please choose one of these consonants to use: {pair[0]} or {pair[1]} ").capitalize()
        user_consonants.append(included)
    user_consonants.extend(OTHER_CONSONANTS)
    user_alphabet = user_vowels + user_consonants
else:
    with open(args.file.name) as f:
        data = f.read()
    j = json.loads(data)
    user_alphabet = j['alphabet']
    user_vowels = [x for x in user_alphabet if x in VOWELS]
    user_consonants = [x for x in user_alphabet if x not in VOWELS]

user_alphabet.sort()
print(f"Here is your alphabet: {user_alphabet}")
cont = input("Do you want to generate words now? [Y/n] ").upper()
while cont != 'N' and cont != 'QUIT':
    generate_word()
    cont = input("").upper()
