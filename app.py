from flask import Flask, request, render_template, send_file
from forms import inputForm

import os
import downloader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linuxdegilgnulinux'


@app.route('/')
def home():
    music = os.listdir('mp3_files/')
    if music:
        if music[0] == 'ilteris.mp3':
            os.remove('mp3_files/ilteris.mp3')
    form = inputForm(request.form)
    return render_template('index.html', form=form)


@app.route('/start', methods=['GET', 'POST'])
def start():
    music = os.listdir('mp3_files/')
    if music:
        if music[0] == 'ilteris.mp3':
            os.remove('mp3_files/ilteris.mp3')
    form = inputForm(request.form)
    if request.method == 'POST' and form.validate():
        music = os.listdir('mp3_files/')
        if music:
            if music[0] == 'ilteris.mp3':
                os.remove('mp3_files/ilteris.mp3')
        dwnldr = downloader.Downloader()
        youtube_url = request.form.get('youtube_url')
        dwnldr.startDownloading(youtube_url)
        file_name = os.listdir('mp3_files/')
        file_name = str(file_name[0])

        return send_file('mp3_files/' + file_name, as_attachment=True)
    return render_template('index.html', form=form)
