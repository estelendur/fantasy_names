VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
CONSONANT_PAIRS = [ ['B', 'V'], ['V', 'W'], ['W', 'R'],
        ['M', 'N'], ['B', 'M'], ['C', 'K'], ['C', 'G'],
        ['C', 'S'], ['S', 'Sh'], ['Ch', 'Sh'], ['Tt', 'Th'] ]
OTHER_CONSONANTS = ['D', 'F', 'H', 'J', 'L', 'P', 'Q', 'T', 'X', 'Y', 'Z']

user_vowels = []
user_consonants = []

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
user_alphabet.sort()
print(f"Here is your alphabet: {user_alphabet}")
