import pandas as pd


def load_data(path):
    return pd.read_csv(path, sep=";")


if __name__ == "__main__":
    df = load_data("../data/student-mat.csv")
    print(df.head())