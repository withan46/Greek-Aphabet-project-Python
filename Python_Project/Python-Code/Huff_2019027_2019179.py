def encode(originalText):
    encoding = get_huffman_encoding(originalText)

    enc = ''
    for letter in originalText:
        enc += encoding[letter]
    return enc


def get_huffman_encoding(originalText):
    pdf = make_pdf(originalText)
    encoding = huffman(pdf)
    return encoding


def decode(mes, code):
    # code: γράμμα -> κωδικό, π.χ 'Α' -> '101'
    # codeToLetter αντίστροφο του code πχ '101' -> 'Α'
    codeToLetter = {}
    decoded = ''

    # π.χ στην άσκηση minCodeWord = 3 (101) και max_codeword = 9 (100111001)
    max_codeword = 0
    minCodeWord = 100

    for i in code.keys():
        if max_codeword < len(code[i]):
            max_codeword = len(code[i])
        if minCodeWord > len(code[i]):
            minCodeWord = len(code[i])

        # Αν π.χ  code[A] == 101
        # θα γίνει codeToLetter[101] == A
        codeToLetter[code[i]] = i

    pos = 0
    while pos < len(mes):
        # δοκιμάζω για κάθε πιθανό μήκος κωδικού αν το τμήμα του message με αυτό το μήκος
        # αντιστοιχεί σε γράμμα
        for i in range(minCodeWord, max_codeword + 1):

            # t : το τμήμα του message από την θεση pos με μήκος i
            t = mes[pos:pos + i]

            if t in codeToLetter:
                # το t αντιστοιχεί σε αυτό το γράμμα
                letter = codeToLetter[t]
                decoded += letter
                # προχωράμε το δείκτη pos
                pos += i
                break
        else:

            pos += max_codeword

    return decoded


# Μέσο μήκος κώδικα
def avg_code_length(pdf, encoding):
    lc = 0
    for letter in pdf:
        lc += pdf[letter] * len(encoding[letter])
    return lc


def make_pdf(text):
    pdf = {'Α': 0, 'Β': 0, 'Γ': 0, 'Δ': 0, 'Ε': 0, 'Ζ': 0, 'Η': 0, 'Θ': 0, 'Ι': 0, 'Κ': 0, 'Λ': 0, 'Μ': 0, 'Ν': 0,
           'Ξ': 0, 'Ο': 0, 'Π': 0,
           'Ρ': 0, 'Σ': 0, 'Τ': 0, 'Υ': 0, 'Φ': 0, 'Χ': 0, 'Ψ': 0, 'Ω': 0}

    for letter in text:
        pdf[letter] += 1

    for letter in pdf:
        pdf[letter] /= len(text)

    return pdf


def huffman(p):
    """Return a Huffman code for an ensemble with distribution p."""
    #   print('in total = ',sum(p.values()))
    #   assert(sum(p.values()) == 1.0) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if len(p) == 2:
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'
    return c


def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert (len(p) >= 2)  # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda x: x[1])  # for python3
    return sorted_p[0][0], sorted_p[1][0]
