# NOTES: Most symbols, macros and environements are taken form following references:
# - The Comprehensive LaTeX Symbol List - The CTAN archive
#   - https://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf
# - User's Guide for the amsmath Package (Version 2.1)
#   - https://mirror.nyist.edu.cn/CTAN/macros/latex/required/amsmath/amsldoc.pdf
# - LaTeX/Mathematics - Wikibooks
#   - https://en.wikibooks.org/wiki/LaTeX/Mathematics
#   - https://en.wikibooks.org/wiki/LaTeX/Advanced_Mathematics
# Symbols:LaTeX Commands - ProofWiki
#   - https://proofwiki.org/wiki/Symbols:LaTeX_Commands

# Supported packages in MathJax and KaTeX
# - https://docs.mathjax.org/en/latest/input/tex/macros/index.html
# - https://github.com/KaTeX/KaTeX/wiki/Package-Emulation

LATEX_PACKAGES = "amsmath amsfonts amssymb arydshln bm cancel color fontenc hyperref latexsym mathrsfs mathtools overrightarrow textcomp ulem unicode-math"

# Notes: Following packages supported by KaTeX are not included by tex-live-extra:
#   `extpfeil`, `mathabx`, `MnSymbol`, `statmath`, `stix`, `stmaryrd`, `undertilde`


def chars_to_list(chars) -> list:
    return chars.split()
