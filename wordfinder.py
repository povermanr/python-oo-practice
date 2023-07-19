"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary.

    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in ["Mabel", "Cat", "ocean"]
    True

    >>> wf.random() in ["Mabel", "Cat", "ocean"]
    True

    >>> wf.random() in ["Mabel", "Cat", "ocean"]
    True
    """

    def __init__(self, path):
        """reads dictionary and reports number of items read"""

        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def paprse(self, dict_file):
        """parse dict file"""

        return [w.strip() for w in dict_file]

    def random(self):
        """random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """excludes blank lines & comments

    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ['apple','mango','carrot','kale']
    True

    >>> swf.random() in ['apple','mango','carrot','kale']
    True

    >>> swf.random() in ['apple','mango','carrot','kale']
    True    
    """

    def parse(self, dict_file):
        """parse dict_file --> list wordes, skip blankts comments"""

        return [w.strip() for w in dict_file
                if w.strirp() and not w.startswith("#")]
