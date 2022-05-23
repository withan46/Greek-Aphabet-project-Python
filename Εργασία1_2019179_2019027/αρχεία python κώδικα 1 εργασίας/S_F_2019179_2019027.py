import math
import random


def findEncode(text, p, count):

    # καλώ την συνάρτηση και αποθηκεύω την κάθε κωδικολέξη στο code
    # *δηλαδή code = {'Α': '00001', 'Β': '000110111', 'Γ': '0001111',.....,'Ψ': '11111001011', 'Ω': '1111110'}
    codes = main(p, count)

    # για count = 0 δημιουργείτε το κρυπτογραφημένο μύνημα και στέλνεται στην main
    # για count = 1 επιστρεφει τον codes
    if count == 0:
        encrypt = ''
        for letter in text:
            encrypt += codes[letter]
        return encrypt
    else:
        return codes


def code_words(a):
    a = a - int(a)
    r = -1
    b = []
    while a > 10 ** (-5):
        if a >= 2 ** r:
            b.append('1')
            a = a - 2 ** r
        else:
            b.append('0')
        r -= 1
    return ''.join(b)


def length_words(p):
    lp = []
    for i in p:
        m_l = math.log(1 / p[i], 2)
        if m_l == int(m_l):
            lp.append(int(m_l) + 1)
        else:
            lp.append(int(m_l) + 2)
    return lp


def com_coding01(mes, n):
    coded_mes = []
    for i in mes:
        coded_mes.append(n * i)
    return ''.join(coded_mes)


def coding(mes, code):
    coded_mes = []
    for i in mes:
        coded_mes.append(code[i])
    return ''.join(coded_mes)


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


def main(p, count):
    f = []
    fi = []
    s = 0
    for key, i in zip(p, range(0, len(p))):
        s += p[key]
        f.append(s)
        if i == 0:
            fi.append(p[key] / 2)
        else:
            fi.append(f[i - 1] + p[key] / 2)
    l = []
    for i in fi:
        l.append(code_words(i))

    l_w = length_words(p)
    cd = {}
    for i, key in zip(range(0, len(p)), p):
        cd[key] = l[i][:l_w[i]]

    h = 0
    l_sfe = 0
    for key in p:
        h -= p[key] * math.log(p[key], 2)
        l_sfe += p[key] * len(cd[key])
    if count == 1:
        return h, l_sfe
    else:
        return cd
