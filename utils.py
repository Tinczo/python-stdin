"""
utils.py - Moduł zawierający funkcje pomocnicze współdzielone przez inne moduły.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """Sprawdza, czy znak jest końcem zdania."""
    return char in '.!?'

def is_whitespace(char):
    """Sprawdza, czy znak jest białym znakiem."""
    return char in ' \t\n\r\f\v'

def read_book_content():
    """
    Czyta treść książki ze standardowego wejścia, pomijając preambułę i informację o wydaniu.
    Zwraca treść jako string.
    """
    content = ""
    lines = []
    line = ""
    char = sys.stdin.read(1)
    
    # Pomijanie preambuły
    empty_line_count = 0
    preamble_lines = 0
    is_preamble = False
    
    while char:
        if char == '\n':
            lines.append(line)
            line = ""
            if not line.strip():
                empty_line_count += 1
            else:
                empty_line_count = 0
                
            # Sprawdzenie czy to koniec preambuły
            if empty_line_count >= 2 and preamble_lines > 0:
                is_preamble = True
                break
                
            preamble_lines += 1
            
            # Jeśli mamy 10 linii i nie było dwóch pustych z rzędu, zakładamy brak preambuły
            if preamble_lines >= 10 and empty_line_count < 2:
                break
        else:
            line += char
        char = sys.stdin.read(1)
    
    # Jeśli nie było preambuły, resetujemy wejście
    if not is_preamble:
        sys.stdin.seek(0)
        lines = []
        line = ""
        char = sys.stdin.read(1)
    
    # Czytanie treści
    dashes_count = 0
    edition_info = False
    
    while char:
        if char == '\n':
            # Sprawdzenie czy to początek informacji o wydaniu
            if line.strip() == "-----":
                edition_info = True
                break
            
            lines.append(line)
            line = ""
        else:
            line += char
        char = sys.stdin.read(1)
    
    # Łączenie linii z zachowaniem struktury akapitów
    for i, line in enumerate(lines):
        if not line.strip():
            content += "\n"
        else:
            content += line.strip() + "\n"
    
    return content

def clean_text(text):
    """
    Oczyszcza tekst z nadmiarowych białych znaków.
    """
    result = ""
    prev_whitespace = False
    
    for char in text:
        if is_whitespace(char):
            if not prev_whitespace:
                result += ' '
                prev_whitespace = True
        else:
            result += char
            prev_whitespace = False
    
    return result.strip()

def process_sentences(text, processor_function):
    """
    Przetwarza zdania w tekście używając podanej funkcji processor_function.
    """
    result = ""
    sentence = ""
    in_sentence = False
    
    for i in range(len(text)):
        char = text[i]
        
        if not in_sentence and not is_whitespace(char):
            in_sentence = True
        
        if in_sentence:
            sentence += char
            
            if is_end_of_sentence(char) or (char == '\n' and i+1 < len(text) and text[i+1] == '\n'):
                # Koniec zdania
                processed = processor_function(sentence)
                if processed:
                    result += processed
                sentence = ""
                in_sentence = False
            
        else:
            result += char
    
    # Obsługa ostatniego zdania, jeśli nie kończy się znakiem końca zdania
    if sentence:
        processed = processor_function(sentence)
        if processed:
            result += processed
    
    return result

def split_into_sentences(text):
    """
    Dzieli tekst na zdania.
    """
    sentences = []
    sentence = ""
    in_sentence = False
    
    for i in range(len(text)):
        char = text[i]
        
        if not in_sentence and not is_whitespace(char):
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
    
    return sentences

def count_words_in_sentence(sentence):
    """
    Liczy słowa w zdaniu.
    """
    word_count = 0
    in_word = False
    
    for char in sentence:
        if is_whitespace(char):
            if in_word:
                in_word = False
        else:
            if not in_word:
                word_count += 1
                in_word = True
    
    return word_count

def split_sentence_into_words(sentence):
    """
    Dzieli zdanie na słowa.
    """
    words = []
    word = ""
    
    for char in sentence:
        if is_whitespace(char):
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    
    if word:
        words.append(word)
    
    return words