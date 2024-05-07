from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    heading_content = request.form['heading_content']
    heading_font_size = request.form['heading_font_size']
    heading_font_color = request.form['heading_font_color']
    notes_content = request.form['notes_content']
    notes_font_size = request.form['notes_font_size']
    notes_font_color = request.form['notes_font_color']

    pdf = FPDF()
    pdf.add_page()

    # Heading
    pdf.set_font("Arial", size=int(heading_font_size))
    pdf.set_text_color(*hex_to_rgb(heading_font_color))
    pdf.cell(200, 10, txt=heading_content, ln=True, align='C')

    # Notes
    pdf.set_font("Arial", size=int(notes_font_size))
    pdf.set_text_color(*hex_to_rgb(notes_font_color))
    pdf.multi_cell(0, 10, txt=notes_content)

    pdf_output = 'static/notes.pdf'
    pdf.output(pdf_output)

    return send_file(pdf_output, as_attachment=True)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) / 255.0 for i in (0, 2, 4))

if __name__ == '__main__':
    app.run(debug=True)
