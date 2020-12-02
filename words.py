def print_upper_words(lists):

    for word in lists:
        print(word.upper())

print_upper_words(['broo','ayeee', 'whats up', 'nopppee'])
""" Should print words on seperate line uppercased.

>>
HIII
BYEEE
FYEEE
MINEE
"""

def print_upper_words2(words):

    for word in words:
        if word.startswith('E') or word.startswith('e'):
            print(word.upper())

print_upper_words(['Ebroo','ayeee', 'whats up', 'nopppee', 'eastside'])

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

    
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                