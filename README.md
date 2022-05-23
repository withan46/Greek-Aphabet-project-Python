# How to: encoding-decoding / Finding the probability of the greek letters appearing in a text / Entropy of the Greek alphabet / Kullback Leibler distance of distribution / Huffman compression ratio



* ## Save Greek capitals
**Results:**
The text in Greek capitals was saved in the file NEO_SYNTAGMA_AB.txt
NEO_SYNTAGMA_AB.txt<br/><br/>
**The probability of the letters appearing:**<br/>
{'Α': 0.10434762341314853, 'Β': 0.006751402333856457, 'Γ': 0.016618238886212843,<br/> 
 'Δ': 0.020456205230200288, 'Ε': 0.07780816383610174, 'Ζ': 0.003993349596780459,<br/> 
 'Η': 0.05896017527230915, 'Θ': 0.011179825038457354, 'Ι': 0.09312118339885327,<br/> 
 'Κ': 0.03970819025125472, 'Λ': 0.023439563683826155, 'Μ': 0.030183196855042962,<br/>
 'Ν': 0.05603897011980049, 'Ξ': 0.004203116988051028, 'Ο': 0.10884596858150629,<br/>
 'Π': 0.04182140248923971, 'Ρ': 0.048098885902077476, 'Σ': 0.07925322808707677,<br/> 
 'Τ': 0.07989806858616778, 'Υ': 0.051859160619668415, 'Φ': 0.008631539692651926,<br/> 
 'Χ': 0.008079929145236727, 'Ψ': 0.0017169849433628043, 'Ω': 0.024985627049116645}<br/><br/>
**Code**:
```python
# First subject
greekUpperText = 
to_greek_upper_2019027_2019179.convert(clearText_2019179_2019027.main()
)
SYMBOLS = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
finalText = 
to_greek_upper_2019027_2019179.convert(clearText_2019179_2019027.main()
```
_Code 1.1:piece of code that removes from NEO_SYNTAGMA.txt those characters that do not belong
in the letters of the Greek alphabet_
```python
f = open("NEO_SYNTAGMA_AB.txt", "w")
f.write(finalText)
f.close()
)
```
_Code 1.2: Code 1.2: save the above text to, NEO_SYNTAGMA_AB.tx_
```python
pdf = Huff_2019027_2019179.make_pdf(finalText)
```
_Code 1.3: calculation of the probability of the appearance of the letters in Greek
language of _NEO_SYNTAGMA_ΑΒ.txt_ , to **Huff_2019027_2019179.py**_
* ## Entropy of the Greek alphabet
**Results:**
Entropy of the Greek alphabet if the letters appear equally likely: 4.584962500721156

**Code**:
```python
# Second subject
Hu = entropy.entropy(entropy.uu)
print('\n Θέμα 2\n Εντροπία του ελληνικού αλφάβητου αν τα γράμματα 
εμφανίζονται ισοπίθανα:', Hu)
```
* ## Entropy of the Greek alphabet based on the pdf
**Result:**
Entropy of the Greek alphabet based on the pdf distribution of the text: 4.0999305570789994<br/>

**Code:**
```python
# Third subject
Hx = entropy.entropy(pdf)
print('\n Θέμα 3\n Εντροπία του ελληνικού αλφάβητου με βάση την 
κατανομή pdf του κειμένου:', Hx)
```
_Code 3.1: calculates the entropy of the Greek alphabet
_NEO_SYNTAGMA_AB.txt, στο entropy_2019027_2019179.py__

* ## Distance Kullback Leibler of the pdf distribution by the uniform distribution u
**Results:**
Distance Kullback Leibler of the pdf distribution by the uniform distribution u: 0.4850319436421568

**Code:**
```python
# Forth subject
leibler = entropy.kullback(pdf, entropy.uu)
print('\n Θέμα 4\n Απόσταση Kullback Leibler της κατανομής pdf από την 
ομοιόμορφη κατανομή u:', leibler)
```
_Code 4.1: calculates the distance Kullback Leibler, στο
**entropy_2019027_2019179.py**_
* ## ShannonFanoElias encoded
**Results:**

ShannonFanoElias encoded text was saved to file
NEO_SYNTAGMA_ShannonFanoElias.txt
NEO_SYNTAGMA_ShannonFanoElias.txt

**Password of each letter:**
{'Α': '00001', 'Β': '000110111', 'Γ': '0001111', 'Δ': '0010001', 'Ε': '00101', 'Ζ': '001110100', 'Η': '010000', <br/>
 'Θ': '01001011', 'Ι': '01011', 'Κ': '011010', 'Λ': '0111000', 'Μ': '0111100', 'Ν': '100000', 'Ξ': '100010110', <br/>
 'Ο': '10011', 'Π': '101011', 'Ρ': '101110', 'Σ': '11001', 'Τ': '11011', 'Υ': '111011', 'Φ': '11110101', <br/>
 'Χ': '11111000', 'Ψ': '11111001011', 'Ω': '1111110'}<br/><br/>
 
Original text length = 128714 <br/>
Decoded text length = 128714 <br/>
Decoding success rate = 100.0 %<br/>

