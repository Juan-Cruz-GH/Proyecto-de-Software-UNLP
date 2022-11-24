from fpdf import FPDF
from datetime import datetime
from flask import make_response, render_template


class PDFCarnet(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.set_xy(0, 0)
        self.cell(200, 40, "", 0, 0, "R")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, "Page" + str(self.page_no()) + "/{nb}", 0, 0, "C")


def generar_carnet_PDF(socio, photo, url):
    """Genera el pdf de una cuota paga"""
    pdf = PDFCarnet()
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_font("Arial", "B", 16)
    pdf.set_font("Arial", "", 12)
    pdf.image(photo)
    pdf.image(
        "http://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=" + url + "&.png"
    )
    response = make_response(pdf.output(dest="S").encode("latin-1"))
    response.headers.set(
        "Content-Disposition", "attachment", filename="Carnet" + ".pdf"
    )
    response.headers.set("Content-Type", "application/pdf")
    return response
