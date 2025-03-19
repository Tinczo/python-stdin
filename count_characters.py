"""
count_characters.py - Zlicza wszystkie znaki w tekście, z pominięciem białych znaków.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_whitespace(char):
    """
    Sprawdza, czy znak jest białym znakiem.
    """
    return char in ' \t\n\r\f\v'

def count_non_whitespace_chars():
    """
    Zlicza znaki w tekście z wejścia standardowego, pomijając białe znaki.
    """
    char_count = 0
    
    char = sys.stdin.read(1)
    while char:
        if not is_whitespace(char):
            char_count += 1
        char = sys.stdin.read(1)
    
    return char_count

def main():
    try:
        char_count = count_non_whitespace_chars()
        print(f"Liczba znaków (bez białych znaków): {char_count}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()