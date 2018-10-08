'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should
return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

def find(remaining_sentence, words):
    if remaining_sentence in words:
        return remaining_sentence, None

    for i in range(len(remaining_sentence)):
        if remaining_sentence[:i] in words:
            return remaining_sentence[:i], remaining_sentence[i:]

    return None, None

def solve(sentence, words):

    remaining_sentence = sentence
    used_words = []

    while remaining_sentence is not None:
        word, remaining_sentence = find(remaining_sentence, words)
        if word is not None:
            used_words.append(word)

    return used_words



if __name__ == '__main__':

    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    sentence = "bedbathandbeyond"

    print(solve(sentence=sentence, words=words))

    words = ['quick', 'brown', 'the', 'fox']
    sentence = "thequickbrownfox"

    print(solve(sentence=sentence, words=words))