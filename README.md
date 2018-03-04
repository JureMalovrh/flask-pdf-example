## Simple PDF generation

### Technologies used (needs to be installed):
- [Flask](http://flask.pocoo.org/)
- [pdfkit](https://pypi.python.org/pypi/pdfkit)

### How to run
`FLASK_APP=app.py flask run`

After you run application, visit [local server page](localhost:5000/pdf/test). You should see generated pdf. Route exposed is `/pdf/<date>`, where your date will be included inside a pdf title.