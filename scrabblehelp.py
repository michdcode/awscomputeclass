def get_sowpods():
    """Loads data for scrabble"""


    WORD_LIST = "sowpods.txt"
    wordlist = open(WORD_LIST).readlines()
    wordlist = [word.lower().strip() for word in wordlist]

    return wordlist

def get_scores():
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10}
    return scores

def get_counts():
    counts = {"a": 9, "c": 2, "b": 2, "e": 12, "d": 4, "g": 3,
            "f": 2, "i": 9, "h": 2, "k": 1, "j": 1, "m": 2,
            "l": 4, "o": 8, "n": 6, "q": 1, "p": 2, "s": 4,
            "r": 6, "u": 4, "t": 6, "w": 2, "v": 2, "y": 2,
            "x": 1, "z": 11, "blank": 2}
    return counts
        
          