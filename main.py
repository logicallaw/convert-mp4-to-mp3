import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_file, mp3_file):
    try:
        video = VideoFileClip(mp4_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)
        print(f"Successfully converted: {mp3_file}")
    except Exception as e:
        print(f"Failed: {e}")

def batch_convert_mp4_to_mp3(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(input_dir, filename)
            mp3_path = os.path.join(output_dir, filename.replace(".mp4", ".mp3"))
            convert_mp4_to_mp3(mp4_path, mp3_path)

# 변환 실행
input_directory = "inputs"
output_directory = "outputs"

batch_convert_mp4_to_mp3(input_directory, output_directory)