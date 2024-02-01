import platform
from pathlib import Path


# What characters are forbidden in Windows and Linux directory names?
#   https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names

INVALID_FILE_PATH_CHARS = [
    "\\",
    "/",
    ":",
    "*",
    "?",
    '"',
    "<",
    ">",
    "|",
    "\n",
    "\t",
    "\r",
    *[chr(i) for i in range(32)],
]

WINDOWS_INVALID_FILE_PATH_NAMES = [
    "con",
    "prn",
    "aux",
    "nul",
    *[f"com{i+1}" for i in range(10)],
    *[f"lpt{i+1}" for i in range(10)],
]


class FilepathConverter:
    def __init__(self, root=None, parent=None, ext=None, accept_exts=[]):
        self.output_root = root or Path(__file__).parents[1] / "datasets"
        self.parent = parent
        self.ext = ext
        self.accept_exts = accept_exts or [ext]

    def preprocess(self, input_string):
        return input_string

    def validate(self, input_string):
        if not input_string:
            return input_string
        filename = input_string
        for char in INVALID_FILE_PATH_CHARS:
            filename = filename.replace(char, "_")
        if platform.system() == "Windows":
            filename_base = filename.split(".")[0]
            if filename_base.lower() in WINDOWS_INVALID_FILE_PATH_NAMES:
                filename_base = filename_base + "_"
                filename = ".".join([filename_base, *filename.split(".")[1:]])
        return filename

    def append_extension(self, filename):
        filename_ext = "." + filename.split(".")[-1]
        if filename_ext.lower() not in self.accept_exts:
            filename += self.ext
        return filename

    def convert(self, input_string, parent=None):
        filename = self.preprocess(input_string)
        filename = self.validate(filename)
        filename = self.append_extension(filename)

        parent = parent or self.parent
        parent = self.validate(parent)
        if parent:
            filepath = self.output_root / parent / filename
        else:
            filepath = self.output_root / filename

        self.filename = filename
        self.filepath = filepath

        return self.filepath


class LatexToFilepathConverter(FilepathConverter):
    def __init__(self, root=None, parent=None):
        super().__init__(root=root, parent=parent, ext=".tex")
        self.output_root = self.output_root / "latex"


class LatexImageToFilepathConverter(FilepathConverter):
    def __init__(self, root=None, parent=None):
        super().__init__(root=root, parent=parent, ext=".png")
        self.output_root = self.output_root / "latex"


def auto_makedir(filepath: Path):
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    latex_str = "sqrt(sin(x)+1)"
    converter = LatexImageToFilepathConverter()
    print(converter.convert(latex_str))
