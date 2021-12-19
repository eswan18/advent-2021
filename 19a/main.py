from scanner import Scanner


#with open('test_input.txt', 'rt') as f:
with open('test2.txt', 'rt') as f:
    scanner_text = f.read().split('\n\n')

scanners = [Scanner.from_text(s) for s in scanner_text]
scanner = scanners[0]

for s in [scanner, scanner.facing_down(), scanner.facing_right()]:
    print(s)
    print(s.rotated(1))
    print(s.rotated(2))
    print(s.rotated(3))
