import pandas as pd

def parse(file):
    df = pd.read_csv(file)
    # Ensure standard columns
    df.columns = [col.strip().capitalize() for col in df.columns]
    if "Category" not in df.columns:
        df["Category"] = "Uncategorized"
    return df
