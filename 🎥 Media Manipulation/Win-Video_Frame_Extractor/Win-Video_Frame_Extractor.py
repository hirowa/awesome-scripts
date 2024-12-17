import os
import shutil
import subprocess

def get_video_files():
    """Get all video files in the current working directory."""
    video_extensions = ('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')
    files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith(video_extensions)]
    return files

def create_folder_for_video(video_file):
    """Create a folder with the same name as the video file (without extension)."""
    folder_name = os.path.splitext(video_file)[0]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def create_frames_folder(video_folder):
    """Create a 'Frames' folder inside the video folder."""
    frames_folder = os.path.join(video_folder, 'Frames')
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    return frames_folder

def extract_frames(video_path, frames_folder, max_frames):
    """Use FFmpeg to extract frames from the video."""
    ffmpeg_command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'select=not(mod(n\\,{max_frames}))',  # Extract frames every n frames
        '-vsync', 'vfr',
        os.path.join(frames_folder, 'frame_%04d.jpg')
    ]
    subprocess.run(ffmpeg_command)

def move_video_to_folder(video_file, folder_name):
    """Move video file to its corresponding folder."""
    shutil.move(video_file, os.path.join(folder_name, video_file))

def main():
    video_files = get_video_files()
    if not video_files:
        print("No video files found in the current directory.")
        return

    max_frames = int(input("Enter the maximum number of frames to extract: "))

    for video in video_files:
        print(f"Processing video: {video}")

        # Create folder for video and frames
        video_folder = create_folder_for_video(video)
        frames_folder = create_frames_folder(video_folder)

        # Move video file to its folder
        move_video_to_folder(video, video_folder)

        # Full path to the moved video
        video_path = os.path.join(video_folder, video)

        print(f"Extracting frames for video {video}. Frames will be saved in: {frames_folder}")

        # Extract frames using FFmpeg
        extract_frames(video_path, frames_folder, max_frames)

        print(f"Frames extracted for {video}.\n")

if __name__ == "__main__":
    main()
