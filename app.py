from flask import Flask, request, render_template, send_file
from forms import inputForm

import os
import downloader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linuxdegilgnulinux'


@app.route('/')
def home():
    form = inputForm(request.form)
    return render_template('index.html', form=form)


@app.route('/start', methods=['GET', 'POST'])
def start():
    form = inputForm(request.form)
    if request.method == 'POST' and form.validate():
        dwnldr = downloader.Downloader()
        youtube_url = request.form.get('youtube_url')
        os.chdir('mp3_files/')
        dwnldr.startDownloading(youtube_url)
        confirm = 1
        os.chdir('../')
        return render_template('index.html', form=form, confirm=confirm)
    return render_template('index.html', form=form)


@app.route('/download', methods=['GET', 'POST'])
def download():
    files = os.listdir('mp3_files')
    file_name = files[0]
    try:
        return send_file('mp3_files/' + file_name, as_attachment=True, attachment_filename=str(file_name) + '.mp3')
    except Exception as e:
        return str(e)