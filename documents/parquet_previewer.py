from pathlib import Path
import pandas as pd


class ParquetPreviewer:
    def __init__(self):
        self.parquet_root = Path(__file__).parents[1] / "datasets" / "parquets"

    def preview(self, file_pattern):
        file_fullpaths = list(self.parquet_root.glob(file_pattern))
        for file in file_fullpaths:
            file_fullpath = file
            df = pd.read_parquet(file_fullpath)
            print(df.columns)
            print(df.head())


if __name__ == "__main__":
    previewer = ParquetPreviewer()
    file_pattern = "train*"
    previewer.preview(file_pattern=file_pattern)
