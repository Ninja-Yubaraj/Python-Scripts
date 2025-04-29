#!/usr/bin/env python3
#
# Script name: Simple-HTTP-Server.py
# Version: 1.0.0
# Description: A Python script to upload and save multiple files locally via a simple web page.
# Dependencies: Flask
# Github: https://github.com/Ninja-Yubaraj/Python-Scripts
# Gitlab: https://gitlab.com/Ninja-Yubaraj/Python-Scripts
# License: https://gitlab.com/Ninja-Yubaraj/Python-Scripts/LICENSE
# Contributors: Yubaraj Sarkar

import os
from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'Uploads')

# Ensure the Uploads directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# No file size limit (optional: set app.config['MAX_CONTENT_LENGTH'] if needed)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Simple HTML upload form
UPLOAD_PAGE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Upload Files</title>
</head>
<body>
  <h1>Upload Files</h1>
  <form method="POST" action="/" enctype="multipart/form-data">
    <input type="file" name="files" multiple>
    <br><br>
    <button type="submit">Upload</button>
  </form>
  <h2>Uploaded Files:</h2>
  <ul>
    {% for filename in files %}
      <li><a href="/uploads/{{ filename }}" target="_blank">{{ filename }}</a></li>
    {% endfor %}
  </ul>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('files')
        for file in uploaded_files:
            if file.filename:  # Check if file has a filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(UPLOAD_PAGE, files=files)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
