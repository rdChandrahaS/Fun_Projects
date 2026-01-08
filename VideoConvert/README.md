# Bulk TS to MP4 Converter

A tailored Python script to automate the batch conversion of `.ts` (MPEG Transport Stream) video files to `.mp4` format. This tool uses **FFmpeg** to perform a "remux" (stream copy), ensuring conversions are instantaneous and technically lossless (0% quality loss).

## 🚀 Features

* **Batch Processing:** Automatically finds all `.ts` files in a specified directory.
* **Lossless Conversion:** Uses `vcodec='copy'` and `acodec='copy'` to change the container format without re-encoding the audio or video streams.
* **High Speed:** Converts files in seconds rather than minutes.
* **Error Handling:** Skips corrupt files without crashing the entire batch process.
* **Clean Output:** Suppresses verbose FFmpeg logs, showing only clear status updates (Converting -> DONE/FAILED).

## 📋 Prerequisites

Before running the script, ensure you have the following installed:

1.  **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2.  **FFmpeg (System Tool)**: You must have the FFmpeg software installed on your computer and added to your system's PATH.
    * *Windows Guide:* [How to install FFmpeg on Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)
    * To verify, open Command Prompt and type: `ffmpeg -version`
3.  **Python Library**: You need the wrapper library for the script to run.

## 🛠️ Installation

1.  Clone this repository or download the script file.
2.  Install the required Python dependency via your terminal/command prompt:

```bash
    pip install ffmpeg-python

> Note: Do not install the package simply named ffmpeg. The correct package for this script is ffmpeg-python.

    ⚙️ Configuration
        By default, the script looks for videos in D:\VideoConvert.

    To change the target folder:

        Open the script in any text editor (Notepad, VS Code, etc.).

        Locate line 5 (or the configuration section):

        folder_path = r"D:\VideoConvert"


    The script will display the progress:

        Found 5 files. Starting conversion...
        Converting: video1.ts -> video1.mp4 ... [DONE]
        Converting: video2.ts -> video2.mp4 ... [DONE]
        All conversions completed.

❓ Troubleshooting
Issue --> Solution
ModuleNotFoundError: No module named 'ffmpeg'  --> Run pip install ffmpeg-python.
FileNotFoundError: [WinError 2] The system cannot find the file specified,FFmpeg is not installed or not in your System PATH. --> Install FFmpeg binaries.
Error: The folder '...' was not found,The folder path in the script configuration does not exist. -->  Create the folder or update the folder_path variable.