from collections import OrderedDict
from utils.logger import logger
from constants import chars_to_list

LATEX_SYMBOLS = []

# Table 1: LATEX-2e Escapable "Special" Characters
# - https://tex.stackexchange.com/questions/34580/escape-character-in-latex
# ANCHOR[id=escaped-symbols]
ESCAPED_SYMBOLS = r"\& \% \$ \# \_ \{ \} \~ \^ \\"

# ANCHOR[id=ascii-symbols]
# ANCHOR[id=lower-ascii-symbols]
LOWER_ASCII_SYMBOLS = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
# ANCHOR[id=upper-ascii-symbols]
UPPER_ASCII_SYMBOLS = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
# ANCHOR[id=digit-symbols]
DIGIT_SYMBOLS = "0 1 2 3 4 5 6 7 8 9"
# ANCHOR[id=punctuation-symbols]
PUNCTUATION_SYMBOLS = r". , : ; ! ? ' \' \" ` - \ < > + = * @"

# Table 3: [LaTeX-2e] Commands Defined to Work in Both Math and Text Mode
# ANCHOR[id=latex2e-math-text-symbols]
LATEX2E_MATH_TEXT_SYMBOLS = r"\copyright \dag \ddag \dots \P \pounds \S"

# Table 4: [AMS] Commands Defined to Work in Both Math and Text Mode
# https://ctan.org/pkg/amsfonts
# ANCHOR[id=ams-math-text-symbols]
AMS_MATH_TEXT_SYMBOLS = r"\checkmark \circledR \maltese"

# # Table 5: Non-ASCII Letters (Excluding Accented Letters)
# ANCHOR[id=non-ascii-symbols]
NON_ASCII_SYMBOLS = r"\aa \AA \ae \AE \dh \DH \dj \DJ \ij \IJ \l \L \ng \NG  \o \O \oe \OE \ss \SS \th \TH"

# Table 53: Binary Operators
# ANCHOR[id=binary-operator-symbols]
BINARY_OPERATOR_SYMBOLS = r"\amalg \ast \bigcirc \bigtriangledown \bigtriangleup \bullet \cap \cdot \circ \cup \dagger \ddagger \diamond \div \lhd \mp \odot \ominus \oplus \oslash \otimes \pm \rhd \setminus \sqcap \sqcup \star \times \triangleleft \triangleright \unlhd \unrhd \uplus \vee \wedge \wr"

# Table 54: [AMS] Binary Operators
# ANCHOR[id=ams-binary-operator-symbols]
AMS_BINARY_OPERATOR_SYMBOLS = r"\barwedge \boxdot \boxminus \boxplus \boxtimes \Cap \centerdot \circledast \circledcirc \circleddash \Cup \curlyvee \curlywedge \divideontimes \dotplus \doublebarwedge \intercal \leftthreetimes \ltimes \rightthreetimes \rtimes \smallsetminus \veebar"

# Table 79: Variable-sized Math Operators
# ANCHOR[id=variable-sized-math-operator-symbols]
VARIABLE_SIZED_MATH_OPERATOR_SYMBOLS = r"\bigcap \bigcup \bigodot \bigoplus \bigotimes \bigsqcup \biguplus \bigvee \bigwedge \coprod \int \oint \prod \sum"

# Table 80: [AMS] Variable-sized Math Operators
# ANCHOR[id=ams-variable-sized-math-operator-symbols]
AMS_VARIABLE_SIZED_MATH_OPERATOR_SYMBOLS = r"\iint \iiint \iiiint \idotsint"

# Table 98: Binary Relations
# ANCHOR[id=binary-relation-symbols]
BINARY_RELATION_SYMBOLS = r"\approx \asymp \bowtie \cong \dashv \doteq \equiv \frown \Join \mid \models \parallel \perp \prec \preceq \propto \sim \simeq \smile \succ \succeq \vdash"

# Table 99: [AMS] Binary Relations
# ANCHOR[id=ams-binary-relation-symbols]
AMS_BINARY_RELATION_SYMBOLS = r"\approxeq \backepsilon \backsim \backsimeq \because \between \Bumpeq \bumpeq \circeq \curlyeqprec \curlyeqsucc \doteqdot \eqcirc \fallingdotseq \multimap \pitchfork \precapprox \preccurlyeq \precsim \risingdotseq \shortmid \shortparallel \smallfrown \smallsmile \succapprox \succcurlyeq \succsim \therefore \thickapprox \thicksim \varpropto \Vdash \vDash \Vvdash"

