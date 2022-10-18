import csv
from io import StringIO
from fpdf import FPDF
from datetime import datetime
from flask import make_response

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.set_xy(0, 0)
        self.cell(200, 40, "Listado de Socios", 0, 0, 'R')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

class PDFRecibo(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.set_xy(0, 0)
        self.cell(200, 40, "Recibo de pago", 0, 0, 'R')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def generarPDF(data_socios):
    cant_socios = 0
    pdf = PDF()
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 20, f'{datetime.now().date()}')
    pdf.set_font('Arial', 'B', 12)
    y_height = 5
    pdf.set_xy(0, 50)
    pdf.cell(15)
    pdf.cell(30, y_height, 'Nombre', border=1)
    pdf.cell(30, y_height, 'Apellido', border=1)
    pdf.cell(25, y_height, 'Dni', border=1)
    pdf.cell(25, y_height, 'Telefono', border=1)
    pdf.cell(30, y_height, 'Genero', border=1)
    pdf.cell(40, y_height, 'Direccion', border=1, ln=1)
    pdf.set_font('Arial', '', 12)
    for socio in data_socios:
        cant_socios += 1
        if(cant_socios == 41):
            pdf.add_page()
            cant_socios = 0
        pdf.cell(5)
        pdf.cell(30, y_height, socio["nombre"], border=1)
        pdf.cell(30, y_height, socio["apellido"], border=1)
        pdf.cell(25, y_height, socio["dni"], border=1)
        pdf.cell(25, y_height, socio["telefono"], border=1)
        pdf.cell(30, y_height, socio["genero"], border=1)
        pdf.cell(40, y_height, socio["direccion"], border=1, ln=1)
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename='socios' + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

def generarCSV(data_socios):
    headers = ['nro_socio', 'apellido', 'nombre','tipo_documento', 'dni', 'email', 'telefono', 'direccion', 'genero', 'activo']
    si = StringIO()
    with open('socios.csv', 'w') as f:
        writer = csv.DictWriter(si, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_socios)
        output = make_response(si.getvalue())
        output.headers.set('Content-Disposition', 'attachment', filename='socios' + '.csv')
        output.headers.set('Content-Type', 'application/csv')
    return output

def generarReciboPDF(data):
    '''Genera el pdf de una cuota paga'''
    pdf = PDFRecibo()
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 20, f'{datetime.now().date()}', ln=1)
    pdf.cell(500, 30, data["encabezado"])
    pdf.set_font('Arial', 'B', 12)
    y_height = 5
    pdf.set_xy(0, 50)
    pdf.cell(15)
    pdf.cell(70, y_height, 'Cuota numero '+ str(data["pago"].nro_cuota) + " del año " + str(data["pago"].año_cuota), ln=1)
    pdf.cell(180, y_height, "Socio: " + data["pago"].socio.apellido + " "+ data["pago"].socio.nombre, ln=1)
    pdf.cell(25, y_height, "Monto total:" )
    pdf.cell(125)
    pdf.cell(20, y_height, str(data["pago"].total), ln=1)
    pdf.cell(35, y_height, 'Fecha de pago:')
    pdf.cell(115)
    pdf.cell(25, y_height, str(data["pago"].fecha_pago.strftime('%Y-%m-%d')), ln=1)
    
    pdf.set_font('Arial', '', 12)
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename='Recibo' + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response