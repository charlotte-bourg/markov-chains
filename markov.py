"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text = file.read()
    file.close()
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split() #previously I had this doing text_string.split(" ") which only splits on a space, but a null parameter will split on any whitespace including newline characters
    #print(words)
    for i in range(len(words)-2):
        key_pair = (words[i], words[i+1])
        #print(f"key pair is: {key_pair}")
        value = words[i+2]
        #print(f"value is: {value}")
        if key_pair in chains:
            #chains[key_pair] = []
            chains[key_pair].append(value)
            #print("updating existing key pair")
            #print(f"chains is: {chains}")
        else: 
            chains[key_pair] = [value]
            #print("adding new key pair")
            #print(f"chains is: {chains}")
    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    end_not_reached = True
    key = choice(list(chains.keys())) #set initial randomly selected key tuple
    while end_not_reached:
        words.append(key[0]) #add the first word in key tuple to words list
        next_word = choice(chains[key]) #randomly select next word from value list
        key = (key[1],next_word) #update the key to a tuple of the second word in previous key, selected value
        if key not in chains:
            end_not_reached = False
            words.append(key[0])
            words.append(key[1])
    return ' '.join(words)


if len(sys.argv) > 1:
    input_path = sys.argv[1]
else: 
    input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
