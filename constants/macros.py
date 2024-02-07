from collections import OrderedDict
from utils.logger import logger
from constants import chars_to_list

LATEX_MACROS = []

# ANCHOR[id=display-style-macros]
DISPLAY_STYLE_MACROS = r"\displaystyle"

# ANCHOR[id=sub-sup-macros]
SUB_SUP_MACROS = r"_ ^"

# Table 259: Math-mode Accents
# ANCHOR[id=math-mode-accent-macros]
MATH_MODE_ACCENT_MACROS = (
    r"\acute \bar \breve \check \ddot \dot \grave \hat \mathring \tilde \vec"
)

# Table 260: [AMS] Math-mode Accents
# ANCHOR[id=ams-math-mode-accent-macros]
AMS_MATH_MODE_ACCENT_MACROS = r"\dddot \ddddot"

# Table 270: Extensible Accents
# ANCHOR[id=extensible-accent-macros]
EXTENSIBLE_ACCENT_MACROS = r"\overbrace \overline \overleftarrow \overrightarrow \sqrt \underbrace \underline \widehat \widetilde"

# Table 271: [overrightarrow] Extensible Accents
# ANCHOR[id=overrightarrow-extensible-accent-macros]
OVERRIGHTARROW_EXTENSIBLE_ACCENT_MACROS = r"\Overrightarrow"

# Table 273: [AMS] Extensible Accents
# ANCHOR[id=ams-extensible-accent-macros]
AMS_EXTENSIBLE_ACCENT_MACROS = (
    r"\overleftrightarrow \underleftarrow \underleftrightarrow \underrightarrow"
)

# Table 288: AMS Extensible Arrows
# ANCHOR[id=ams-extensible-arrow-macros]
AMS_EXTENSIBLE_ARROW_MACROS = r"\xleftarrow \xrightarrow"

# Table 348: Math Alphabets
# ANCHOR[id=math-alphabet-macros]
MATH_ALPHABET_MACROS = r"\mathrm \mathit \mathnormal \mathcal \mathscr \mathbb"

# Table 689: Sample resized delimiters
# ANCHOR[id=vertical-resize-macros]
VERTICAL_RESIZE_MACROS = r"\big \Big \bigg \Bigg"

# Table 693: Producing bold mathematical symbols
# ANCHOR[id=bold-math-font-macros]
BOLD_MATH_FONT_MACROS = r"\mathbf \pmb \boldsymbol"


# === AMS MATH === #

# AMS ch-4.1: Matrices
# ANCHOR[id=ams-matrix-dot-macros]
AMS_MATRIX_DOT_MACROS = r"\hdotsfor"

# AMS ch-4.7: Boxed formulas
# ANCHOR[id=ams-boxed-macros]
AMS_BOXED_MACROS = r"\boxed"

# AMS ch-4.10: Affixing symbols to other symbols
# `\stackrel` is used to create stacked relationship, #1 is stacked on top of #2.
#   - syntax: { \stackrel {#1} {#2} }
#   - https://www.tutorialspoint.com/tex_commands/stackrel.htm
# ANCHOR[id=ams-affix-macros]
AMS_AFFIX_MACROS = r"\stackrel \overset \underset"

# AMS ch-4.11: Fractions and related constructions
# ANCHOR[id=ams-frac-macros]
AMS_FRAC_MACROS = r"\frac \dfrac \tfrac \cfrac \binom \dbinom \tbinom"

# AMS ch-4.14: Delimiters
# ANCHOR[id=ams-delimiter-macros]
AMS_DELIMITER_MACROS = (
    r"\left \right \bigl \bigr \Bigl \Bigr \biggl \biggr \Biggl \Biggr"
)

# AMS ch-5.1: Operator names
# ANCHOR[id=ams-operator-name-macros]
AMS_OPERATOR_NAME_MACROS = r"\operatorname \operatorname* \mathop"

# AMS ch-5.2: mod and relatives
#   \mod and \pod are variants of \pmod preferred by some authors;
#   \mod omits the parentheses, whereas \pod omits the “mod” and retains the parentheses
# ANCHOR[id=ams-mod-macros]
AMS_MOD_MACROS = r"\mod \bmod \pmod \pod"

# AMS ch-6: The \text command
# ANCHOR[id=ams-text-font-macros]
AMS_TEXT_FONT_MACROS = (
    r"\text \textrm \textbf \textit \texttt \textsf \textup \textnormal"
)