# Table 100: [AMS] Negated Binary Relations
# ANCHOR[id=ams-negated-binary-relation-symbols]
AMS_NEGATED_BINARY_RELATION_SYMBOLS = r"\ncong \nmid \nparallel \nprec \npreceq \shortmid \shortparallel \nsim \nsucc \nsucceq \nvDash \nvdash \nVDash \precnapprox \precnsim \succnapprox \succnsim"

# Table 125: Subset and Superset Relations
# ANCHOR[id=subset-superset-relation-symbols]
SUBSET_SUPERSET_RELATION_SYMBOLS = (
    r"\sqsubset \sqsubseteq \sqsupset \sqsupseteq \subset \subseteq \supset \supseteq"
)

# Table 126: [AMS] Subset and Superset Relations
# ANCHOR[id=ams-subset-superset-relation-symbols]
AMS_SUBSET_SUPERSET_RELATION_SYMBOLS = r"\nsubseteq \nsupseteq \nsupseteqq \sqsubset \sqsupset \Subset \subseteqq \subsetneq \subsetneqq \Supset \supseteqq \supsetneq \supsetneqq \varsubsetneq \varsubsetneqq \varsupsetneq \varsupsetneqq"

# Table 136: Inequalities
# ANCHOR[id=inequality-symbols]
INEQUALITY_SYMBOLS = r"\le \ge \geq \gg \leq \ll \ne \neq"

# Table 137: [AMS] AMS Inequalities
# ANCHOR[id=ams-inequality-symbols]
AMS_INEQUALITY_SYMBOLS = r"\eqslantgtr \eqslantless \geqq \geqslant \ggg \gnapprox \gneq \gneqq \gnsim \gtrapprox \gtrdot \gtreqless \gtreqqless \gtrless \gtrsim \gvertneqq \leqq \leqslant \lessapprox \lessdot \lesseqgtr \lesseqqgtr \lessgtr \lesssim \lll \lnapprox \lneq \lneqq \lnsim \lvertneqq \ngeq \ngeqq \ngeqslant \ngtr \nleq \nleqq \nleqslant \nless"

# Table 146: [AMS] Triangle Relations
# ANCHOR[id=ams-triangle-relation-symbols]
AMS_TRIANGLE_RELATION_SYMBOLS = r"\blacktriangleleft \blacktriangleright \ntriangleleft \ntrianglelefteq \ntriangleright \ntrianglerighteq \trianglelefteq \triangleq \trianglerighteq \vartriangleleft \vartriangleright"

# Table 153: Arrows
# ANCHOR[id=arrow-symbols]
ARROW_SYMBOLS = r"\Downarrow \downarrow \hookleftarrow \hookrightarrow \leadsto \leftarrow \Leftarrow \leftrightarrow \Leftrightarrow \longleftarrow \Longleftarrow \longleftrightarrow \Longleftrightarrow \longmapsto \longrightarrow \Longrightarrow \mapsto \nearrow \nwarrow \rightarrow \Rightarrow \searrow \swarrow \uparrow \Uparrow \updownarrow \Updownarrow \to \gets \iff"

# Table 154: Harpoons
# ANCHOR[id=harpoon-symbols]
HARPOON_SYMBOLS = r"\leftharpoondown \leftharpoonup \rightharpoondown \rightharpoonup \rightleftharpoons"

# Table 156: [AMS] Arrows
# ANCHOR[id=ams-arrow-symbols]
AMS_ARROW_SYMBOLS = r"\circlearrowleft \circlearrowright \curvearrowleft \curvearrowright \dashleftarrow \dashrightarrow \downdownarrows \leftarrowtail \leftleftarrows \leftrightarrows \leftrightsquigarrow \Lleftarrow \looparrowleft \looparrowright \Lsh \rightarrowtail \rightleftarrows \rightrightarrows \rightsquigarrow \Rsh \twoheadleftarrow \twoheadrightarrow \upuparrows"

