import subprocess
import os
from pathlib import Path

def path_to_downloads():
    path_to_download = str(os.path.join(Path.home(), 'Downloads'))
    return path_to_download

def merge_codecs(video_file,audio_file,output_file):
    '''
    Takes 3 arguments:
        video_file path & name: path/to/video_file
        audio_file path & name: path/to/audio_file
        final output file path & name: path/to/output_file 
    '''
    path = path_to_downloads()
    output = path + "\\" + output_file
    codec = "copy"
    subprocess.run(f"ffmpeg -i {video_file} -i {audio_file} -c {codec} {output}")
    
    
    
# path = path_to_downloads()
# newpath = path + "\output"
# print(newpath)