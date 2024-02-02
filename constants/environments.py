from utils.logger import logger
from constants import chars_to_list


LATEX_ENVIRONMENTS = []

# AMS ch-3: Displayed equations
DISPLAYED_EQUATIONS_ENVS = "equation equation* align align* gather gather* alignat alignat* multiline multiline* flalign flalign* split cases"


# AMS ch-4.1: Matrices
MATRIX_ENVS = "pmatrix bmatrix Bmatrix vmatrix Vmatrix smallmatrix"


# Other environments
OTHER_ENVS = ""


ENVIRONMENTS_LIST = [
    DISPLAYED_EQUATIONS_ENVS,
    MATRIX_ENVS,
    OTHER_ENVS,
]


def collect_environments():
    for environments in ENVIRONMENTS_LIST:
        environments_list = chars_to_list(environments)
        LATEX_ENVIRONMENTS.extend(environments_list)


collect_environments()

if __name__ == "__main__":
    logger.note(LATEX_ENVIRONMENTS)
    logger.success(f"[+] {len(LATEX_ENVIRONMENTS)} environments.")
