The problem, basically, is that when a Literal is found at the top level, it's expected to have a number of bits that's divisible by 4, "due to the hexadecimal representation".
But subpackets that are literals may (do?) not have extra zeroes.
