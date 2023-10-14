"""
The flask application package.
"""
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploaded_files'  # Каталог для загруженных файлов
app.config['SECRET_KEY'] = 'your_secret_key'  # Установите ваш собственный секретный ключ

class UploadForm(FlaskForm):
    pdf_file = FileField('PDF')

@app.route('/upload', methods=['POST'])
def index():
    form = UploadForm()
    pdf_file = form.pdf_file.data
    if pdf_file:
        filename = pdf_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        #Мб какие то условия дополнительные, валидация
        caseRealization()
        return 'Yes.'        
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

def caseRealization():
    #SashaAlgoritm
    return

import RZD.views