# Table 157: [AMS] Negated Arrows
# ANCHOR[id=ams-negated-arrow-symbols]
AMS_NEGATED_ARROW_SYMBOLS = r"\nleftarrow \nLeftarrow \nleftrightarrow \nLeftrightarrow \nrightarrow \nRightarrow"

# Table 158: [AMS] Harpoons
# ANCHOR[id=ams-harpoon-symbols]
AMS_HARPOON_SYMBOLS = r"\downharpoonleft \downharpoonright \leftrightharpoons \rightleftharpoons \upharpoonleft \upharpoonright"

# # Table 198: Extension Characters
# EXTENSION_SYMBOLS = r"\relbar \Relbar"

# Table 203: Log-like Symbols
# ANCHOR[id=log-like-symbols]
LOG_LIKE_SYMBOLS = r"\arccos \cos \csc \exp \ker \limsup \min \sinh \arcsin \cosh \deg \gcd \lg \ln \Pr \sup \arctan \cot \det \hom \lim \log \sec \tan \arg \coth \dim \inf \liminf \max \sin \tanh"

# Table 204: [AMS] Log-like Symbols
# ANCHOR[id=ams-log-like-symbols]
AMS_LOG_LIKE_SYMBOLS = r"\injlim \projlim \varinjlim \varliminf \varlimsup \varprojlim"

# Table 208: Greek Letters
# ANCHOR[id=greek-symbols]
GREEK_SYMBOLS = r"\alpha \beta \gamma \delta \epsilon \varepsilon \zeta \eta \theta \vartheta \iota \kappa \lambda \mu \nu \xi \omicron \pi \varpi \rho \varrho \sigma \varsigma \tau \upsilon \phi \varphi \chi \psi \omega \Gamma \Delta \Theta \Lambda \Xi \Pi \Sigma \Upsilon \Phi \Psi \Omega"

# Table 209: [AMS] Greek Letters
# ANCHOR[id=ams-greek-symbols]
AMS_GREEK_SYMBOLS = r"\digamma \varkappa"

# Table 218: [AMS] Hebrew Letters
# ANCHOR[id=ams-hebrew-symbols]
AMS_HEBREW_SYMBOLS = r"\beth \gimel \daleth"

# Table 223: Letter-like Symbols
# ANCHOR[id=letter-like-symbols]
LETTER_LIKE_SYMBOLS = (
    r"\bot \ell \exists \forall \hbar \Im \imath \in \jmath \ni \partial \Re \top \wp"
)

# Table 224: [AMS] Letter-like Symbols
# ANCHOR[id=ams-letter-like-symbols]
AMS_LETTER_LIKE_SYMBOLS = (
    r"\Bbbk \circledR \circledS \complement \Finv \Game \hbar \hslash \nexists"
)

# Table 238: [AMS] Delimiters
# ANCHOR[id=ams-delimiter-symbols]
AMS_DELIMITER_SYMBOLS = r"\ulcorner \llcorner \urcorner \lrcorner"

# Table 244: Variable-sized Delimiters
# ANCHOR[id=variable-sized-delimiter-symbols]
VARIABLE_SIZED_DELIMITER_SYMBOLS = r"\downarrow \Downarrow \langle \rangle \lceil \rceil \lfloor \rfloor \uparrow \Uparrow \updownarrow \Updownarrow \lbrace \lbrack \rbrace \rbrack \vert \Vert \slash \backslash ( ) [ ] \{ \} | \| /"

# Table 245: Large, Variable-sized Delimiters
# ANCHOR[id=large-variable-sized-delimiter-symbols]
LARGE_VARIABLE_SIZED_DELIMITER_SYMBOLS = (
    r"\lmoustache \rmoustache \arrowvert \Arrowvert \lgroup \rgroup \bracevert"
)

# Table 246: [AMS] Variable-sized Delimiters
# ANCHOR[id=ams-variable-sized-delimiter-symbols]
AMS_VARIABLE_SIZED_DELIMITER_SYMBOLS = r"\lvert \lVert \rvert \rVert"

# https://www.overleaf.com/learn/latex/Brackets_and_Parentheses
# ANCHOR[id=null-delimiter-symbols]
NULL_DELIMITER_SYMBOLS = r"\left. \right."

# Table 306: Dots
# ANCHOR[id=dot-symbols]
DOT_SYMBOLS = r"\cdotp \cdots \colon \ddots \ldotp \ldots \vdots"

