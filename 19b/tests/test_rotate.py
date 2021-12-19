import sys
sys.path.append('.')

from scanner import Scanner

def test_rotate():
    with open('tests/scanner_rotations.txt', 'rt') as f:
        scanner_text = f.read().split('\n\n')
    scanner = Scanner.from_text(scanner_text[0])
    # Make sure we find all expected rotations.
    all_rotations = [str(r).strip() for r in scanner.all_rotations()]
    for scanner_str in scanner_text:
        try:
            assert scanner_str.strip() in all_rotations
        except AssertionError:
            print(f'Didnt find {scanner_str}')

test_rotate()