# AMS ch-7.1: Multiline subscripts and superscripts
# `\substack` draws multi-line subscripts or superscripts.
#   - syntax: { \sum_{\substack{0<i<m\\0<j<n}} P(i,j) }
# ANCHOR[id=ams-substack-macros]
AMS_SUBSTACK_MACROS = r"\substack"

# AMS ch-7.2: The \sideset command
# `\sideset` is used for putting symbols at the four 'corners' of a large operator.
#   - syntax: { \sideset{_#1^#2}{_#3^#4} <large_operator> }
#   - https://www.tutorialspoint.com/tex_commands/sideset.htm
# `\limits` is used to set limits above/below any token of class OP.
#   - syntax: { \int\limits_a^b f(x)dx }
#   - https://www.tutorialspoint.com/tex_commands/limits.htm
# \nolimits is used to change the default placement of limits; only allowed on items of class OP.
#   - syntax: { \sum\nolimits_{k=1}^n a_k }
#   - https://www.tutorialspoint.com/tex_commands/nolimits.htm
# ANCHOR[id=ams-sideset-macros]
AMS_SIDESET_MACROS = r"\sideset \limits \nolimits"

# AMS ch-9.1: Using math fonts
# ANCHOR[id=ams-math-font-macros]
AMS_MATH_FONT_MACROS = r"\mathbf \mathrm \mathcal \mathsf \mathtt \mathit \mathfrak"

# https://katex.org/docs/supported#style-color-size-and-font
# ANCHOR[id=short-ams-math-font-macros]
SHORT_AMS_MATH_FONT_MACROS = r"\bf \rm \cal \sf \tt \it \bm \it \frak \mit"

# https://www.overleaf.com/learn/latex/Questions/How_do_I_adjust_the_font_size%3F
# ANCHOR[id=font-size-macros]
FONT_SIZE_MACROS = r"\tiny \scriptsize \footnotesize \small \normalsize \large \Large \LARGE \huge \Huge \scriptstyle \scriptscriptstyle"

# remove the tag or number from the equation
# ANCHOR[id=no-tag-macros]
NO_TAG_MACROS = r"\nonumber \notag"

# https://docs.moodle.org/403/en/Chemistry_notation_using_mhchem
CHEMISTRY_NOTATION_MACROS = "\ce"

# Other macros
OTHER_MACROS = r""


MACROS_SET_LIST = [
    DISPLAY_STYLE_MACROS,
    SUB_SUP_MACROS,
    MATH_MODE_ACCENT_MACROS,
    AMS_MATH_MODE_ACCENT_MACROS,
    EXTENSIBLE_ACCENT_MACROS,
    OVERRIGHTARROW_EXTENSIBLE_ACCENT_MACROS,
    AMS_EXTENSIBLE_ACCENT_MACROS,
    AMS_EXTENSIBLE_ARROW_MACROS,
    MATH_ALPHABET_MACROS,
    VERTICAL_RESIZE_MACROS,
    BOLD_MATH_FONT_MACROS,
    AMS_MATRIX_DOT_MACROS,
    AMS_BOXED_MACROS,
    AMS_AFFIX_MACROS,
    AMS_FRAC_MACROS,
    AMS_DELIMITER_MACROS,
    AMS_OPERATOR_NAME_MACROS,
    AMS_MOD_MACROS,
    AMS_TEXT_FONT_MACROS,
    AMS_SUBSTACK_MACROS,
    AMS_SIDESET_MACROS,
    AMS_MATH_FONT_MACROS,
    SHORT_AMS_MATH_FONT_MACROS,
    FONT_SIZE_MACROS,
    NO_TAG_MACROS,
    CHEMISTRY_NOTATION_MACROS,
    OTHER_MACROS,
]


def collect_macros():
    global LATEX_MACROS
    for macros in MACROS_SET_LIST:
        macros_list = chars_to_list(macros)
        LATEX_MACROS.extend(macros_list)
    LATEX_MACROS = list(OrderedDict.fromkeys(LATEX_MACROS))


collect_macros()

if __name__ == "__main__":
    logger.back(LATEX_MACROS)
    logger.success(f"[+] {len(LATEX_MACROS)} macros in {len(MACROS_SET_LIST)} sets.")
