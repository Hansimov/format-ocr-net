from pathlib import Path
from lark import Lark


class FormulaGrammarChecker:
    def __init__(self):
        self.grammar_filepath = Path(__file__).parent / "formula_grammar.lark"
        self.init_parser()

    def init_parser(self):
        with open(self.grammar_filepath, "r") as rf:
            # escape the backslash (\) in .lark file
            grammar = rf.read().replace("\\", "\\\\")

        self.parser = Lark(grammar, start="full_eqn")

    def parse(self, expr):
        try:
            res = self.parser.parse(expr)
            print(res.pretty())
            print(f"Valid: {expr}")
        except Exception as e:
            print(e)
            print(f"Invalid: {expr}")


if __name__ == "__main__":
    # expr = r"\frac{ab}{cd} + \frac{ef}{gh} = \bar{x} + \bar{b}"
    # expr = r"{ a b }"
    # expr = r"G ( 0, 1 )"
    expr = r"G ( 0 , t ^ { \prime \prime } ; 0 , t ^ { \prime \prime } ) = i \int \int \frac { d \omega ^ { \prime \prime } } { 2 \pi } \frac { d k ^ { \prime \prime } } { 2 \pi } P _ { 0 } ( \omega ^ { \prime \prime } , k ^ { \prime \prime } )"
    checker = FormulaGrammarChecker()
    checker.parse(expr)