# Table 307: [AMS] Dots
# ANCHOR[id=ams-dot-symbols]
AMS_DOT_SYMBOLS = r"\because \dotsb \dotsc \dotsi \dotsm \dotso \therefore"

# Table 327: [AMS] Angles
# ANCHOR[id=ams-angle-symbols]
AMS_ANGLE_SYMBOLS = r"\angle \measuredangle \sphericalangle"

# Table 334: Miscellaneous LATEX-2e Math Symbols
# ANCHOR[id=latex2e-misc-math-symbols]
LATEX2E_MISC_MATH_SYMBOLS = r"\aleph \emptyset \angle \backslash \Box \Diamond \infty \mho \nabla \neg \prime \surd \triangle"

# Table 335: Miscellaneous [AMS] Math Symbols
# ANCHOR[id=ams-misc-math-symbols]
AMS_MISC_MATH_SYMBOLS = r"\backprime \bigstar \blacklozenge \blacksquare \blacktriangle \blacktriangledown \diagdown \diagup \eth \lozenge \mho \square \triangledown \varnothing \vartriangle"

# Table 473: LATEX-2e Musical Symbols
# ANCHOR[id=latex2e-musical-symbols]
LATEX2E_MUSICAL_SYMBOLS = r"\flat \natural \sharp"

# Table 512: LATEX-2e Playing-Card Suits
# ANCHOR[id=latex2e-playing-card-suit-symbols]
LATEX2E_PLAYING_CARD_SUIT_SYMBOLS = r"\clubsuit \diamondsuit \heartsuit \spadesuit"

# AMS ch-4.2: Math spacing commands
# ANCHOR[id=ams-spacing-symbols]
AMS_SPACING_SYMBOLS = r"\space \thinspace \medspace \thickspace \enspace \quad \qquad \negthinspace \negmedspace \negthickspace \hfill \: \, \; \! ~"

# AMS ch-9.4: Italic Greek letters
# ANCHOR[id=ams-italic-greek-symbols]
AMS_ITALIC_GREEK_SYMBOLS = r"\varGamma \varDelta \varTheta \varLambda \varXi \varPi \varSigma \varUpsilon \varPhi \varPsi \varOmega"

# https://tex.stackexchange.com/questions/381417/what-does-mean-in-latex
# & is special. It is neither a macro or an environment.
# It is a symbol used inside an environment.
# ANCHOR[id=align-symbols]
ALIGN_SYMBOLS = "&"

# Other symbols
OTHER_SYMBOLS = ""

SYMBOLS_SET_LIST = [
    ESCAPED_SYMBOLS,
    LOWER_ASCII_SYMBOLS,
    UPPER_ASCII_SYMBOLS,
    DIGIT_SYMBOLS,
    PUNCTUATION_SYMBOLS,
    LATEX2E_MATH_TEXT_SYMBOLS,
    AMS_MATH_TEXT_SYMBOLS,
    NON_ASCII_SYMBOLS,
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
    NULL_DELIMITER_SYMBOLS,
    DOT_SYMBOLS,
    AMS_DOT_SYMBOLS,
    AMS_ANGLE_SYMBOLS,
    LATEX2E_MISC_MATH_SYMBOLS,
    AMS_MISC_MATH_SYMBOLS,
    LATEX2E_MUSICAL_SYMBOLS,
    LATEX2E_PLAYING_CARD_SUIT_SYMBOLS,
    AMS_SPACING_SYMBOLS,
    AMS_ITALIC_GREEK_SYMBOLS,
    ALIGN_SYMBOLS,
    OTHER_SYMBOLS,
]


def collect_symbols():
    global LATEX_SYMBOLS
    for symbols in SYMBOLS_SET_LIST:
        symbols_list = chars_to_list(symbols)
        LATEX_SYMBOLS.extend(symbols_list)
    LATEX_SYMBOLS = list(OrderedDict.fromkeys(LATEX_SYMBOLS))


collect_symbols()

if __name__ == "__main__":
    logger.back(LATEX_SYMBOLS)
    logger.success(f"[+] {len(LATEX_SYMBOLS)} symbols in {len(SYMBOLS_SET_LIST)} sets.")
