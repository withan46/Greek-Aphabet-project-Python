import math

p = 1.0 / 24

uu = {'Α': p, 'Β': p, 'Γ': p, 'Δ': p, 'Ε': p, 'Ζ': p, 'Η': p, 'Θ': p, 'Ι': p, 'Κ': p, 'Λ': p, 'Μ': p, 'Ν': p,
      'Ξ': p, 'Ο': p, 'Π': p,
      'Ρ': p, 'Σ': p, 'Τ': p, 'Υ': p, 'Φ': p, 'Χ': p, 'Ψ': p, 'Ω': p}


def entropy(pdf):
    e = 0
    for i in pdf.keys():
        e -= pdf[i] * math.log(pdf[i], 2)
    return e


def kullback(p, q):
    distance = 0
    for i in p.keys():
        distance += p[i] * math.log(p[i] / q[i], 2)
    return distance
