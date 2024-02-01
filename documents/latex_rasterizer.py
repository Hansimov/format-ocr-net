import os
import glob
from pathlib import Path
from documents.filepath_converter import FilepathConverter, auto_makedir
from utils.logger import logger, shell_cmd


class LatexRasterizer:
    def __init__(self):
        self.dataset_name = "latex"
        self.tex_path_converter = FilepathConverter(
            root="datasets", parent=self.dataset_name, ext=".tex"
        )
        self.image_path_converter = FilepathConverter(
            root="datasets", parent=self.dataset_name, ext=".png"
        )

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
    from samples.equations import equations

    rasterizer = LatexRasterizer()
    rasterizer.rasterize(latex_str=equations[1])
