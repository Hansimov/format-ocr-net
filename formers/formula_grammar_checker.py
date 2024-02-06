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

        self.parser = Lark(grammar, start="full_eqn", debug=True)

    def parse(self, expr):
        try:
            res = self.parser.parse(expr)
            print(res.pretty())
            print(f"Valid: {expr}")
        except Exception as e:
            print(e)
            print(f"Invalid: {expr}")


if __name__ == "__main__":
    expr = r"\frac{ab}{cd} + \frac{ef}{gh} = \bar{x} + \bar{b}"
    checker = FormulaGrammarChecker()
    checker.parse(expr)
