import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_file, mp3_file):
    try:
        video = VideoFileClip(mp4_file)
        audio = video.audio
        audio.write_audiofile(mp3_file)
        print(f"Conversion successful: {mp4_file} -> {mp3_file}")
    except Exception as e:
        print(f"Conversion failed for {mp4_file}: {e}")

def batch_convert_mp4_to_mp3(input_dir, output_dir):
    # Ensure input and output directories exist
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Created input directory: {input_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(input_dir, filename)
            mp3_path = os.path.join(output_dir, filename.replace(".mp4", ".mp3"))
            convert_mp4_to_mp3(mp4_path, mp3_path)

    if not any(filename.endswith(".mp4") for filename in os.listdir(input_dir)):
        print("No MP4 files found in the input directory.")

# Run conversion
input_directory = "inputs"
output_directory = "outputs"

batch_convert_mp4_to_mp3(input_directory, output_directory)