from utils.logger import logger
from constants import chars_to_list

LATEX_MACROS = []

DISPLAY_STYLE_MACROS = r"\displaystyle \textstyle \scriptstyle \scriptscriptstyle"

# Table 259: Math-mode Accents
MATH_MODE_ACCENT_MACROS = (
    r"\acute \bar \breve \check \ddot \dot \grave \hat \mathring \tilde \vec"
)

# Table 260: [AMS] Math-mode Accents
AMS_MATH_MODE_ACCENT_MACROS = r"\dddot \ddddot"

# Table 270: Extensible Accents
EXTENSIBLE_ACCENT_MACROS = r"\widetilde \overleftarrow \overline \overbrace \sqrt \widehat \overrightarrow \underline \underbrace"

# Table 271: [overrightarrow] Extensible Accents
OVERRIGHTARROW_EXTENSIBLE_ACCENT_MACROS = r"\Overrightarrow"

# Table 273: [AMS] Extensible Accents
AMS_EXTENSIBLE_ACCENT_MACROS = (
    r"\overleftrightarrow \underleftarrow \underleftrightarrow \underrightarrow"
)

# Table 288: AMS Extensible Arrows
AMS_EXTENSIBLE_ARROW_MACROS = r"\xleftarrow \xrightarrow"

# Table 348: Math Alphabets
MATH_ALPHABET_MACROS = r"\mathrm \mathit \mathnormal \mathcal \mathscr \mathbb"


# === AMS MATH === #

# AMS ch-4.1: Matrices
AMS_MATRIX_DOT_MACROS = r"\hdotsfor"

# AMS ch-4.7: Boxed formulas
AMS_BOXED_MACROS = r"\boxed"

# AMS ch-4.10: Affixing symbols to other symbols
AMS_AFFIX_MACROS = r"\stackrel \overset \underset"

# AMS ch-4.11: Fractions and related constructions
AMS_FRAC_MACROS = r"\frac \dfrac \tfrac \binom \dbinom \tbinom \cfrac"

# AMS ch-4.14: Delimiters
AMS_DELIMITER_MACROS = (
    r"\left \right \bigl \bigr \Bigl \Bigr \biggl \biggr \Biggl \Biggr"
)

# AMS ch-5.1: Operator names
AMS_OPERATOR_NAME_MACROS = r"\operatorname \operatorname*"

# AMS ch-5.2: mod and relatives
#   \mod and \pod are variants of \pmod preferred by some authors;
#   \mod omits the parentheses, whereas \pod omits the “mod” and retains the parentheses
AMS_MOD_MACROS = r"\mod \bmod \pmod \pod"

# AMS ch-6: The \text command
AMS_TEXT_MACRO = r"\text \textrm \textbf \textit"

# AMS ch-7.1: Multiline subscripts and superscripts
AMS_SUBSTACK_MACROS = r"\substack"

# AMS ch-7.2: The \sideset command
AMS_SIDESET_MACROS = r"\sideset \limits \nolimits"

# AMS ch-9.1: Using math fonts
AMS_MATH_FONT_MACROS = r"\mathbf \mathrm \mathcal \mathsf \mathtt \mathit \mathfrak"

# Other macros
OTHER_MACROS = r""


MACROS_SET_LIST = [
    DISPLAY_STYLE_MACROS,
    MATH_MODE_ACCENT_MACROS,
    AMS_MATH_MODE_ACCENT_MACROS,
    EXTENSIBLE_ACCENT_MACROS,
    OVERRIGHTARROW_EXTENSIBLE_ACCENT_MACROS,
    AMS_EXTENSIBLE_ACCENT_MACROS,
    AMS_EXTENSIBLE_ARROW_MACROS,
    MATH_ALPHABET_MACROS,
    AMS_MATRIX_DOT_MACROS,
    AMS_BOXED_MACROS,
    AMS_AFFIX_MACROS,
    AMS_FRAC_MACROS,
    AMS_DELIMITER_MACROS,
    AMS_OPERATOR_NAME_MACROS,
    AMS_MOD_MACROS,
    AMS_TEXT_MACRO,
    AMS_SUBSTACK_MACROS,
    AMS_SIDESET_MACROS,
    AMS_MATH_FONT_MACROS,
    OTHER_MACROS,
]


def collect_macros():
    global LATEX_MACROS
    for macros in MACROS_SET_LIST:
        macros_list = chars_to_list(macros)
        LATEX_MACROS.extend(macros_list)
    LATEX_MACROS = list(set(LATEX_MACROS))


collect_macros()

if __name__ == "__main__":
    logger.back(LATEX_MACROS)
    logger.success(f"[+] {len(LATEX_MACROS)} macros in {len(MACROS_SET_LIST)} sets.")
