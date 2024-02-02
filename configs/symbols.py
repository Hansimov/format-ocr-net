import string
from utils.logger import logger


# NOTES: Most symbols are taken form following reference:
# The Comprehensive LaTeX Symbol List - The CTAN archive
#   - https://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf


def chars_to_list(chars) -> list:
    return chars.split()


LATEX_SYMBOLS = []
LATEX_MACROS = []


# https://tex.stackexchange.com/questions/34580/escape-character-in-latex
ESCAPED_SYMBOLS = r"\& \% \$ \# \_ \{ \} \~ \^ \\"

LOWER_ASCII_SYMBOLS = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
UPPER_ASCII_SYMBOLS = " ".join([char.upper() for char in LOWER_ASCII_SYMBOLS])
DIGIT_SYMBOLS = "0 1 2 3 4 5 6 7 8 9"

# Table 3: [LaTeX-2e] Commands Defined to Work in Both Math and Text Mode
LATEX2E_MATH_TEXT_SYMBOLS = r"\copyright \dag \ddag \dots \P \pounds \S"

# Table 4: [AMS] Commands Defined to Work in Both Math and Text Mode
# https://ctan.org/pkg/amsfonts
AMS_MATH_TEXT_SYMBOLS = r"\checkmark \circledR \maltese"

# # Table 5: Non-ASCII Letters (Excluding Accented Letters)
# NON_ASCII_SYMBOLS = r"\aa \AA \ae \AE \dh \DH \dj \DJ \ij \IJ \l \L \ng \NG  \o \O \oe \OE \ss \SS \th \TH"

# Table 53: Binary Operators
BINARY_OPERATOR_SYMBOLS = r"\amalg \ast \bigcirc \bigtriangledown \bigtriangleup \bullet \cap \cdot \circ \cup \dagger \ddagger \diamond \div \lhd \mp \odot \ominus \oplus \oslash \otimes \pm \rhd \setminus \sqcap \sqcup \star \times \triangleleft \triangleright \unlhd \unrhd \uplus \vee \wedge \wr"

# Table 54: [AMS] Binary Operators
AMS_BINARY_OPERATOR_SYMBOLS = r"\barwedge \boxdot \boxminus \boxplus \boxtimes \Cap \centerdot \circledast \circledcirc \circleddash \Cup \curlyvee \curlywedge \divideontimes \dotplus \doublebarwedge \intercal \leftthreetimes \ltimes \rightthreetimes \rtimes \smallsetminus \veebar"

# Table 79: Variable-sized Math Operators
VARIABLE_SIZED_MATH_OPERATOR_SYMBOLS = r"\bigcap \bigcup \bigodot \bigoplus \bigotimes \bigsqcup \biguplus \bigvee \bigwedge \coprod \int \oint \prod \sum"

# Table 80: [AMS] Variable-sized Math Operators
AMS_VARIABLE_SIZED_MATH_OPERATOR_SYMBOLS = r"\iint \iiint \iiiint \idotsint"

# Table 98: Binary Relations
BINARY_RELATION_SYMBOLS = r"\approx \asymp \bowtie \cong \dashv \doteq \equiv \frown \Join \mid \models \parallel \perp \prec \preceq \propto \sim \simeq \smile \succ \succeq \vdash"

# Table 99: [AMS] Binary Relations
AMS_BINARY_RELATION_SYMBOLS = r"\approxeq \backepsilon \backsim \backsimeq \because \between \Bumpeq \bumpeq \circleeq \curlyeqprec \curlyeqsucc \doteqdot \eqcirc \fallingdotseq \multimap \pitchfork \precapprox \preccurlyeq \precsim \risingdotseq \shortmid \shortparallel \smallfrown \smallsmile \succapprox \succcurlyeq \succsim \therefore \thickapprox \thicksim \varpropto \Vdash \vDash \Vvdash"

# Table 100: [AMS] Negated Binary Relations
AMS_NEGATED_BINARY_RELATION_SYMBOLS = r"\ncong \nmid \nparallel \nprec \npreceq \shortmid \shortparallel \nsim \nsucc \nsucceq \nvDash \nvdash \nVDash \precnapprox \precnsim \succnapprox \succnsim"

