#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
count_proper_name_sentences.py - Liczy procent zdań, które zawierają przynajmniej jedną nazwę własną.
Nazwą własną jest każdy wyraz napisany wielką literą, nie będący pierwszym wyrazem w zdaniu.
"""
import sys
# Ustawienie kodowania dla wejścia/wyjścia standardowego
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def is_whitespace(char):
    """
    Sprawdza, czy znak jest białym znakiem.
    """
    return char in ' \t\n\r\f\v'

def has_proper_name(sentence):
    """
    Sprawdza, czy zdanie zawiera nazwę własną.
    Używa przetwarzania znak po znaku bez używania list.
    """
    in_word = False
    is_first_word = True
    current_word_has_uppercase = False
    
    for char in sentence:
        if is_whitespace(char):
            if in_word:
                # Koniec słowa
                if current_word_has_uppercase and not is_first_word:
                    return True
                is_first_word = False
                in_word = False
                current_word_has_uppercase = False
        else:
            if not in_word:
                # Początek nowego słowa
                in_word = True
                if char.isupper():
                    current_word_has_uppercase = True
            # Kontynuacja słowa - nic nie robimy
    
    # Sprawdzenie ostatniego słowa w zdaniu, jeśli istnieje
    if in_word and current_word_has_uppercase and not is_first_word:
        return True
    
    return False

def count_sentences_with_proper_names():
    """
    Liczy procent zdań, które zawierają przynajmniej jedną nazwę własną.
    Używa przetwarzania znak po znaku bez używania list.
    """
    # Zmienne pomocnicze do przetwarzania tekstu
    current_sentence = ""
    in_sentence = False
    proper_name_count = 0
    total_sentences = 0
    
    # Czytamy tekst znak po znaku
    char = sys.stdin.read(1)
    prev_char = None
    
    while char:
        # Sprawdzenie początku zdania
        if not in_sentence and not is_whitespace(char):
            in_sentence = True
        
        # Zbieranie znaków zdania
        if in_sentence:
            current_sentence += char
            
            # Sprawdzenie końca zdania
            if is_end_of_sentence(char) or (char == '\n' and prev_char == '\n'):
                # Mamy kompletne zdanie
                if has_proper_name(current_sentence):
                    proper_name_count += 1
                total_sentences += 1
                
                # Reset dla nowego zdania
                current_sentence = ""
                in_sentence = False
        
        # Przygotowanie do następnej iteracji
        prev_char = char
        char = sys.stdin.read(1)
    
    # Obsługa ostatniego zdania, jeśli nie kończy się znakiem końca zdania
    if current_sentence:
        if has_proper_name(current_sentence):
            proper_name_count += 1
        total_sentences += 1
    
    # Obliczanie procentu
    if total_sentences > 0:
        percent = (proper_name_count / total_sentences) * 100
    else:
        percent = 0
    
    return percent, proper_name_count, total_sentences

def main():
    try:
        percent, proper_name_count, total_sentences = count_sentences_with_proper_names()
        print(f"Procent zdań z nazwami własnymi: {percent:.2f}% ({proper_name_count}/{total_sentences})")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()