import random
import re
import string
import sympy as sp
from tqdm import tqdm
import pandas as pd

from documents.filepath_converter import FilepathConverter
from documents.latex_rasterizer import LatexRasterizer
from utils.logger import logger


class SimpleEquationsDatasetGenerator:
    def __init__(self):
        self.dataset_name = "simple_equations"
        self.filepath_converter = FilepathConverter(
            root="datasets", parent=self.dataset_name, ext=".txt"
        )
        self.latex_rasterizer = LatexRasterizer(
            root="datasets", parent=self.dataset_name
        )
        self.ops = [sp.Add, sp.Mul, sp.Pow, sp.sqrt, sp.sin, sp.cos, sp.exp]
        self.re_sub_patterns = [
            [r"(?<=\w)\\", r" \\"],
            [r"([^\s\w\\])", r" \1 "],
            [r"\s+", " "],
        ]

    def random_symbol(self, max_len=2):
        # generate a symbol of [a-zA-Z0-9]+, with length <= max_len
        symbol_str = "".join(random.choices(string.ascii_letters))
        symbol_str += "".join(
            random.choices(
                string.ascii_letters + string.digits, k=random.randint(1, max_len - 1)
            )
        )
        symbol = sp.symbols(symbol_str)
        return symbol

    def random_equation(self, ops_num_range=[2, 10]):
        # choose random number of ops and symbols, then combine all to single equation
        ops_num = random.randint(*ops_num_range)
        equation = self.random_symbol()
        for _ in range(ops_num):
            op = random.choice(self.ops)
            symbol = self.random_symbol()
            try:
                equation = op(equation, symbol)
            except:
                equation = op(equation)
        # convert equation to string, also add whitespaces among symbols and operators
        logger.note(equation)
        latex_str = sp.latex(equation, mul_symbol="times")
        for pattern, replaced in self.re_sub_patterns:
            latex_str = re.sub(pattern, replaced, latex_str)
        filepath = self.filepath_converter.hash(latex_str)
        return {
            "hash": filepath.stem,
            "equation": repr(equation),
            "latex": latex_str,
        }

    def generate(self):
        # self.train_df = pd.DataFrame()
        # self.train_df.columns = ["hash", "equation", "latex", "image"]
        equations_num = 1
        for i in tqdm(range(equations_num)):
            random.seed(i)
            item = self.random_equation()
            self.latex_rasterizer.rasterize(item["latex"])


if __name__ == "__main__":
    generator = SimpleEquationsDatasetGenerator()
    generator.generate()
