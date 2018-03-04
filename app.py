from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

def create_pdf(template_name, data):
    """ Generates a pdf from a template """
    render = render_template(template_name, data=data)

    # so that wkhtmltopdf does not print anything
    options = {
        'quiet': ''
    }
    #False is there so that generated pdf is retained in memory, not written on disk
    pdf = pdfkit.from_string(render, False, options)
    return pdf

@app.route('/pdf/<date>')
def pdf_generator(date):
    response = make_response(create_pdf("template.html", {"date": date}))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=report.pdf'
    return response
