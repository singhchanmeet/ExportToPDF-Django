# ExportToPDF-Django

## 📝 Description
While the <a href="https://django-import-export.readthedocs.io/en/latest/api_admin.html">Django-Import-Export</a> Library supports the export of records in CSV, XLS, HTML and many other formats directly from
the Django Admin Panel, there is no Library to export the records in PDF format. This can be a common use case in many kinds of
forms.

So, the <a href="https://github.com/singhchanmeet/ExportToPDF-Django/">ExportToPDF-Django</a> Repository demonstrates a simple yet useful way to export records in PDF format without the use of
any Third Party Library.


## :gear: How To Use

1) Installation (Inside your Python Virtual Environment) :
```bash
pip install -r requirements.txt

```

2) Setting up Django Project :
```bash
python manage.py makemigrations

```
```bash
python manage.py migrate

```
```bash
python manage.py runserver

```
  Now you can access the Form at 127.0.0.1:8000 and the Admin Panel at 127.0.0.1:8000/admin
  
 ## 🎥 Video Demo

https://github.com/singhchanmeet/ExportToPDF-Django/assets/119502048/71177895-b399-4bda-8b8e-233000157232


## 💡 How to Customize the Generated PDF
You can style the PDF just like an HTML page by editing the <a href="https://github.com/singhchanmeet/ExportToPDF-Django/blob/main/templates/pdfs.html">pdfs.html</a> and <a href="https://github.com/singhchanmeet/ExportToPDF-Django/blob/main/static/pdfstyle.css">pdfstyle.css</a> files!

This is possible because we are just passing a QuerySet of the selected records from the Admin Panel to an HTML page and then 
using the Browser's default PDF print feature (<a href="https://www.w3schools.com/jsref/met_win_print.asp"> window.print() </a>)