# Table 125: Subset and Superset Relations
SUBSET_SUPERSET_RELATION_SYMBOLS = (
    r"\sqsubset \sqsubseteq \sqsupset \sqsupseteq \subset \subseteq \supset \supseteq"
)

# Table 126: [AMS] Subset and Superset Relations
AMS_SUBSET_SUPERSET_RELATION_SYMBOLS = r"\nsubseteq \nsupseteq \nsupseteqq \sqsubset \seqsupset \Subset \subseteqq \subsetneq \subsetneqq \Supset \supseteqq \supsetneq \supsetneqq \varsubsetneq \varsubsetneqq \varsupsetneq \varsupsetneqq"

# Table 136: Inequalities
INEQUALITY_SYMBOLS = r"\geq \gg \leq \ll \neq"

# Table 137: [AMS] AMS Inequalities
AMS_INEQUALITY_SYMBOLS = r"\eqslantgtr \eqslantless \geqq \geqslant \ggg \gnapprox \gneq \gneqq \gnsim \gtrapprox \gtrdot \gtreqless \gtreqqless \gtrless \gtrsim \gvertneqq \leqq \leqslant \lessapprox \lessdot \lesseqgtr \lesseqqgtr \lessgtr \lesssim \lll \lnapprox \lneq \lneqq \lnsim \vertneqq \ngeq \ngeqq \ngeqslant \ngtr \nleq \nleqq \nleqslant \nless"

# Table 146: [AMS] Triangle Relations
AMS_TRIANGLE_RELATION_SYMBOLS = r"\blacktriangleleft \blacktriangleright \ntriangleleft \ntrianglelefteq \ntriangleright \ntrianglerighteq \trianglelefteq \triangleq \trianglerighteq \vartriangleleft \vartriangleright"

# Table 153: Arrows
ARROW_SYMBOLS = r"\Downarrow \downarrow \hookleftarrow \hookrightarrow \leftsto \leftarrow \Leftarrow \leftrightarrow \Leftrightarrow \longleftarrow \Longleftarrow \longleftrightarrow \Longleftrightarrow \longmapsto \longrightarrow \Longrightarrow \mapsto \nearrow \nwarrow \rightarrow \Rightarrow \searrow \swarrow \uparrow \Uparrow \updownarrow \Updownarrow"

# Table 154: Harpoons
HARPOON_SYMBOLS = r"\leftharpoondown \leftharpoonup \rightharpoondown \rightharpoonup \rightleftharpoons"

# Table 156: [AMS] Arrows
AMS_ARROW_SYMBOLS = r"\circlearrowleft ⟲ \circlearrowleft \circlearrowright \curvearrowleft \curvearrowright \dashleftarrow \dashrightarrow \downdownarrows \leftarrowtail \leftleftarrows \leftrightarrows \leftrightsquigarrow \Lleftarrow \looparrowleft \looparrowright \Lsh \rightarrowtail \rightleftarrows \rightrightarrows \rightsquigarrow \Rsh \twoheadleftarrow \twoheadrightarrow \upuparrows"

# Table 157: [AMS] Negated Arrows
AMS_NEGATED_ARROW_SYMBOLS = r"\nleftarrow \nLeftarrow \nleftrightarrow \nLeftrightarrow \nrightarrow \nRightarrow"

# Table 158: [AMS] Harpoons
AMS_HARPOON_SYMBOLS = r"\downharpoonleft \downharpoonright \leftrightharpoons \rightleftharpoons \upharpoonleft \upharpoonright"

# Table 198: Extension Characters
EXTENSION_SYMBOLS = r"\relbar \Relbar"

# Table 203: Log-like Symbols
LOG_LIKE_SYMBOLS = r" \arccos \cos \csc \exp \ker \limsup \min \sinh \arcsin \cosh \deg \gcd \lg \ln \Pr \sup \arctan \cot \det \hom \lim \log \sec \tan \arg \coth \dim \inf \liminf \max \sin \tanh"

