import pandas as pd

CATEGORY_KEYWORDS = {
    "Groceries": ["bigbasket", "grofers", "supermarket"],
    "Dining": ["swiggy", "zomato", "restaurant", "cafe"],
    "Travel": ["uber", "ola", "air", "rail", "hotel"],
    "Entertainment": ["netflix", "spotify", "prime"],
    "Bills": ["electricity", "bill", "water", "gas"],
}

def categorize(df):
    df["Category"] = "Uncategorized"
    for cat, keywords in CATEGORY_KEYWORDS.items():
        df.loc[df["Description"].str.lower().str.contains("|".join(keywords)), "Category"] = cat
    return df

def suggest_tags(df):
    suggestions = df.copy()
    suggestions["Suggested Category"] = "Other"
    for cat, keywords in CATEGORY_KEYWORDS.items():
        mask = suggestions["Description"].str.lower().str.contains("|".join(keywords))
        suggestions.loc[mask, "Suggested Category"] = cat
    return suggestions
