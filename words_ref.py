# program for analyzing text from a website and saving it to a dictionary
""" Retrieve and print words from a url
    usage:
    python words_ref.py <url>
"""
import sys
from urllib.request import urlopen
def fetch_words(url):
    """ fetch a list of words from the url.
    Args:
    url: the url of the utf-8 text document.

    Returns:
    A list of strings containing the words from the
    document
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """print items one per line

    Args:
    items: an iterable series of printable items
    """
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)

# makes the script to be executed, import by $python words.py
if __name__  == '__main__':
    # pass the url in the main  argument from the command line
    main(sys.argv[1])
