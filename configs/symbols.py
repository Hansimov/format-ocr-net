import string
from utils.logger import logger


# NOTES: Most symbols are taken form following reference:
# The Comprehensive LaTeX Symbol List - The CTAN archive
#   - https://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf


def chars_to_list(chars) -> list:
    return chars.split()


LATEX_SYMBOLS = []


# https://tex.stackexchange.com/questions/34580/escape-character-in-latex
ESCAPED_SYMBOLS = r"\& \% \$ \# \_ \{ \} \~ \^ \\"


LOWER_ASCII_SYMBOLS = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
UPPER_ASCII_SYMBOLS = " ".join([char.upper() for char in LOWER_ASCII_SYMBOLS])
DIGITS_SYMBOLS = "0 1 2 3 4 5 6 7 8 9"

# Table 3: [LaTeX-2e] Commands Defined to Work in Both Math and Text Mode
LATEX2E_COMMAND_SYMBOLS = r"\copyright \dag \ddag \dots \P \pounds \S"

# Table 4: [AMS] Commands Defined to Work in Both Math and Text Mode
# https://ctan.org/pkg/amsfonts
AMSFONTS_SYMBOLS = r"\checkmark \circledR \maltese"

# Table 5: Non-ASCII Letters (Excluding Accented Letters)
NON_ASCII_SYMBOLS = r"\aa \AA \ae \AE \dh \DH \dj \DJ \ij \IJ \l \L \ng \NG  \o \O \oe \OE \ss \SS \th \TH"

# Table 6: Upright Greek Letters
# https://www.ctan.org/pkg/textgreek
GREEK_NAMES = r"alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi omicron pi rho sigma tau upsilon phi chi psi omega"
# UPRIGHT_GREEK_SYMBOLS = " ".join(
#     rf"\text{name} \text{name.capitalize()}" for name in UPRIGHT_GREEK_NAMES.split()
# )

# # Table 7: Letters Used to Typeset African Languages
# # https://www.ctan.org/pkg/fc
# AFRICAN_SYMBOLS = r"\B{d} \B{D} \B{h} \B{H} \B{t} \B{T} \m{b} \m{B} \m{c} \m{C} \m{d} \m{D} \M{d} \M {D} \m{e} \m{E} \M{e} \M{E} \m{f} \m{F} \m{g} \m{G} \m{i} \m{I} \m{j} \m{J} \m{k} \m{K} \m{n} \m{N} \m{o} \m{O} \m{p} \m{P} \m{s} \m{S} \m{t} \m{T} \M{t} \M{T} \m{u} \m{U} \m{y} \m{Y} \m{z} \m{Z} \T{e} \T{E} \T{o} \T{O}"

# # Table 8: Letters Used to Typeset Vietnamese
# # https://www.ctan.org/pkg/vntex
# VIETNAM_SYMBOLS = r"\ohorn \OHORN \uhorn \UHORN"

# Table 9: Punctuation Marks Not Found in OT1
# Table 10: [pifont] Decorative Punctuation Marks
# Table 11: [fontawesome5] Decorative Punctuation Marks and Typographic Symbols
# Table 12: [tipa] Phonetic Symbols
# Table 13: [tipx] Phonetic Symbols
# Table 14: [wsuipa] Phonetic Symbols
# Table 15: [wasysym] Phonetic Symbols
# Table 16: [phonetic] Phonetic Symbols
# Table 17: [t4phonet] Phonetic Symbols
# Table 18: [semtrans] Transliteration Symbols
# Table 20: [tipa] Text-mode Accents
# Table 21: [extraipa] Text-mode Accents
# Table 22: [wsuipa] Text-mode Accents
# Table 23: [phonetic] Text-mode Accents
# Table 24: [metre] Text-mode Accents
# Table 25: [t4phonet] Text-mode Accents
# Table 26: [arcs] Text-mode Accents
# Table 27: [semtrans] Accents
# Table 28: [ogonek] Accents
# Table 29: [combelow] Accents
# Table 30: [wsuipa] Diacritics
# Table 31: [textcomp] Diacritics
# Table 32: [marvosym] Diacritics
# Table 33: [textcomp] Currency Symbols
# Table 34: [marvosym] Currency Symbols
# Table 35: [fontawesome5] Currency Symbols
# Table 36: [wasysym] Currency Symbols
# Table 37: [ChinA2e] Currency Symbols
# Table 38: [teubner] Currency Symbols
# Table 39: [tfrupee] Currency Symbols
# Table 40: [eurosym] Euro Signs
# Table 41: [fourier] Euro Signs
# Table 42: [textcomp] Legal Symbols
# Table 43: [fontawesome5] Legal Symbols
# Table 44: [cclicenses] Creative Commons License Icons

for symbols in [
    ESCAPED_SYMBOLS,
    LOWER_ASCII_SYMBOLS,
    UPPER_ASCII_SYMBOLS,
    DIGITS_SYMBOLS,
    LATEX2E_COMMAND_SYMBOLS,
    AMSFONTS_SYMBOLS,
    NON_ASCII_SYMBOLS,
]:
    symbols_list = chars_to_list(symbols)
    LATEX_SYMBOLS.extend(symbols_list)

if __name__ == "__main__":
    logger.success(LATEX_SYMBOLS)
