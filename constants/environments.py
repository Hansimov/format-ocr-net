from utils.logger import logger
from constants import chars_to_list


LATEX_ENVIRONMENTS = []

# AMS ch-3: Displayed equations
AMS_EQUATIONS_ENVS = "equation equation* subequations align align* gather gather* alignat alignat* multiline multiline* flalign flalign* cases array eqnarray eqnarray*"

LOW_LEVEL_AMS_EQUATIONS_ENVS = "gathered aligned alignedat split"


# AMS ch-4.1: Matrices
AMS_MATRIX_ENVS = "matrix pmatrix pmatrix* bmatrix bmatrix* Bmatrix Bmatrix* vmatrix vmatrix* Vmatrix Vmatrix* smallmatrix"


# Other environments
OTHER_ENVS = ""


ENVIRONMENTS_LIST = [
    AMS_EQUATIONS_ENVS,
    LOW_LEVEL_AMS_EQUATIONS_ENVS,
    AMS_MATRIX_ENVS,
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
