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


def make_chains(text_string,gram_size=2):
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
    words = text_string.split() 
    for i in range(len(words) - gram_size): 
        key = ()
        for gram in range(gram_size):
            key = key + tuple([words[gram+i]])
        value = words[i + gram_size]
        if key in chains:
            chains[key].append(value)
        else: 
            chains[key] = [value]
    return chains


def make_text(chains,gram_size=2):
    """Return text from chains."""
    words = []
    end_not_reached = True
    key = choice(list(chains.keys())) # set initial randomly selected key tuple
    while end_not_reached:
        words.append(key[0]) # add the first word in key tuple to words list
        next_word = choice(chains[key]) # randomly select next word from value list
        key_list = list(key) # create a list based on the tuple key for mutability 
        del key_list[0] # remove the first item in the key
        key_list.append(next_word) # add next val to key list
        key = tuple(key_list) # turn back to a tuple for use with chains dictionary 
        if key not in chains:
            end_not_reached = False
            for gram in range(gram_size):
                words.append(key[gram])
    return ' '.join(words)


if len(sys.argv) > 1:
    input_path = sys.argv[1]
else: 
    input_path = 'green-eggs.txt'

gram_size = int(input("What size of n-gram would you like to use? Enter the integer value for n: "))

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,gram_size)

# Produce random text
random_text = make_text(chains,gram_size)

print(random_text)
