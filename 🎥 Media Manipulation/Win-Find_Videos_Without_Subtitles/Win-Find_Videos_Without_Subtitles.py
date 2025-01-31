import os

# Function to find video files that do not have corresponding subtitle files
def find_videos_without_subtitles(directory):
    video_extensions = {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'}  # List of common video file extensions
    missing_subtitles = []  # List to store video files without subtitles
    
    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        # Get video file names (without extensions)
        video_files = {os.path.splitext(f)[0] for f in files if os.path.splitext(f)[1].lower() in video_extensions}
        # Get subtitle file names (without extensions)
        subtitle_files = {os.path.splitext(f)[0] for f in files if f.lower().endswith('.srt')}
        
        # Check if each video file has a corresponding subtitle file
        for video in video_files:
            if video not in subtitle_files:
                missing_subtitles.append(os.path.join(root, video))  # Add missing videos to the list
    
    return missing_subtitles  # Return the list of videos without subtitles

if __name__ == "__main__":
    # Get directory path from user input and clean up any surrounding quotes
    directory = input("Enter the directory path: ").strip().strip('"')
    
    # Validate if the given path is a directory
    if not os.path.isdir(directory):
        print("Invalid directory path.")  # Print error message if path is not valid
    else:
        missing = find_videos_without_subtitles(directory)  # Find videos missing subtitles
        
        # Display results
        if missing:
            print("The following video files are missing subtitles:")
            for video in missing:
                print(video)  # Print each video without a subtitle
        else:
            print("All video files have corresponding subtitles.")  # Message if all videos have subtitles
