import ffmpeg
import os

# 1. Define the directory containing the videos
folder_path = r"D:\VideoConvert"

def convert_all_ts_videos():
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' was not found.")
        return

    # 2. Find all .ts files in that folder
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.ts')]

    if not files:
        print(f"No .ts files found in {folder_path}")
        return

    print(f"Found {len(files)} files. Starting conversion...\n")

    # 3. Loop through each file and convert
    for filename in files:
        input_path = os.path.join(folder_path, filename)
        
        # Create the output name (same name, but .mp4 extension)
        output_filename = os.path.splitext(filename)[0] + ".mp4"
        output_path = os.path.join(folder_path, output_filename)

        print(f"Converting: {filename} -> {output_filename} ...", end=" ")

        try:
            (
                ffmpeg
                .input(input_path)
                .output(output_path, vcodec='copy', acodec='copy') # 'copy' ensures instant conversion without quality loss
                .run(quiet=True, overwrite_output=True) # quiet=True hides the messy ffmpeg logs
            )
            print("[DONE]")
            
        except ffmpeg.Error as e:
            print("[FAILED]")
            print(f"Error details: {e}")

    print("\nAll conversions completed.")

if __name__ == "__main__":
    convert_all_ts_videos()






'''
import ffmpeg  # Import the library to talk to the FFmpeg tool
import os      # Import the library to manage files and folders on Windows

# --- CONFIGURATION ---
# The folder where your videos are located.
# We use 'r' before the quote to make it a "raw string". 
# This tells Python to treat backslashes (\) as normal text, not special commands.
folder_path = r"D:\VideoConvert"

def convert_all_ts_videos():
    # 1. VALIDATION: Check if the folder actually exists to avoid crashing
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' was not found.")
        return

    # 2. SCANNING: Find all files in the folder that end with .ts
    # os.listdir() -> Gets a list of every file in the folder
    # if f.lower().endswith('.ts') -> Filters the list to only keep .ts files
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.ts')]

    # If the list is empty, stop the program
    if not files:
        print(f"No .ts files found in {folder_path}")
        return

    print(f"Found {len(files)} files. Starting conversion...\n")

    # 3. PROCESSING: Loop through the list of found files one by one
    for filename in files:
        # Create the full path to the input file 
        # (Joins "D:\VideoConvert" with "video.ts" -> "D:\VideoConvert\video.ts")
        input_path = os.path.join(folder_path, filename)
        
        # Create the name for the output file
        # os.path.splitext splits "video.ts" into two parts: ("video", ".ts")
        # We take part [0] ("video") and add ".mp4" to it.
        output_filename = os.path.splitext(filename)[0] + ".mp4"
        
        # Create the full path for the new mp4 file
        output_path = os.path.join(folder_path, output_filename)

        print(f"Converting: {filename} -> {output_filename} ...", end=" ")

        try:
            # 4. CONVERSION (REMUXING)
            (
                ffmpeg
                .input(input_path) # Load the .ts file
                
                # 'vcodec' = Video Codec. 'copy' means: take the video stream data exactly as is.
                # 'acodec' = Audio Codec. 'copy' means: take the audio stream data exactly as is.
                # This ensures 0% quality loss and 100% speed because we are not re-compressing.
                .output(output_path, vcodec='copy', acodec='copy') 
                
                # Execute the command
                # quiet=True -> Hides the messy technical text FFmpeg usually outputs
                # overwrite_output=True -> If 'video.mp4' already exists, replace it
                .run(quiet=True, overwrite_output=True) 
            )
            print("[DONE]")
            
        except ffmpeg.Error as e:
            # 5. ERROR HANDLING
            # If the file is corrupt or there is an issue, catch the error so the script doesn't crash
            print("[FAILED]")
            print(f"Error details: {e}")

    print("\nAll conversions completed.")

# Run the function when the script starts
if __name__ == "__main__":
    convert_all_ts_videos()
'''