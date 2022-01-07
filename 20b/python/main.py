from image import Image

with open('input.txt', 'rt') as f:
    key = f.readline().strip()
    f.readline()
    image = Image.from_string(f.read().strip())

assert(len(key) == 512)
current = image
for _ in range(50):
    current = current.enhance(key)
    print(current.n_lit)