# Table 204: [AMS] Log-like Symbols
AMS_LOG_LIKE_SYMBOLS = r"\injlim \projlim \varinjlim \varliminf \varlimsup \varprojlim"


# Table 208: Greek Letters
GREEK_SYMBOLS = r"\alpha \beta \gamma \delta \epsilon \varepsilon \zeta \eta \theta \iota \kappa \lambda \mu \nu \xi \omicron \pi \rho \sigma \varsigma \tau \upsilon \phi \varphi \chi \psi \omega \Gamma \Delta \Theta \Lamba \Xi \Pi \Sigma \Upsilon \Phi \Psi \Omega"

# Table 209: [AMS] Greek Letters
AMS_GREEK_SYMBOLS = r"\digamma \varkappa"

# Table 218: [AMS] Hebrew Letters
AMS_HEBREW_SYMBOLS = r"\beth \gimel \daleth"

# Table 223: Letter-like Symbols
LETTER_LIKE_SYMBOLS = (
    r"\bot \ell \exists \forall \hbar \Im \imath \in \jmath \ni \partial \Re \top \wp"
)

# Table 224: [AMS] Letter-like Symbols
AMS_LETTER_LIKE_SYMBOLS = (
    r"\Bbbk \circledR \circledS \complement \Finv \Game \hbar \hslash \nexists"
)

# Table 238: [AMS] Delimiters
AMS_DELIMITER_SYMBOLS = r"\ulcorner \llcorner \urcorner \lrcorner"

# Table 244: Variable-sized Delimiters
VARIABLE_SIZED_DELIMITER_SYMBOLS = r"\downarrow \langle \lceil \lfloor ( / \Downarrow \rangle \rceil \rfloor ) \backslash [ | \uparrow \updownarrow \{ ] \| \Uparrow \Updownarrow \}"

# Table 245: Large, Variable-sized Delimiters
LARGE_VARIABLE_SIZED_DELIMITER_SYMBOLS = (
    r"\lmoustache \arrowvert \rmoustache \Arrowvert \lgroup \bracevert \rgroup"
)

# Table 246: [AMS] Variable-sized Delimiters
AMS_VARIABLE_SIZED_DELIMITER_SYMBOLS = r"\lvert \lVert \rvert \rVert"


# Table 259: Math-mode Accents
MATH_MODE_ACCENT_MACROS = (
    r"\acute \bar \breve \check \ddot \dot \grave \hat \mathring \tilde \vec"
)

# Table 260: [AMS] Math-mode Accents
AMS_MATH_MODE_ACCENT_MACROS = r"\dddot \ddddot"

# Table 270: Extensible Accents
EXTENSIBLE_ACCENT_MACROS = r"\widetilde \overleftarrow \overline \overbrace \sqrt \widehat \overrightarrow \underline \underbrace"

# Table 273: [AMS] Extensible Accents
AMS_EXTENSIBLE_ACCENT_MACROS = (
    r"\overleftrightarrow \underleftarrow \underleftrightarrow \underrightarrow"
)

# Table 288: AMS Extensible Arrows
AMS_EXTENSIBLE_ARROW_MACROS = r"\xleftarrow \xrightarrow"

# Table 306: Dots
DOT_SYMBOLS = r"\cdotp \cdots \colon \ddots \ldotp \ldots \vdots"

# Table 307: [AMS] Dots
AMS_DOT_SYMBOLS = r"\because \dotsb \dotsc \dotsi \dotsm \dotso \therefore"

# Table 327: [AMS] Angles
AMS_ANGLE_SYMBOLS = r"\angle \measuredangle \sphericalangle"

# Table 334: Miscellaneous LATEX-2e Math Symbols
MISC_LATEX2E_MATH_SYMBOLS = r"\aleph \emptyset \angle \backslash \Box \Diamond \infty \mho \nabla \neg \prime \surd \triangle"

# Table 335: Miscellaneous [AMS] Math Symbols
MISC_AMS_MATH_SYMBOLS = r"\backprime \bigstar \blacklozenge \blacksquare \blacktriangle \blacktriangledown \diagdown \diagup \eth \lozenge \mho \square \triangledown \varnothing \vartriangle"

