from pathlib import Path
from tqdm import tqdm
from constants.symbols import LATEX_SYMBOLS
from constants.macros import LATEX_MACROS, AMS_DELIMITER_MACROS
from constants.environments import LATEX_ENVIRONMENTS
from utils.logger import logger


class FormulaDatasetAnalyzer:
    IGNORE_ELEMENTS = ["{", "}", "&", "\c", "\d", "#"]

    def __init__(self):
        self.dataset_path = Path(__file__).parents[1] / "datasets" / "math.txt"

    def load(self):
        with open(self.dataset_path, "r", encoding="utf-8") as rf:
            self.formulas = rf.readlines()

        logger.success(f"{len(self.formulas)} formulas in {self.dataset_path.name}")

    def analyze_formula(self, formula):
        elements = formula.split()
        symbols = []
        macros = []
        environments = []
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
                symbols.append(element)
            elif element in LATEX_MACROS or delimited_element in LATEX_MACROS:
                macros.append(element)
            elif element.startswith(r"\begin") or element.startswith(r"\end"):
                environments.append(element)
            elif element in self.IGNORE_ELEMENTS:
                continue
            elif all(char in LATEX_SYMBOLS for char in element):
                # if all chars in element are symbols
                symbols.append(element)
            else:
                raise TypeError(f"Unknown type: {element}")

    def analyze(self):
        offset = 0
        for idx, formula in enumerate(tqdm(self.formulas[offset:])):
            try:
                self.analyze_formula(formula)
            except Exception as e:
                logger.warn(f"Line: {idx+offset+1}")
                raise e


if __name__ == "__main__":
    analyzer = FormulaDatasetAnalyzer()
    analyzer.load()
    analyzer.analyze()
