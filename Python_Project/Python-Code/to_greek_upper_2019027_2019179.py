def convert(text):
    greek_upper = ''
    for i in text:
        if i in ['α', 'Α', 'ά', 'Ά']:
            greek_upper += 'Α'
        elif i in ['β', 'Β']:
            greek_upper += 'Β'
        elif i in ['γ', 'Γ']:
            greek_upper += 'Γ'
        elif i in ['δ', 'Δ']:
            greek_upper += 'Δ'
        elif i in ['ε', 'έ', 'Ε', 'Έ']:
            greek_upper += 'Ε'
        elif i in ['ζ', 'Ζ']:
            greek_upper += 'Ζ'
        elif i in ['η', 'ή', 'Η', 'Ή']:
            greek_upper += 'Η'
        elif i in ['θ', 'Θ']:
            greek_upper += 'Θ'
        elif i in ['ι', 'ί', 'Ι', 'Ί', 'ϊ', 'ΐ']:
            greek_upper += 'Ι'
        elif i in ['κ', 'Κ']:
            greek_upper += 'Κ'
        elif i in ['λ', 'Λ']:
            greek_upper += 'Λ'
        elif i in ['μ', 'Μ']:
            greek_upper += 'Μ'
        elif i in ['ν', 'Ν']:
            greek_upper += 'Ν'
        elif i in ['ξ', 'Ξ']:
            greek_upper += 'Ξ'
        elif i in ['ο', 'ό', 'Ο', 'Ό']:
            greek_upper += 'Ο'
        elif i in ['π', 'Π']:
            greek_upper += 'Π'
        elif i in ['ρ', 'Ρ']:
            greek_upper += 'Ρ'
        elif i in ['σ', 'Σ', 'ς']:
            greek_upper += 'Σ'
        elif i in ['τ', 'Τ']:
            greek_upper += 'Τ'
        elif i in ['υ', 'ύ', 'Υ', 'Ύ']:
            greek_upper += 'Υ'
        elif i in ['φ', 'Φ']:
            greek_upper += 'Φ'
        elif i in ['χ', 'Χ']:
            greek_upper += 'Χ'
        elif i in ['ψ', 'Ψ']:
            greek_upper += 'Ψ'
        elif i in ['ω', 'Ω', 'ώ', 'Ώ']:
            greek_upper += 'Ω'
    return greek_upper