# Table 348: Math Alphabets
MATH_ALPHABET_MACROS = r"\mathrm \mathit \mathnormal \mathcal \mathscr \mathbb"

# Table 473: LATEX-2e Musical Symbols
LATEX2E_MUSICAL_SYMBOLS = r"\flat \natural \sharp"

# Table 512: LATEX-2e Playing-Card Suits
LATEX2E_PLAYING_CARD_SUIT_SYMBOLS = r"\clubsuit \diamondsuit \heartsuit \spadesuit"


SYMBOLS_LIST = [
    ESCAPED_SYMBOLS,
    LOWER_ASCII_SYMBOLS,
    UPPER_ASCII_SYMBOLS,
    DIGIT_SYMBOLS,
    LATEX2E_MATH_TEXT_SYMBOLS,
    AMS_MATH_TEXT_SYMBOLS,
    BINARY_OPERATOR_SYMBOLS,
    AMS_BINARY_OPERATOR_SYMBOLS,
    VARIABLE_SIZED_MATH_OPERATOR_SYMBOLS,
    AMS_VARIABLE_SIZED_MATH_OPERATOR_SYMBOLS,
    BINARY_RELATION_SYMBOLS,
    AMS_BINARY_RELATION_SYMBOLS,
    AMS_NEGATED_BINARY_RELATION_SYMBOLS,
    SUBSET_SUPERSET_RELATION_SYMBOLS,
    AMS_SUBSET_SUPERSET_RELATION_SYMBOLS,
    INEQUALITY_SYMBOLS,
    AMS_INEQUALITY_SYMBOLS,
    AMS_TRIANGLE_RELATION_SYMBOLS,
    ARROW_SYMBOLS,
    HARPOON_SYMBOLS,
    AMS_ARROW_SYMBOLS,
    AMS_NEGATED_ARROW_SYMBOLS,
    AMS_HARPOON_SYMBOLS,
    EXTENSION_SYMBOLS,
    LOG_LIKE_SYMBOLS,
    AMS_LOG_LIKE_SYMBOLS,
    GREEK_SYMBOLS,
    AMS_GREEK_SYMBOLS,
    AMS_HEBREW_SYMBOLS,
    LETTER_LIKE_SYMBOLS,
    AMS_LETTER_LIKE_SYMBOLS,
    AMS_DELIMITER_SYMBOLS,
    VARIABLE_SIZED_DELIMITER_SYMBOLS,
    LARGE_VARIABLE_SIZED_DELIMITER_SYMBOLS,
    AMS_VARIABLE_SIZED_DELIMITER_SYMBOLS,
    DOT_SYMBOLS,
    AMS_DOT_SYMBOLS,
    AMS_ANGLE_SYMBOLS,
    MISC_LATEX2E_MATH_SYMBOLS,
    MISC_AMS_MATH_SYMBOLS,
    LATEX2E_MUSICAL_SYMBOLS,
    LATEX2E_PLAYING_CARD_SUIT_SYMBOLS,
]

MICROS_LIST = [
    MATH_MODE_ACCENT_MACROS,
    AMS_MATH_MODE_ACCENT_MACROS,
    EXTENSIBLE_ACCENT_MACROS,
    AMS_EXTENSIBLE_ACCENT_MACROS,
    AMS_EXTENSIBLE_ARROW_MACROS,
    MISC_AMS_MATH_SYMBOLS,
    MATH_ALPHABET_MACROS,
]


def collect_symbols_and_macros():
    for symbols in SYMBOLS_LIST:
        symbols_list = chars_to_list(symbols)
        LATEX_SYMBOLS.extend(symbols_list)
    for macros in MICROS_LIST:
        macros_list = chars_to_list(macros)
        LATEX_MACROS.extend(macros_list)


collect_symbols_and_macros()

if __name__ == "__main__":
    logger.success(LATEX_SYMBOLS)
    logger.success(LATEX_MACROS)