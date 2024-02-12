from pathlib import Path
from pprint import pprint
from tqdm import tqdm
from constants.symbols import LATEX_SYMBOLS
from constants.macros import LATEX_MACROS, AMS_DELIMITER_MACROS
from constants.environments import LATEX_ENVIRONMENTS
from utils.logger import logger
from formers.formula_grammar_checker import FormulaGrammarChecker


class FormulaDatasetAnalyzer:
    IGNORE_ELEMENTS = ["{", "}", "&", "\c", "\d", "#", "\sp"]

    def __init__(self):
        self.dataset_path = Path(__file__).parents[1] / "datasets" / "math.txt"
        self.symbols = []
        self.macros = []
        self.environments = []
        self.invalid_formulas = []
        self.checker = FormulaGrammarChecker()

    def load(self):
        with open(self.dataset_path, "r", encoding="utf-8") as rf:
            self.formulas = [formula.rstrip("\n") for formula in rf.readlines()]

        logger.success(f"{len(self.formulas)} formulas in {self.dataset_path.name}")

    def check_formula(self, formula):
        is_valid, error = self.checker.check(formula)
        return is_valid, error

    def analyze_formula(self, formula):
        elements = formula.split()
        for element in elements:
            for delimiter in AMS_DELIMITER_MACROS.split():
                if element.startswith(delimiter):
                    delimited_element = element[len(delimiter) :]
                    # logger.note(
                    #     f"AMS_DELIMITER_MACROS: {element} of {delimiter} + {element_remain}"
                    # )
                    break
                else:
                    delimited_element = element

            if element in LATEX_SYMBOLS or delimited_element in LATEX_SYMBOLS:
                self.symbols.append(element)
            elif element in LATEX_MACROS or delimited_element in LATEX_MACROS:
                self.macros.append(element)
            elif element.startswith(r"\begin") or element.startswith(r"\end"):
                self.environments.append(element)
            elif element in self.IGNORE_ELEMENTS:
                continue
            elif all(char in LATEX_SYMBOLS for char in element):
                # if all chars in element are symbols
                self.symbols.append(element)
            else:
                raise TypeError(f"Unknown type: {element}")

    def check(self):
        invalid_count = 0
        offset = 119000
        invalid_threshold = 5
        with tqdm(total=len(self.formulas)) as pbar:
            for idx, formula in enumerate(self.formulas[offset:]):
                is_valid, error = self.check_formula(formula)
                if not is_valid:
                    invalid_count += 1
                    invalid_formula = {
                        "line": idx + offset + 1,
                        "error_idx": invalid_count,
                        "error": error,
                        "formula": formula,
                    }
                    self.invalid_formulas.append(invalid_formula)
                    pprint(invalid_formula)
                if invalid_count == invalid_threshold:
                    # pprint(self.invalid_formulas)
                    logger.warn(f"[Stop] Invalid count reached {invalid_threshold}!")
                    break
                # logger.warn(f"Line: {idx+offset+1}")
                invalid_ratio = round(invalid_count / (idx + 1) * 10000, 1)
                pbar.set_postfix(
                    {
                        "invalid": f"{invalid_count:>6} ({invalid_ratio}%%)",
                    }
                )
                pbar.update()

    def analyze(self):
        offset = 0
        with tqdm(total=len(self.formulas)) as pbar:
            for idx, formula in enumerate(self.formulas[offset:]):
                try:
                    self.analyze_formula(formula)
                    symbols_count = len(self.symbols)
                    macros_count = len(self.macros)
                    symbols_ratio = round(
                        symbols_count / (symbols_count + macros_count) * 100, 1
                    )
                    macros_ratio = round(
                        macros_count / (symbols_count + macros_count) * 100, 1
                    )
                    envs_count = len(self.environments)
                    envs_ratio = round(envs_count / (idx + 1) * 100, 1)

                    pbar.set_postfix(
                        {
                            "sym": f"{symbols_count:>6} ({symbols_ratio}%)",
                            "mac": f"{macros_count:>6} ({macros_ratio}%)",
                            "env": f"{envs_count:>6} ({envs_ratio}%)",
                        }
                    )
                    pbar.update()
                except Exception as e:
                    logger.warn(f"Line: {idx+offset+1}")
                    raise e


if __name__ == "__main__":
    analyzer = FormulaDatasetAnalyzer()
    analyzer.load()
    # analyzer.analyze()
    analyzer.check()