**Code:**
Main:
```python
# Fifth subject
# Encoding
count = 0
enco = ShannonFanoElias.findEncode(finalText, p, count)
f = open("NEO_SYNTAGMA_ShannonFanoElias.txt", "w")
f.write(enco)
f.close()
print('\n Θέμα 5\n Το κωδικοποιημένο με ShannonFanoElias κείμενο 
αποθηκεύτηκε στο αρχείο '
 'NEO_SYNTAGMA_ShannonFanoElias.txt')
# Decoding
deco = ShannonFanoElias.decode(enco, ShannonFanoElias.main(p, 0))
minlength = min(len(greekUpperText), len(deco))
j = 0
for i in range(minlength):
 if greekUpperText[i] == deco[i]:
 j += 1
print(' Μήκος αρχικού κειμένου = ', len(greekUpperText),
 '\n Μήκος αποκωδικοποιημένου κειμένου =', len(deco),
 '\n Ποσοστό επιτυχίας αποκωδικοποίησης = ', 100.0 * j / 
minlength, '%')
```
_Code 5.1: implements Shannon-Fano-Elias coding and decoding, to
**S_F_2019179_2019027.py**_
* ## Save Huffman encoded text


**Results**:
Huffman encoded text saved to NEO_SYNTAGMA_Huffman.txt
NEO_SYNTAGMA_Huffman.txt

**Password of each letter:**
{'Α': '010', 'Ο': '011', 'Ι': '000', 'Σ': '1100', 'Τ': '1101', 'Ε': '1011', 'Ν': '1000', 'Η': '1001', 'Υ': '0011', 'Ρ': '11111', <br/>
'Κ': '11100', 'Π': '11101', 'Μ': '10100', 'Ω': '00100', 'Δ': '111100', 'Λ': '111101', 'Γ': '101010', 'Θ': '001010', <br/>
'Φ': '1010110', 'Β': '0010110', 'Χ': '0010111', 'Ξ': '10101110', 'Ψ': '101011110', 'Ζ': '101011111'}<br/><br/>

Original text length = 128714 <br/>
Decoded text length = 128714 <br/>
Decoding success rate = 100.0 %<br/>

**Code:**
Main:
```python
# Sixth Subject
# Encode
enc = huff.encode(greekUpperText)
f = open("NEO_SYNTAGMA_Huffman.txt", "w")
f.write(enc)
f.close()
print('\n Θέμα 6\n Το κωδικοποιημένο με huffman κείμενο αποθηκεύτηκε 
στο αρχείο NEO_SYNTAGMA_Huffman.txt')
# Decode
dec = huff.decode(enc, huff.get_huffman_encoding(greekUpperText))
minlength = min(len(greekUpperText), len(dec))
j = 0
for i in range(minlength):
 if greekUpperText[i] == dec[i]:
 j += 1
print(' Μήκος αρχικού κειμένου = ', len(greekUpperText),
 '\n Μήκος αποκωδικοποιημένου κειμένου =', len(dec),
 '\n Ποσοστό επιτυχίας αποκωδικοποίησης = ', 100.0 * j / 
minlength, '%')
```
_Code 6.1: Huffman coding and decoding, to
Huff_2019027_2019179.py_
* ## Code rendering
**Results:**

Code rendering Shannon-Fano-Elias: 0.7216129840994531 <br/>
Code rendering with length code word 8-bit: 0.5124913196348749 <br/>
Code rendering huffman: 0.9908903275135029 <br/>
Code rendering length code word 8-bit: 0.5124913196348749<br/>


**Code:**
```python
# Seventh subject
count = 1
h, l_sfe = ShannonFanoElias.main(p, count)
print('\n Θέμα 7'
 '\n Απόδοση του κώδικα Shannon-Fano-Elias:', h / l_sfe,
 '\n Απόδοση του κώδικα με κωδικολέξη μήκους 8-bit:', h / 8.0)
lc = huff.avg_code_length(pdf, huff.huffman(pdf))
print(' Απόδοση του κώδικα huffman:', Hx / lc,
 '\n Απόδοση του κώδικα με κωδικολέξη μήκους 8-bit:', Hx / 8.0)
 ```
_Code 7.1: finds the code rendering Shannon-Fano-Elias - Huffman,
and code rendering that will encode a length codeword 8-bit._
* ## Code Sizes
**Results:**

Text length “NEO_SYNTAGMA_AB.txt”: 128714 <br/>
Size of Shannon-Fano_Elias coded text: 91413.0 <br/>
Size of huffman coded text: 66571.25 <br/>
Compression rate with Shannon-Fano_Elias: 0.7102024643783893 <br/>
Huffman compression ratio: 0.5172028683748465<br/>

**Code:**
```python
# Eighth subject
print('\n Θέμα 8'
 '\n Το μέγεθος του κειμένου “NEO_SYNTAGMA_AB.txt”:', 
len(greekUpperText),
```
_Code 8.1: find and display the size of the NEO_SYNTAGMA_AB_


```python
'\n Μέγεθος που έχει το κωδικοποιημένο με Shannon-Fano_Elias κείμενο:', 
len(enco) / 8,
'\n Μέγεθος που έχει το κωδικοποιημένο με huffman κείμενο:', len(enc) / 
8,
```
_Code 8.2: find and display the size of the text
with (5) and (6) codes calculated with one bit._
```python
'\n Ποσοστό συμπίεσης με Shannon-Fano_Elias:', (len(enco) / 8) / 
len(greekUpperText),
'\n Ποσοστό συμπίεσης με huffman:', (len(enc)/8) / len(greekUpperText)
)
```
_Code 8.3: finding the percentage of compression achieved in each case_
