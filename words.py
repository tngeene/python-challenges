# program for analyzing text from a website and saving it to a dictionary
from urllib.request import urlopen
def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    for word in story_words:
        print(word)

# makes the script to be executed, import by $python words.py
if __name__  == '__main__':
    fetch_words()
