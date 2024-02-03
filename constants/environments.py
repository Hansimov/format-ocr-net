from collections import OrderedDict
from utils.logger import logger
from constants import chars_to_list


LATEX_ENVIRONMENTS = []

# AMS ch-3: Displayed equations
AMS_EQUATIONS_ENVS = "equation equation* subequations align align* gather gather* alignat alignat* multiline multiline* flalign flalign* cases array eqnarray eqnarray* subarray"

LOW_LEVEL_AMS_EQUATIONS_ENVS = "gathered aligned alignedat split"

# AMS ch-4.1: Matrices
AMS_MATRIX_ENVS = "matrix pmatrix pmatrix* bmatrix bmatrix* Bmatrix Bmatrix* vmatrix vmatrix* Vmatrix Vmatrix* smallmatrix"


# Other environments
OTHER_ENVS = ""


ENVIRONMENTS_SET_LIST = [
    AMS_EQUATIONS_ENVS,
    LOW_LEVEL_AMS_EQUATIONS_ENVS,
    AMS_MATRIX_ENVS,
    OTHER_ENVS,
]


def collect_environments():
    global LATEX_ENVIRONMENTS
    for environments in ENVIRONMENTS_SET_LIST:
        environments_list = chars_to_list(environments)
        LATEX_ENVIRONMENTS.extend(environments_list)
    LATEX_ENVIRONMENTS = list(OrderedDict.fromkeys(LATEX_ENVIRONMENTS))


collect_environments()

if __name__ == "__main__":
    logger.back(LATEX_ENVIRONMENTS)
    logger.success(
        f"[+] {len(LATEX_ENVIRONMENTS)} environments in {len(ENVIRONMENTS_SET_LIST)} sets."
    )
