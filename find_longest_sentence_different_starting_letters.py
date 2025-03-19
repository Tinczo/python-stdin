"""
find_longest_sentence_different_starting_letters.py - Wyszukuje najdłuższe zdanie, w którym żadne dwa 
sąsiadujące słowa nie zaczynają się na tę samą literę.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def has_no_adjacent_same_starting_letters(sentence):
    """
    Sprawdza, czy w zdaniu żadne dwa sąsiadujące słowa nie zaczynają się na tę samą literę.
    """
    words = []
    word = ""
    
    for char in sentence:
        if char in ' \t\n\r\f\v':
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    
    if word:
        words.append(word)
    
    # Sprawdzamy, czy sąsiadujące słowa zaczynają się na tę samą literę
    for i in range(1, len(words)):
        if words[i] and words[i-1]:
            if words[i][0].lower() == words[i-1][0].lower():
                return False
    
    return True

def find_longest_sentence_with_different_starting_letters():
    """
    Znajduje najdłuższe zdanie, w którym żadne dwa sąsiadujące słowa nie zaczynają się na tę samą literę.
    """
    text = sys.stdin.read()
    
    sentences = []
    sentence = ""
    in_sentence = False
    
    for i in range(len(text)):
        char = text[i]
        
        if not in_sentence and not (char in ' \t\n\r\f\v'):
            in_sentence = True
        
        if in_sentence:
            sentence += char
            
            if is_end_of_sentence(char) or (char == '\n' and i+1 < len(text) and text[i+1] == '\n'):
                # Koniec zdania
                sentences.append(sentence.strip())
                sentence = ""
                in_sentence = False
    
    # Obsługa ostatniego zdania, jeśli nie kończy się znakiem końca zdania
    if sentence:
        sentences.append(sentence.strip())
    
    # Znajdowanie najdłuższego zdania z różnymi początkowymi literami sąsiadujących słów
    longest_sentence = ""
    max_length = 0
    
    for sentence in sentences:
        if has_no_adjacent_same_starting_letters(sentence):
            length = len(sentence)
            if length > max_length:
                max_length = length
                longest_sentence = sentence
    
    return longest_sentence, max_length

def main():
    try:
        longest_sentence, length = find_longest_sentence_with_different_starting_letters()
        print(f"Najdłuższe zdanie bez powtórzeń pierwszych liter ({length} znaków):")
        print(longest_sentence)
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()