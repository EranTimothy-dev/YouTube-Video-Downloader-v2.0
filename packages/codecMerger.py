import subprocess
import os
from pathlib import Path

def path_to_downloads():
    '''
    Takes 0 positional arguments.
    checks the users operating and finds the path to the downloads folder and returns it as a string.
    '''
    path_to_download = str(os.path.join(Path.home(), 'Downloads'))
    return path_to_download

def merge_codecs(video_file,audio_file,output_file):
    '''
    Takes 3 arguments:
        video_file path & name: path/to/video_file
        audio_file path & name: path/to/audio_file
        final output file path & name: path/to/output_file
    Requires ffmpeg to be installed and added to path in local system and ffmpeg.exe file 
    should be in the current working repository/directory to run this function without errors 
    '''
    path = path_to_downloads()
    output = path + "\\" + output_file
    codec = "copy"
    subprocess.run(f"ffmpeg -y -i {video_file} -i {audio_file} -c {codec} {output}")
    print("Video and Audio files merged successfully.")

    if os.path.exists(video_file) and os.path.exists(audio_file):
        os.remove(video_file)
        os.remove(audio_file)
        # os.rmdir(path+"\\videos")
        os.rmdir("videos")
        print("Unnecessary files deleted successfully.")
    else:
        print("file not found")
    
    