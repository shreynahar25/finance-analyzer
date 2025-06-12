import matplotlib.pyplot as plt
import pandas as pd

def get_pie_chart(df):
    df_grouped = df.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    df_grouped.plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    return fig

def get_trend_chart(df):
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df = df.dropna(subset=["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    trend = df.groupby("Month")["Amount"].sum()
    fig, ax = plt.subplots()
    trend.plot(kind="line", marker="o", ax=ax)
    ax.set_ylabel("Total Expenses")
    ax.set_xlabel("Month")
    return fig
