import os
import subprocess

def merge_audio_video(video_path, audio_path, output_path):
    # Constructing the FFmpeg command as a string
    command = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac -strict experimental "{output_path}"'
    # Running the command
    subprocess.run(command, shell=True)

def main():
    while True:
        print("\nThis script merges an audio file with a video file.")
        print("The merged file will be saved in the same directory as the video file with '_merged' appended to its name.")
        print("-----")
        
        video_path = input("Enter the path to the video file: ").strip().strip('"')
        audio_path = input("Enter the path to the audio file: ").strip().strip('"')

        # Construct the output file path
        base, _ = os.path.splitext(video_path)
        output_path = f"{base}_merged.mp4"

        merge_audio_video(video_path, audio_path, output_path)
        print(f"Merged file saved as {output_path}")

        # Ask the user if they want to process more files
        another = input("Do you want to merge another audio with a video file? (yes/no): ").lower()
        if another != 'yes':
            break

# Run the main function
main()