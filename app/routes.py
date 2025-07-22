import os
from flask import request, redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename

from app.utils import delete_uploaded_file

ALLOWED_EXTENSIONS = {'mp4' }# , 'jpg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register_routes(app):
    @app.route('/restart', methods=['POST'])
    def restart_autoplay():
        try:
            os.system('reboot')
            flash("Rebooting...")
        except Exception as e:
            flash(f"Error: {e}")
        return redirect(url_for('index'))

    
    @app.route('/')
    def index():
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('index.html', files=files)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
        else:
            flash('Invalid file type')
        return redirect(url_for('index'))

    @app.route('/files/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
    @app.route('/delete/<filename>', methods=['POST'])
    def delete_file(filename):
        if delete_uploaded_file(app.config['UPLOAD_FOLDER'], filename):
            flash(f"Deleted {filename}")
        else:
            flash(f"File {filename} not found")
        return redirect(url_for('index'))
    


