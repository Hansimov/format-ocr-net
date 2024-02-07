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

        self.parser = Lark(grammar, start="latex_eqn", parser="lalr")

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
    from samples.exprs import exprs

    checker = FormulaGrammarChecker()
    for expr in exprs:
        checker.check(expr, verbose=True)
