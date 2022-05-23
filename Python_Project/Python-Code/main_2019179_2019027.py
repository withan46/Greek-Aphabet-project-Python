import entropy_2019027_2019179
import clearText_2019179_2019027
import to_greek_upper_2019027_2019179
import Huff_2019027_2019179
import S_F_2019179_2019027

# Θέμα 1
greekUpperText = to_greek_upper_2019027_2019179.convert(clearText_2019179_2019027.main())

SYMBOLS = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

finalText = to_greek_upper_2019027_2019179.convert(clearText_2019179_2019027.main())
f =  open('NEO_SYNTAGMA_AB.txt', 'a',encoding='utf-8')
f.write(finalText)
f.close()

pdf = Huff_2019027_2019179.make_pdf(finalText)

print(' Θέμα 1\n Το κείμενο με κεφαλαία Ελληνικά αποθηκεύτηκε στο αρχείο NEO_SYNTAGMA_AB.txt')
print(" Η πιθανότητα εμφάνισης των γραμμάτων:", pdf)

# Θέμα 2
Hu = entropy_2019027_2019179.entropy(entropy_2019027_2019179.uu)
print('\n Θέμα 2\n Εντροπία του ελληνικού αλφάβητου αν τα γράμματα εμφανίζονται ισοπίθανα:', Hu)

# Θέμα 3
Hx = entropy_2019027_2019179.entropy(pdf)
print('\n Θέμα 3\n Εντροπία του ελληνικού αλφάβητου με βάση την κατανομή pdf του κειμένου:', Hx)

# Θέμα 4
leibler = entropy_2019027_2019179.kullback(pdf, entropy_2019027_2019179.uu)
print('\n Θέμα 4\n Απόσταση Kullback Leibler της κατανομής pdf από την ομοιόμορφη κατανομή u:', leibler)

# Θέμα 5
# Κωδικοποίηση
count = 0
enco = S_F_2019179_2019027.findEncode(finalText, pdf, count)

f = open("NEO_SYNTAGMA_ShannonFanoElias.txt", "w")
f.write(enco)
f.close()
print('\n Θέμα 5\n Το κωδικοποιημένο με ShannonFanoElias κείμενο αποθηκεύτηκε στο αρχείο '
      'NEO_SYNTAGMA_ShannonFanoElias.txt')

# Αποκωδικοποίηση
deco = S_F_2019179_2019027.decode(enco, S_F_2019179_2019027.main(pdf, 0))
minlength = min(len(greekUpperText), len(deco))
j = 0
for i in range(minlength):
    if greekUpperText[i] == deco[i]:
        j += 1
print(' Μήκος αρχικού κειμένου = ', len(greekUpperText),
      '\n Μήκος αποκωδικοποιημένου κειμένου =', len(deco),
      '\n Ποσοστό επιτυχίας αποκωδικοποίησης = ', 100.0 * j / minlength, '%')

# Θέμα 6
# Κωδικοποίηση
enc = Huff_2019027_2019179.encode(greekUpperText)
f = open("NEO_SYNTAGMA_Huffman.txt", "w")
f.write(enc)
f.close()
print('\n Θέμα 6\n Το κωδικοποιημένο με huffman κείμενο αποθηκεύτηκε στο αρχείο NEO_SYNTAGMA_Huffman.txt')

# Αποκωδικοποίηση
dec = Huff_2019027_2019179.decode(enc, Huff_2019027_2019179.get_huffman_encoding(greekUpperText))
minlength = min(len(greekUpperText), len(dec))
j = 0
for i in range(minlength):
    if greekUpperText[i] == dec[i]:
        j += 1
print(' Μήκος αρχικού κειμένου = ', len(greekUpperText),
      '\n Μήκος αποκωδικοποιημένου κειμένου =', len(dec),
      '\n Ποσοστό επιτυχίας αποκωδικοποίησης = ', 100.0 * j / minlength, '%')
# Θέμα 7
count = 1
h, l_sfe = S_F_2019179_2019027.main(pdf, count)
print('\n Θέμα 7'
      '\n Απόδοση του κώδικα Shannon-Fano-Elias:', h / l_sfe,
      '\n Απόδοση του κώδικα με κωδικολέξη μήκους 8-bit:', h / 8.0)

lc = Huff_2019027_2019179.avg_code_length(pdf, Huff_2019027_2019179.huffman(pdf))
print(' Απόδοση του κώδικα huffman:', Hx / lc,
      '\n Απόδοση του κώδικα με κωδικολέξη μήκους 8-bit:', Hx / 8.0)

# Θέμα 8
print('\n Θέμα 8'
      '\n Το μέγεθος του κειμένου “NEO_SYNTAGMA_AB.txt”:', len(greekUpperText),
      '\n Μέγεθος που έχει το κωδικοποιημένο με Shannon-Fano_Elias κείμενο:', len(enco) / 8,
      '\n Μέγεθος που έχει το κωδικοποιημένο με huffman κείμενο:', len(enc) / 8,
      '\n Ποσοστό συμπίεσης με Shannon-Fano_Elias:', (len(enco) / 8) / len(greekUpperText),
      '\n Ποσοστό συμπίεσης με huffman:', (len(enc)/8) / len(greekUpperText)
      )
