import pdfplumber
import pandas as pd
import io

def parse(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Dummy parser logic - replace with actual parsing rules
    data = []
    for line in text.split("\n"):
        parts = line.split()
        if len(parts) >= 3:
            try:
                amount = float(parts[-1].replace(",", "").replace("₹", ""))
                date = parts[0]
                description = " ".join(parts[1:-1])
                data.append([date, description, amount])
            except:
                continue
    df = pd.DataFrame(data, columns=["Date", "Description", "Amount"])
    return df
