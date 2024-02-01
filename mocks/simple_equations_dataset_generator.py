import random
import re
import sympy as sp

from documents.filepath_converter import FilepathConverter
from utils.logger import logger


class SimpleEquationsDatasetGenerator:
    def __init__(self):
        self.dataset_name = "simple_equations"
        self.filepath_converter = FilepathConverter(
            root="datasets", parent=self.dataset_name, ext=".txt"
        )

    def generate(self):
        x, y, z = sp.symbols("x y z")
        ops = [sp.Add, sp.Mul, sp.Pow, sp.sqrt, sp.sin, sp.cos]
        equations_num = 20
        for i in range(equations_num):
            random.seed(i)
            # choose random number of ops and symbols, then combine all to single equation
            num_ops = random.randint(2, 5)
            equation = x
            for _ in range(num_ops):
                op = random.choice(ops)
                symbol = random.choice([x, y, z])
                try:
                    equation = op(equation, symbol)
                except:
                    equation = op(equation)
            # convert equation to string, also add whitespaces among symbols and operators
            logger.note(equation)
            latex_str = sp.latex(equation, mul_symbol="times")
            logger.file(latex_str)
            latex_str = re.sub(r"(?<=\w)\\", r" \\", latex_str)
            latex_str = re.sub(r"([^\s\w\\])", r" \1 ", latex_str)
            latex_str = re.sub(r"\s+", " ", latex_str)
            logger.success(latex_str)
            filepath = self.filepath_converter.hash(latex_str)
            print(filepath)


if __name__ == "__main__":
    generator = SimpleEquationsDatasetGenerator()
    generator.generate()
