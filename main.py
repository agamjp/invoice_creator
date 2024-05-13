import os
from fpdf import FPDF
import pandas as pd

files = os.listdir("data")

for f in files:
    if f.endswith(".xlsx"):
        df = pd.read_excel(f"data/{f}")
        print(df)
