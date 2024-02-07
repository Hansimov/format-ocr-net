from pathlib import Path
from lark import Lark
from utils.logger import logger


class FormulaGrammarChecker:
    def __init__(self):
        self.grammar_filepath = Path(__file__).parent / "formula_grammar.lark"
        self.init_parser()

    def init_parser(self):
        with open(self.grammar_filepath, "r") as rf:
            # escape the backslash (\) in .lark file
            grammar = rf.read().replace("\\", "\\\\")

        self.parser = Lark(grammar, start="full_eqn", parser="lalr")

    def check(self, expr, verbose=False):
        try:
            res = self.parser.parse(expr)
            if verbose:
                print(res.pretty())
                logger.success(f"Valid: {expr}")
        except Exception as e:
            print(e)
            logger.warn(f"Invalid: {expr}")
            raise e


if __name__ == "__main__":
    exprs = [
        # r"{ a b c } ",
        # r"G ( 0, 1 ) H ( 2, 3 )",
        # r"\bar{x}",
        # r"\bar{x y}",
        # r"\frac{a}{b}",
        # r"\frac ab",
        # r"\frac a b c",
        # r"\frac{ab}{cd}",
        # r"\frac{ab}{cd} + \frac{ef}{gh} = \bar{x} + \bar{b}",
        # r"G ( 0 , t ^ { \prime \prime } ; 0 , t ^ { \prime \prime } ) = i \int \int \frac { d \omega ^ { \prime \prime } } { 2 \pi } \frac { d k ^ { \prime \prime } } { 2 \pi } P _ { 0 } ( \omega ^ { \prime \prime } , k ^ { \prime \prime } )",
        r"{ \frac { \phi ^ { \prime \prime } } { A } } + { \frac { 1 } { A } } \left( - { \frac { 1 } { 2 } } { \frac { A ^ { \prime } } { A } } + 2 { \frac { B ^ { \prime } } { B } } + { \frac { 2 } { r } } \right) \phi ^ { \prime } - { \frac { 2 } { r ^ { 2 } } } \phi - \lambda \phi ( \phi ^ { 2 } - \eta ^ { 2 } ) = 0 \, .",
        # r"E _ { A D M } = \frac { 1 } { 1 6 \pi G _ { 1 0 } } \oint _ { \infty } d \Sigma ^ { m } \lbrace { } ^ { \circ } D _ { n } g _ { m p } - { } ^ { \circ } D _ { m } g _ { n p } \rbrace { } ^ { \circ } g ^ { n p }",
    ]
    checker = FormulaGrammarChecker()
    for expr in exprs:
        checker.check(expr, verbose=True)
