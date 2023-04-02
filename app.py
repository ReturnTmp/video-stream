from flask import Flask, send_file
import os
import base64
import random

app = Flask(__name__)

@app.route('/video')
def video():
    video_dir = os.path.join(os.path.dirname(__file__), 'video')
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
    video_file = random.choice(video_files)
    video_path = os.path.join(video_dir, video_file)
    with open(video_path, 'rb') as f:
        video_data = f.read()
    base64_data = base64.b64encode(video_data)
    return {'name': video_file, 'data': base64_data}

if __name__ == '__main__':
    app.run()