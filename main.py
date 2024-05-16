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
    invoice_nr, invoice_date = number_date
    txt = f"Invoice No. {invoice_nr}\nDate: {invoice_date}"
    df = pd.read_excel(f, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="a4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    pdf.multi_cell(w=0, h=10, txt=txt, align="L")
    columns = df.columns
    columns = [col.replace("_", " ").title() for col in columns]
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=30, h=10, border=1, txt=columns[0], align="L")
    pdf.cell(w=50, h=10, border=1, txt=columns[1], align="L")
    pdf.cell(w=40, h=10, border=1, txt=columns[2], align="L")
    pdf.cell(w=30, h=10, border=1, txt=columns[3], align="L")
    pdf.cell(w=30, h=10, border=1, txt=columns[4], align="L", ln=1)
    pdf.set_font(family="Times", size=12)
    for index, row in df.iterrows():
        pdf.cell(w=30, h=10, border=1, txt=str(row["product_id"]), align="L")
        pdf.cell(w=50, h=10, border=1, txt=row["product_name"], align="L")
        pdf.cell(w=40, h=10, border=1, txt=str(row["amount_purchased"]),
                 align="R")
        pdf.cell(w=30, h=10, border=1, txt=str(row["price_per_unit"]),
                 align="R")
        pdf.cell(w=30, h=10, border=1, txt=str(row["total_price"]),
                 align="R", ln=1)
    pdf.cell(w=150, h=10, border=0, txt="Total amount payable:", align="R")
    total = df["total_price"].sum()
    pdf.cell(w=30, h=10, border=1, txt=str(total), align="R", ln=1)
    pdf.ln(10)
    pdf.set_font(family="Times", size=14)
    pdf.cell(w=0, h=10, border=0, txt=f"The total amount is {total} Euros.", align="L", ln=1)
    pdf.cell(w=0, h=10, border=0, txt="Fake Factory", align="L", ln=1)
    pdf.image(name="data/pythonhow.png", w=25, h=25)

    pdf.output(f"output/{inv_filename}.pdf")
