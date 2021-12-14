cpdef str expand(seq, int steps, dict rules):
    if len(seq) == 2:
        if steps == 1:
            a = seq[0]
            b = seq[1]
            result = a + rules.get((a,b), '') + b
            result
        else:
            result = expand(expand(seq, steps-1, rules), 1, rules)
    else:
        # The hard part.
        first_pair, remainder = seq[:2], seq[1:]
        first_pair_expanded = expand(first_pair, steps, rules)
        remainder_expanded = expand(remainder, steps, rules)
        result = first_pair_expanded[:-1] + remainder_expanded
    return result
