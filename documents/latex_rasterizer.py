import os
import glob
from pathlib import Path
from sympy import sin, sqrt, symbols, preview
from documents.filepath_converter import (
    LatexToFilepathConverter,
    LatexImageToFilepathConverter,
    auto_makedir,
)
from utils.logger import logger, shell_cmd


class LatexRasterizer:
    def __init__(self):
        self.image_path_converter = LatexImageToFilepathConverter()
        self.tex_path_converter = LatexToFilepathConverter()

    def str_to_tex(self, str):
        tex = (
            f"\\documentclass[preview, border=5pt]{{standalone}}\n"
            f"\\usepackage{{amsmath}}\n"
            f"\\begin{{document}}\n"
            f"$\\displaystyle\n"
            f"{str}\n"
            f"$\n"
            f"\\end{{document}}\n"
        )
        return tex

    def latex_command(self, tex_filepath):
        cmd = f'pdflatex -interaction=batchmode -output-format=dvi -output-directory="{tex_filepath.parent}" "{tex_filepath}" > /dev/null 2>&1'
        return cmd

    def dvipng_command(self, tex_filepath, image_filepath):
        dvi_filepath = tex_filepath.with_suffix(".dvi")
        cmd = f'dvipng -D 300 -o "{image_filepath}" "{dvi_filepath}" > /dev/null 2>&1'
        return cmd

    def remove_temp_files(self, tex_filepath):
        temp_exts = [".aux", ".dvi", ".log"]
        folder = tex_filepath.parent
        for ext in temp_exts:
            temp_files = glob.glob(str(folder / f"*{ext}"))
            for temp_file in temp_files:
                os.remove(temp_file)

    def rasterize(self, latex_str):
        tex_filepath = self.tex_path_converter.hash(latex_str)
        image_filepath = self.image_path_converter.hash(latex_str)
        tex = self.str_to_tex(latex_str)
        auto_makedir(tex_filepath)
        with open(tex_filepath, "w") as wf:
            wf.write(tex)
        latex_command_str = self.latex_command(tex_filepath)
        dvipng_command_str = self.dvipng_command(tex_filepath, image_filepath)
        shell_cmd(latex_command_str)
        shell_cmd(dvipng_command_str)
        self.remove_temp_files(tex_filepath)


if __name__ == "__main__":
    rasterizer = LatexRasterizer()
    # latex_str = "sqrt(sin(x)+1)"
    latex_str = r"\begin{array} { r c l } { { \epsilon } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 } \left( 1 - \frac { q _ { 2 } } { p _ { 2 } } \frac { \bar { A } _ { 0 } } { A _ { 0 } } \right) } , } } \\ { { \epsilon ^ { \prime } } } & { { = } } & { { \displaystyle { \frac { 1 } { 2 \sqrt { 2 } } e ^ { i ( \delta _ { 2 } - \delta _ { 0 } ) } \left[ - \omega \left( 1 - \frac { q _ { 2 } } { p _ { 2 } } \right) + \left( \frac { p _ { 2 } A _ { 2 } - q _ { 2 } \bar { A } _ { 2 } } { p _ { 2 } A _ { 0 } } \right) \right] } . } } \end{array}"
    rasterizer.rasterize(latex_str=latex_str)
