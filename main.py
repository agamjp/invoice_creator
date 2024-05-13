from fpdf import FPDF
import pandas as pd
from pathlib import Path
import glob
# alternative: import os
# files = os.listdir("data")
# (adjust the loop accordingly)

files = glob.glob("data/*.xlsx")

for f in files:
    inv_filename = Path(f).stem
    number_date = inv_filename.split("-")
    invoice_nr = number_date[0]
    invoice_date = number_date[1]
    txt = f"Invoice No. {invoice_nr}\nDate: {invoice_date}"
    df = pd.read_excel(f, sheet_name="Sheet 1")
    print(df)
    pdf = FPDF(orientation="P", unit="mm", format="a4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    pdf.multi_cell(w=0, h=14, txt=txt, align="L")

    pdf.output(f"output/{inv_filename}.pdf")
