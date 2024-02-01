from pathlib import Path
from sympy import sin, sqrt, symbols, preview
from documents.filepath_converter import LatexImageToFilepathConverter, auto_makedir


class LatexRasterizer:
    def __init__(self):
        self.filepath_converter = LatexImageToFilepathConverter()
        self.init_preamble()

    def init_preamble(self):
        self.preamble = """
            \\documentclass[border=1em]{standalone}
            \\begin{document}
        """

    def rasterize(self, latex_str):
        output_filepath = self.filepath_converter.convert(latex_str)
        auto_makedir(output_filepath)
        preview(
            latex_str,
            viewer="file",
            output="png",
            filename=output_filepath,
            preamble=self.preamble,
            dvioptions=["-D", "400"],
        )


if __name__ == "__main__":
    rasterizer = LatexRasterizer()
    latex_str = "sqrt(sin(x)+1)"
    rasterizer.rasterize(latex_str=latex_str)
